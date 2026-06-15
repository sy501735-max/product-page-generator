"""tests/test_core.py — 핵심 기능 단위 테스트"""

import sys
import tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from src.generator.page_generator import ProductPageGenerator


SAMPLE_CSV = """name,price,features,target,category,brand
테스트 세럼,38000,수분 공급|피부 톤 개선|빠른 흡수,20-40대 여성,스킨케어,테스트브랜드
저가 크림,8000,보습|간편,누구나,스킨케어,
고가 앰플,150000,프리미엄 성분|고함량,피부 관리에 진심인 분,스킨케어,
"""


@pytest.fixture
def sample_csv(tmp_path):
    f = tmp_path / "products.csv"
    f.write_text(SAMPLE_CSV, encoding="utf-8")
    return str(f)


@pytest.fixture
def generator(sample_csv):
    return ProductPageGenerator(sample_csv)


class TestPageGenerator:
    def test_load_and_generate(self, generator):
        results = generator.generate_all()
        assert len(results) == 3

    def test_html_contains_product_name(self, generator):
        results = generator.generate_all()
        assert "테스트 세럼" in results[0]["html"]

    def test_html_contains_price(self, generator):
        results = generator.generate_all()
        assert "38000" in results[0]["html"]

    def test_html_contains_features(self, generator):
        results = generator.generate_all()
        assert "수분 공급" in results[0]["html"]

    def test_instagram_caption_generated(self, generator):
        results = generator.generate_all()
        caption = results[0]["instagram_caption"]
        assert "테스트 세럼" in caption
        assert "#" in caption

    def test_ad_copy_generated(self, generator):
        results = generator.generate_all()
        assert results[0]["ad_copy"] != ""

    def test_price_tier_premium(self, generator):
        assert generator._get_price_tier("150000") == "premium"

    def test_price_tier_mid(self, generator):
        assert generator._get_price_tier("38000") == "mid"

    def test_price_tier_entry(self, generator):
        assert generator._get_price_tier("8000") == "entry"

    def test_features_pipe_separator(self, generator):
        features = generator._parse_features("수분 공급|피부 톤 개선|빠른 흡수")
        assert len(features) == 3
        assert "수분 공급" in features

    def test_save_outputs(self, generator, tmp_path):
        results = generator.generate_all()
        saved = generator.save_outputs(results, str(tmp_path))
        assert len(saved) > 0
        for path in saved:
            assert Path(path).exists()

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            g = ProductPageGenerator("nonexistent.csv")
            g.generate_all()

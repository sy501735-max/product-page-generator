"""
Product Page Generator — Main Entry Point
CSV 상품 정보 → HTML 상세페이지 + 인스타 캡션 + 광고 카피 자동 생성
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.generator.page_generator import ProductPageGenerator


def main():
    parser = argparse.ArgumentParser(
        description="상품 정보 CSV → HTML 상세페이지 + 마케팅 카피 자동 생성",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예시:
  python -m src.main --products data/sample_products.csv
  python -m src.main --products data/sample_products.csv --output examples
        """,
    )
    parser.add_argument("--products", default="data/sample_products.csv")
    parser.add_argument("--output", default="examples")
    args = parser.parse_args()

    print("=" * 50)
    print("  🛍️  Product Page Generator")
    print("  상품 상세페이지 + 마케팅 카피 자동 생성")
    print("=" * 50)

    print(f"\n📦 상품 데이터 로드 중: {args.products}\n")

    generator = ProductPageGenerator(args.products)
    results = generator.generate_all()
    saved = generator.save_outputs(results, args.output)

    print(f"  ✅ 처리된 상품 수: {len(results)}개")
    for path in saved:
        print(f"  📄 저장됨: {path}")

    print(f"\n✨ 완료! {args.output}/ 폴더에서 결과를 확인하세요.\n")


if __name__ == "__main__":
    main()

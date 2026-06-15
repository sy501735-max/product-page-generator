# 🛍️ Product Page Generator
### CSV 상품 정보 → HTML 상세페이지 + 인스타 캡션 + 광고 카피 자동 생성

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **쇼핑몰/뷰티 브랜드 운영자를 위한 오픈소스 마케팅 자동화 도구**
> 상품 정보 CSV 한 장 → HTML 상세페이지 + 인스타그램 캡션 + 광고 카피까지 자동 생성

---

## 🌟 왜 만들었나요?

상품이 많아질수록 상세페이지 제작이 병목이 됩니다.

- 상품 하나당 상세페이지 외주 비용 수십만 원
- 인스타 홍보글도 매번 새로 써야 하고
- 광고 카피도 따로 만들어야 하고

그래서 직접 만들었습니다.
**상품 정보만 CSV에 입력하면 30초 안에 전부 완성됩니다.**

---

## ✨ 주요 기능

### 📄 1. HTML 상세페이지 자동 생성
- 상품명, 가격, 특징, 타겟 고객을 입력하면 완성된 HTML 상세페이지 생성
- 카테고리별 감성 키워드 자동 적용 (스킨케어, 헤어, 메이크업, 패션 등)
- 가격대별 포지셔닝 문구 자동 결정 (프리미엄 / 가성비 / 입문)
- 반응형 디자인, 모바일 최적화

### 📱 2. 인스타그램 캡션 자동 생성
- 상품 특징 기반 감성 캡션
- 카테고리 맞춤 해시태그 자동 추가
- DM 유도 CTA 포함

### 📢 3. 광고 카피 자동 생성
- 짧고 임팩트 있는 광고 문구
- 스마트스토어, 쿠팡, 인스타 광고에 바로 사용 가능

### 📦 4. 일괄 처리
- CSV 한 파일에 상품 여러 개 → 전부 한 번에 생성

---

## 🚀 빠른 시작

### 설치

```bash
git clone https://github.com/sy501735-max/product-page-generator.git
cd product-page-generator
pip install -e .
```

### 실행

```bash
python -m src.main --products data/sample_products.csv
```

---

## 📋 상품 데이터 형식 (CSV)

```csv
name,price,features,target,category,brand
토닝 앰플 세럼,38000,피부 톤 균일하게 정돈|촉촉한 수분 공급|빠른 흡수력,20-40대 여성,스킨케어,브랜드명
볼륨 매직 샴푸,22000,볼륨 업 효과|두피 케어|손상 모발 영양,모발이 얇은 분,헤어,
```

| 필드 | 설명 | 예시 |
|------|------|------|
| `name` | 상품명 | 토닝 앰플 세럼 |
| `price` | 가격 (숫자만) | 38000 |
| `features` | 주요 특징 (`\|` 구분) | 수분 공급\|빠른 흡수 |
| `target` | 타겟 고객 | 20-40대 여성 |
| `category` | 카테고리 | 스킨케어 |
| `brand` | 브랜드명 (선택) | ToneOnMatch |

---

## 📂 프로젝트 구조

```
product-page-generator/
├── src/
│   ├── generator/
│   │   └── page_generator.py   # 핵심 생성 엔진
│   └── main.py                 # CLI 진입점
├── data/
│   └── sample_products.csv     # 샘플 상품 데이터
├── examples/                   # 생성된 결과물
├── tests/                      # 단위 테스트
└── pyproject.toml
```

---

## 🧪 테스트

```bash
pip install pytest
pytest tests/ -v
```

---

## 📈 적용 사례

- 뷰티 브랜드: 신상품 출시마다 상세페이지 제작 시간 90% 단축
- 스마트스토어 셀러: 상품 50개 일괄 처리로 하루 작업을 30분으로 단축
- 인스타 마켓: 상품 홍보 캡션 자동 생성으로 일일 포스팅 부담 해소

---

## 🗺 로드맵

- [ ] OpenAI API 연동 (GPT 기반 더욱 자연스러운 카피 생성)
- [ ] 이미지 업로드 → 상품명/특징 자동 추출
- [ ] 네이버 스마트스토어 형식 출력 지원
- [ ] 웹 인터페이스 (드래그앤드롭 CSV 업로드)
- [ ] 다국어 지원 (영어, 일본어)

---

## 🤝 기여하기

[CONTRIBUTING.md](CONTRIBUTING.md)를 먼저 읽어주세요.

---

## 📜 라이선스

MIT License

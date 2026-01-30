---
name: python-pro
description: Pythonic한 코드 작성, 최신 도구(uv, ruff, poetry) 활용, 비동기 프로그래밍 등 Python 전문가를 위한 가이드입니다.
---

# Python Pro Skill

이 스킬은 Antigravity의 **Developer** 에이전트가 고품질의 Python 코드를 작성하도록 돕습니다.

## 1. 개발 환경 및 패키지 관리
- **Tooling**: `uv` (빠른 패키지 설치), `poetry` (의존성 관리) 사용 권장.
- **Virtual Environment**: 프로젝트 루트에 `.venv` 생성.

## 2. 코드 스타일 (Code Style) - The Pythonic Way
- **Formatter/Linter**: `ruff` 사용 권장 (Black, Isort, Flake8 대체).
- **Type Hinting**: 모든 함수와 클래스 메서드에 타입 힌트 추가 (mypy 호환).
    ```python
    def process_data(data: list[str]) -> dict[str, int]:
        ...
    ```
- **Docstrings**: Google Style Docstring 사용.

## 3. 비동기 프로그래밍 (AsyncIO)
- I/O 바운드 작업(DB 쿼리, API 호출) 시 `async`/`await` 필수 사용.
- 동기 라이브러리(`requests` 등) 대신 비동기 라이브러리(`httpx`, `aiohttp`) 사용.

## 4. 구조적 패턴 (Structural Patterns)
- **Pydantic**: 데이터 검증 및 설정 관리에 적극 활용.
- **Dependency Injection**: 의존성 주입을 통해 테스트 용이성 확보.

## 5. 테스트 (Testing)
- **Framework**: `pytest`.
- **Async Test**: `pytest-asyncio` 플러그인 활용.

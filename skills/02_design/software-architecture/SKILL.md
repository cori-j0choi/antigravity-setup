---
name: software-architecture
description: 시스템 아키텍처, 디자인 패턴, 모듈화 전략을 제시하는 설계 전문 스킬입니다.
---

# Software Architecture Skill

이 스킬은 Antigravity의 **Architect** 에이전트가 견고하고 유지보수 가능한 시스템 구조를 설계하도록 돕습니다.

## 1. 핵심 원칙 (Core Principles)
1.  **Separation of Concerns (관심사의 분리)**: UI, 비즈니스 로직, 데이터 접근 계층을 명확히 분리합니다.
2.  **Single Responsibility Principle (단일 책임 원칙)**: 하나의 컴포넌트나 함수는 하나의 역할만 수행합니다.
3.  **DRY (Don't Repeat Yourself)**: 중복 코드를 지양하고 재사용 가능한 모듈로 추출합니다.
4.  **KISS (Keep It Simple, Stupid)**: 불필요한 복잡성을 피하고 가장 단순한 해결책을 선택합니다.

## 2. 아키텍처 문서화 (`findings.md`)
설계 단계에서 Architect는 다음 내용을 `findings.md`에 기록해야 합니다.

```markdown
# Architecture Design

## 1. System Overview
- [전체 시스템 구조도 (Mermaid 등)]

## 2. Tech Stack
- Frontend: [React, Next.js, etc.]
- Backend: [Node.js, Python, etc.]
- Database: [PostgreSQL, Redis, etc.]

## 3. Data Model (Schema)
- [Entity 1]: [Attributes...]
- [Entity 2]: [Attributes...]

## 4. API Design
- [Endpoint 1]: [Method] [URL] - [Description]

## 5. Security Considerations
- Authentication/Authorization 전략
- 데이터 암호화 및 보호 조치
```

## 3. 디자인 패턴 (Design Patterns)
상황에 맞는 적절한 디자인 패턴을 제안합니다.
- **Repository Pattern**: 데이터 접근 로직의 추상화.
- **Service Layer Pattern**: 비즈니스 로직의 캡슐화.
- **Observer Pattern**: 이벤트 기반 통신 시스템.

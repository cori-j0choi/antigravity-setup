---
name: backend-architect
description: 확장 가능하고 안전한 백엔드 시스템(API, DB, Server)을 설계하는 전문가 스킬입니다.
---

# Backend Architect Skill

이 스킬은 Antigravity의 **Architect** 및 **Developer** 에이전트가 견고한 백엔드 인프라를 구축하도록 돕습니다.

## 1. API 설계 (API Design)

### 1.1 RESTful Best Practices
- **Resource Naming**: 명사형 URL 사용 (e.g., `/users`, `/products`).
- **HTTP Methods**: GET(조회), POST(생성), PUT/PATCH(수정), DELETE(삭제) 의미 준수.
- **Status Codes**: 200(OK), 201(Created), 400(Bad Request), 401(Unauthorized), 500(Server Error) 등 정확한 상태 코드 반환.

### 1.2 GraphQL (선택 사항)
- 과다한 데이터 페칭(Over-fetching)과 부족한 페칭(Under-fetching) 문제를 해결하기 위해 사용 고려.

## 2. 데이터베이스 모델링 (Database Modeling)

### 2.1 Schema Design
- **Normalization (정규화)**: 데이터 중복을 최소화하여 무결성 유지 (보통 3정규형까지).
- **Indexing**: 자주 조회되는 컬럼에 인덱스를 생성하여 성능 최적화.

### 2.2 ORM (Object-Relational Mapping)
- **Python**: SQLAlchemy, Tortoise ORM 등 사용 권장.
- **Node.js**: Prisma, TypeORM 등 사용 권장.

## 3. 보안 (Security)
- **Authentication**: JWT 또는 OAuth2 기반 인증 시스템 구축.
- **Authorization**: RBAC(Role-Based Access Control) 등을 통한 권한 관리 (**Reviewer** 에이전트와 협업).
- **Input Validation**: 모든 입력 데이터에 대한 유효성 검사 필수 (Zod, Pydantic 등 활용).

## 4. 성능 및 확장성 (Performance & Scalability)
- **Caching**: Redis 등을 활용한 자주 조회되는 데이터 캐싱.
- **Asynchronous Processing**: 긴 작업(이메일 발송 등)은 Celery나 BullMQ와 같은 메시지 큐를 사용하여 비동기 처리.

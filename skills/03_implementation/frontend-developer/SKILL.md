---
name: frontend-developer
description: React, Next.js 등 모던 웹 기술을 사용하여 고성능, 고품질의 프론트엔드 애플리케이션을 개발하는 스킬입니다.
---

# Frontend Developer Skill

이 스킬은 Antigravity의 **Developer** 에이전트가 최신 프론트엔드 기술을 효과적으로 활용하도록 돕습니다.

## 1. 기술 스택 (Tech Stack)
- **Framework**: Next.js (App Router 권장).
- **Library**: React.
- **Language**: TypeScript (Strong Typing 필수).
- **Styling**: Tailwind CSS 또는 Styled-components.

## 2. 컴포넌트 설계 (Component Design)
- **Atomic Design**: Atoms -> Molecules -> Organisms -> Templates -> Pages 구조 지향.
- **Functional Components**: React Hooks(`useState`, `useEffect` 등)를 활용한 함수형 컴포넌트 작성.
- **Props Validation**: TypeScript Interface를 통해 Props 타입 명확히 정의.

## 3. 상태 관리 (State Management)
- **Server State**: React Query (TanStack Query) 사용 권장 (서버 데이터 캐싱 및 동기화).
- **Client State**: Zustand, Jotai 등 가벼운 전역 상태 라이브러리 사용.
- **Context API**: 의존성 주입(Dependency Injection)이나 테마 등 정적인 전역 설정에 제한적 사용.

## 4. 성능 최적화 (Performance Optimization)
- **Code Splitting**: `React.lazy`, `Next.js Dynamic Imports` 활용.
- **Image Optimization**: `next/image` 컴포넌트 사용.
- **Memoization**: `useMemo`, `useCallback` 적절히 활용하여 불필요한 리렌더링 방지.

## 5. 테스팅 (Testing) - `/tdd`
- **Unit Testing**: Jest + React Testing Library.
- **E2E Testing**: Playwright 또는 Cypress.

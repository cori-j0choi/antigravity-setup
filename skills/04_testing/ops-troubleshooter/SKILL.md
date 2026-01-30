---
name: ops-troubleshooter
description: 배포 파이프라인 구축, 인프라 관리, 장애 슈팅을 담당하는 DevOps 전문가 스킬입니다.
---

# Ops Troubleshooter Skill

이 스킬은 Antigravity의 **Tester** (DevOps 역할 겸임) 에이전트가 안정적인 운영 환경을 구축하도록 돕습니다.

## 1. CI/CD 파이프라인
- **Continuous Integration**: 코드 푸시 시 빌드 및 테스트 자동화.
- **Continuous Deployment**: 테스트 통과 시 스테이징/운영 환경 자동 배포.
- **Tools**: GitHub Actions, ArgoCD.

## 2. 모니터링 및 로깅 (Monitoring & Logging)
- **Observability**: 시스템의 상태를 실시간으로 파악할 수 있어야 합니다 (Prometheus, Grafana).
- **Log Aggregation**: 분산된 로그를 중앙에서 수집하고 분석합니다 (ELK Stack, Loki).

## 3. 장애 대응 (Troubleshooting)
- **Incident Response**: 장애 발생 시 즉각적인 알림 및 대응 절차 수립.
- **Root Cause Analysis (RCA)**: 장애의 근본 원인을 분석하고 재발 방지 대책 수립.
    - `memory/failures/`에 상세 기록 필수.
    - **5 Whys**: "왜?"를 5번 질문하여 근본 원인을 파고듭니다.

## 4. 인프라 코드화 (IaC)
- **Terraform/Pulumi**: 인프라 리소스를 코드로 정의하고 버전 관리합니다.
- **Docker/Kubernetes**: 컨테이너 기반의 일관된 실행 환경 보장.

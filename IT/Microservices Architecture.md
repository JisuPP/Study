# Microservices Architecture

애플리케이션을 작고 독립적인 서비스 단위로 나누어 설계하고 개발하는 소프투웨어 아키텍쳐 스타일

---

### 특징
1. 독립성
    - 각 서비스 독립적으로 배포, 실행 가능
    - 서비스 간 결합도가 낮아서 서비스 하나 수정 시 전체 시스템에 영향을 주지는 않음
2. 특정 비즈니스 기능 중심
    - 각 서비스는 특정 비즈니스 도메인을 중심으로 설계
3. 개별 데이터 저장소
    - 각 서비스는 각각의 데이터베이스를 가질 수 있음
    - 데이터 독립성이 보장됨
4. 다양한 기술 스택 사용 가능
    - 서로 다른 프로그래밍 언어나 데이터베이스를 사용 가능
5. 분산 시스템
    - 서비스 간 통신은 HTTP API, 메시지 큐, gRPC 등 분산 시스템 기술로 구성
6. 자동화된 배포
    - CI/CD 파이프라인을 통해 각 서비스를 자동으로 빌드, 테스트 배포 가능

### 장점
1. 개발 속도 증가
    - 독립적 서비스를 개발, 배포하여 병렬 작업 가능
2. 유지 보수 용이
    - 특정 서비스에 문제가 발생하더라도 다른 서비스에 영향 없음
    - 문제가 발생한 서비스만 수정 가능
3. 확장성
    - 각 서비스 별로 독립적 확장 가능
4. 기술 유연성
    - 각 서비스에 적합한 기술 스택을 선택하여 개발 가능
5. 장애 격려
    - 특정 서비스가 실패하더라도 다른 서비스는 정상적으로 동작

### 단점
1. 복잡성 증가
    - 여러 서비스 간의 통신, 데이터 일관성, 배포 관리 등 분산 시스템의 복잡성 증가
2. 네트워크 비용
    - 서비스 간 통신이 네트워크를 통해 이루어져 레이턴시와 네트워크 비용 증가
3. 테스트 어려움
    - 여러 서비스의 상호작용으로 인해 통합 테스트 어려움
4. 운영 비용 증가
    - 각 서비스마다 별도의 배포, 모니터링, 로깅 설정 필요
5. 데이터 관리 어려움
    - 분산 데이터베이스에서 데이터 일관성을 유지하는 것이 어려움
    - 추가적인 설계 필요

### 사용 사례
- Netflix
- Amazon
- Uber

### 구현 주요 기술
1. 컨테이너 및 오케스트레이션
   - Docker
   - Kubernetes
2. 서비스 간 통신
   - REST API
   - gRPC
   - RabbitMQ
   - Kafka
3. API 게이트웨이
   - Ngix
   - Kong
   - AWS API Gateway
4. 모니터링 및 로깅
   - Prometheus
   - Grafana
   - Elasticsearch
   - Longstash
   - Kibana
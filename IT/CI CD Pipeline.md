# CI/CD Pipeline

연속 통합, 배포, 배포 준비 등의 과정을 자동화된 워크플로우로 연결한 것

---

### 구성 요소
1. 연속 통합(Continous Intergration)
    - 개발자가 코드 변경 사항을 공유 repository에 자주 병합하는관행
    - 병합된 코드가 자동으로 빌드 및 테스트가 되어서 코드의 안정성 확인 가틍
    - 코드 통합 시 충돌을 최소화 가능
    - 문제 조기 발견 가능
2. 연속 배포(Continuous Delivery)
    - CI의 다음 단계
    - 코드 변경 사항을 프로덕션 환경에 배포할 준비가 된 상태로 유지
    - 배포는 수동으로 승인
    - 배포 스포세스는 자동화
    - 변경 사항을 빠르게 배포할 수 있는 준비 상태를 항시 유지
3. 연속 배포(Continous Deployment)
    - Continous Delivery의 확장
    - 승인 없이 변경 사항을 자동으로 프로덕션 환경에 배포
    - 완전한 자동화를 통해 사용자가 변경 사항을 빠르게 이용가능 하게 함
    - 변경 사항을 즉시 사용자에게 제공 가능

### 단계
1. 코드 작성 및 버전 관리
    - 개발자가 코드를 작성하고 Git과 같은 버전 관리 시스템에 푸시
2. 자동 빌드
   - 새로운 코드 변경 사항 발생 시 파이프라인이 자동으로 코드 빌드
   - npm install
   - mvn package
3. 자동 테스트
    - 빌드된 코드가 다양항 수준의 테스트를 통과하는지 확인
    - pytest
    - JUnit
4. 배포 준비
    - 테스트를 통과한 코드는 배포 준비 상태 돌입
    - Continous Delivery에서 수동 승인 단게 추가 가능
5. 자동 배포
    - Continous Deplyment의 경우, 테스트를 통과한 코드는 프로덕션 환경에 자동으로 배포됨

### 장점
1. 빠른 피드백 루프
    - 문제를 즉시 감지하고 수정 가능
2. 높은 코드 품질
    - 모든 코드 변경 사항이 자동 테스트를 통과해야 함
    - 테스트로 인해 품질이 보장됨
3. 효율적인 배포
    - 자동화된 배포로 인해 배포 주기 단축
4. 팀 생산성 향상
    - 개발자가 통합 및 배포 프로세스에 소모되는 시간 감소 가능
    - 코드 작성에 집중 가능
5. 사용자 경험 향상
    - 변경 사항이 빠르게 배포
    - 사용자 요구 사항에 신속 대응 가능

### 주요 도구
1. CI 도구
    - Jenkins
    - Travis CI
    - Circle CI
    - GitHub Actions
    - GitLab CI/CD
2. CD 도구
    - ArgoCD
    - Spinnake
    - AWS CodePipeline
3. 빌드 및 테스트 도구
    - Maven
    - Gradle
    - npm
    - Selenium
    - JUnit
    - Pytest
4. 배포 및 인프라 관리
    - Docker
    - Kubernetes
    - Terraform
    - Ansible

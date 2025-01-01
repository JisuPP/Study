# Maven

Apache Software Foundation에서 개발한 프로젝트 관리 및 빌드 자동화 도구

---

### 특징
1. 프로젝트에서 필요한 외부 라이브러리 선언 시 중앙 리포지토리에서 해당 라이브러리 자동 다운로드
2. 프로젝트 디렉토리 구조와 라이프사이클을 표준화
3. 프로젝트 간 일관성 제공
4. 소스 코드 컴파일, 테스트 실행, 패키징, 배포 등 작업을 명령어 한 줄로 자동화 가능
5. 플러그인으로 확장 가능
6. 빌드 프로세스의 각 단계를 처리하는 다양한 플러그인 제공
7. 프로젝트 빌드의 전체 과정을 관리하는 빌드 라이프 사이클 제공
8. 하나의 설정 파일로 여러 모듈을 포함하는 멀티모듈 프로젝트 쉽게 관리 가능

### 구성 요소
1. POM
    - Project Object Model
    - 핵심 설정 파일
    - XML 형식의 `pom.xml` 파일에 프로젝트 정보와 의존성, 빌드 설정 등 포함
    - 주요 태그
```
<groupId> : 프로젝트 그룹 ID
<artifactId> : 프로젝트 이름
<version> : 현재 프로젝트 버전
<dependencies> : 필요 외부 라이브러리 정의
```
2. Repository
    - 의존성 라이브러리를 저장하고 관리하는 중앙 저장소를 제공
    - Local Repository : 사용자 로컬 시스템에 저장된 리포지토리
    - Central Repository : 기본으로 제공하는 공개 중앙 리포지토리
    - Remote Repository : 회사나 팀에서 운영하는 사용자 지정 리포지토리
3. Plugins
    - 기능 확장을 위해 사용

### 디렉토리 구조
```bash
project/
├── src/
│   ├── main/
│   │   ├── java/        # 애플리케이션 소스 코드
│   │   ├── resources/   # 리소스 파일 (예: 설정 파일)
│   ├── test/
│       ├── java/        # 테스트 코드
│       ├── resources/   # 테스트 리소스
├── target/              # 컴파일 결과물 (빌드 디렉토리)
├── pom.xml              # 프로젝트 설정 파일
```

### 빌드 라이프사이클
1. Default Lifecycle
    - 프로젝트 빌드 시 사용
    - `validate` : 프로젝트가 올바르게 구성되었는지 확인
    - `complie` : 소스 코드 컴파일
    - `test` : 단위 테스트 실행
    - `package` : 배포 파일 생성
    - `verify` : 테스트 결과 검증
    - `install` : 빌드 아티팩트를 로컬 리포지토리에 저장
    - `deploy` : 원격 리포지토리에 배포
2. Clen Lifecycle
    - 이전 빌드 결과물을 정리
3. Site Lifecycle
    - 프로젝트 문서 생성

### 의존성 관리
- `pom.xml`에 의존성 선언 시 해당 라이브러리를 중앙 리포지토리에서 자동으로 다운로드

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-core</artifactId>
        <version>5.3.10</version>
    </dependency>
</dependencies>
```

### 종속성 범위
- `compile` : 컴파일, 테스트, 런타임 시 사용
- `provided` : 런타임에 지공되는 라이브러리
- `runtime` : 런타임에서만 필요한 라이브러리
- `test` : 테스트 시에만 필요한 라이브러리

### 명령어
1. 빌드
    - `mvn compile` : 소스 코드 컴파일
    - `mvn package` : JAR/WAR 파일 생성
    - `mvn clean` : 빌드 디렉토리 정리
2. 테스트 
    - `mvn test` : 단위 테스트 실행
3. 의존성 관리
    - `mvn dependency:resolve` : 의존성 확인 및 다운로드
    - `mvn dependency:tree` : 의존성 트리 시각화
4. 배포
    - `mvn install` : 로컬 리포지토리에 패키지 설치
    - `mvn deploy` : 원격 리포지토리에 배포

### 장점
1. 의존성을 자동으로 관리해 개발 시간 절약
2. 일관된 디렉토리 구조와 빌드 프로세스 제공
3. 플러그인을 통해 다양한 기능 확장 가능
4. 멀티모듈 프로젝트 관리 쉬움
5. 광범위한 커뮤니티

### 단점
1. 작은 프로젝트에서는 설정 과도
2. 대규모 프로젝트에서 빌드 시간 오래 걸림
3. 동일한 의존성이 여러버전이 포함되는 경우 충돌 문제 발생 가능
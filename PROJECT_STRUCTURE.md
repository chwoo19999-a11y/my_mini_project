# 📁 프로젝트 구조

```
my_mini_project/
│
├── backend/                          # Django REST Framework 백엔드
│   ├── config/                       # Django 프로젝트 설정
│   │   ├── __init__.py
│   │   ├── settings.py              # Django 설정 (DB, 앱, JWT, CORS 등)
│   │   ├── urls.py                  # 메인 URL 라우팅
│   │   ├── wsgi.py                  # WSGI 설정
│   │   └── asgi.py                  # ASGI 설정
│   │
│   ├── accounts/                     # 사용자 인증 앱
│   │   ├── migrations/              # DB 마이그레이션
│   │   ├── __init__.py
│   │   ├── admin.py                 # Admin 패널 설정
│   │   ├── apps.py                  # 앱 설정
│   │   ├── models.py                # User 모델 (프로필 이미지, bio)
│   │   ├── serializers.py           # JWT, 회원가입, 프로필 Serializer
│   │   ├── views.py                 # 로그인, 회원가입, 프로필 View
│   │   ├── urls.py                  # 인증 관련 URL
│   │   └── tests.py                 # 테스트
│   │
│   ├── destinations/                 # 여행지 관리 앱
│   │   ├── migrations/              # DB 마이그레이션
│   │   ├── management/              # Django 커스텀 명령어
│   │   │   └── commands/
│   │   │       └── init_destinations.py  # 초기 데이터 생성 스크립트
│   │   ├── __init__.py
│   │   ├── admin.py                 # 여행지/지역 Admin
│   │   ├── apps.py                  # 앱 설정
│   │   ├── models.py                # Destination, Region 모델
│   │   ├── serializers.py           # 여행지 Serializer
│   │   ├── views.py                 # 여행지 ViewSet
│   │   ├── urls.py                  # 여행지 URL
│   │   └── tests.py                 # 테스트
│   │
│   ├── social/                       # 소셜 기능 앱 (좋아요, 댓글)
│   │   ├── migrations/              # DB 마이그레이션
│   │   ├── __init__.py
│   │   ├── admin.py                 # 좋아요/댓글 Admin
│   │   ├── apps.py                  # 앱 설정 (Signal 등록)
│   │   ├── models.py                # Like, Comment 모델
│   │   ├── serializers.py           # 좋아요/댓글 Serializer
│   │   ├── views.py                 # 좋아요/댓글 ViewSet
│   │   ├── urls.py                  # 소셜 기능 URL
│   │   ├── signals.py               # 좋아요/댓글 수 자동 업데이트
│   │   └── tests.py                 # 테스트
│   │
│   ├── media/                        # 업로드된 미디어 파일
│   │   └── .gitkeep
│   ├── staticfiles/                  # 정적 파일 (수집됨)
│   │   └── .gitkeep
│   │
│   ├── manage.py                     # Django 관리 명령어
│   ├── requirements.txt              # Python 패키지 목록
│   ├── pytest.ini                    # Pytest 설정
│   ├── .env                          # 환경 변수 (secret)
│   ├── .env.example                  # 환경 변수 예시
│   └── README.md                     # 백엔드 문서
│
├── frontend/                         # React 프론트엔드
│   ├── public/                       # 정적 파일
│   │   └── index.html               # HTML 템플릿
│   │
│   ├── src/                          # 소스 코드
│   │   ├── components/              # 재사용 가능한 컴포넌트
│   │   │   ├── Navbar.js            # 내비게이션 바
│   │   │   └── Navbar.css
│   │   │
│   │   ├── pages/                   # 페이지 컴포넌트
│   │   │   ├── Home.js              # 홈 페이지
│   │   │   ├── Home.css
│   │   │   ├── Login.js             # 로그인 페이지
│   │   │   ├── Login.css
│   │   │   ├── Register.js          # 회원가입 페이지
│   │   │   ├── Register.css
│   │   │   ├── Profile.js           # 프로필 페이지
│   │   │   ├── Profile.css
│   │   │   ├── DestinationDetail.js # 여행지 상세 페이지
│   │   │   ├── DestinationDetail.css
│   │   │   ├── RegionDestinations.js # 지역별 여행지
│   │   │   └── RegionDestinations.css
│   │   │
│   │   ├── services/                # API 서비스 레이어
│   │   │   └── api.js               # Axios 설정, API 함수들
│   │   │
│   │   ├── context/                 # Context API
│   │   │   └── AuthContext.js       # 인증 상태 관리
│   │   │
│   │   ├── App.js                   # 메인 앱 컴포넌트
│   │   ├── App.css                  # 앱 스타일
│   │   ├── index.js                 # 엔트리 포인트
│   │   └── index.css                # 글로벌 스타일
│   │
│   ├── package.json                  # Node 패키지 설정
│   ├── .gitignore                    # Git 무시 파일
│   ├── .env.example                  # 환경 변수 예시
│   └── README.md                     # 프론트엔드 문서
│
├── .gitignore                        # 프로젝트 전체 Git 무시 파일
├── README.md                         # 프로젝트 메인 문서
├── START_HERE.md                     # 빠른 시작 가이드
├── PROJECT_STRUCTURE.md              # 이 파일
└── SKILL.md                          # DRF 개발 프로세스 가이드

```

## 🔑 주요 파일 설명

### Backend

#### config/settings.py
- Django 프로젝트 설정
- 앱 등록 (accounts, destinations, social)
- REST Framework 설정 (JWT, Pagination, Filters)
- CORS 설정
- Swagger (drf-spectacular) 설정

#### accounts/models.py
- **User**: 커스텀 사용자 모델
  - AbstractUser 상속
  - profile_image, bio 필드 추가

#### destinations/models.py
- **Region**: 지역 (북인도/남인도)
- **Destination**: 여행지
  - name, description, image, address
  - latitude, longitude (위치)
  - likes_count, comments_count, view_count (통계)

#### social/models.py
- **Like**: 좋아요 (User ↔ Destination)
  - unique_together: user, destination
- **Comment**: 댓글
  - 대댓글 지원 (parent 필드)
  - 1단계까지만 허용

#### social/signals.py
- Like 생성/삭제 시 Destination의 likes_count 자동 업데이트
- Comment 생성/삭제 시 Destination의 comments_count 자동 업데이트

### Frontend

#### src/services/api.js
- Axios 인스턴스 생성
- JWT 토큰 자동 추가 (Interceptor)
- 토큰 갱신 자동 처리
- API 함수들:
  - authAPI: 회원가입, 로그인, 프로필
  - destinationAPI: 여행지 목록, 상세, 인기, 추천
  - likeAPI: 좋아요 토글
  - commentAPI: 댓글 CRUD

#### src/context/AuthContext.js
- 인증 상태 전역 관리
- login, register, logout 함수
- localStorage에 토큰 및 사용자 정보 저장

#### src/pages/
- **Home**: 인기 여행지, 전체 여행지 목록
- **Login/Register**: JWT 인증
- **Profile**: 프로필 조회/수정, 이미지 업로드
- **DestinationDetail**: 여행지 상세, 좋아요, 댓글
- **RegionDestinations**: 북인도/남인도 필터링

## 📊 데이터 흐름

### 로그인 흐름
1. User가 Login 페이지에서 username/password 입력
2. AuthContext의 login() 함수 호출
3. api.js의 authAPI.login() → POST /api/auth/login/
4. Backend에서 JWT 토큰 발급
5. Frontend에서 localStorage에 저장
6. axios interceptor가 모든 요청에 토큰 자동 추가

### 좋아요 흐름
1. User가 여행지 상세 페이지에서 ❤️ 버튼 클릭
2. likeAPI.toggle(destinationId) 호출
3. Backend의 LikeViewSet.toggle() 실행
4. Like 생성/삭제
5. Signal이 Destination.likes_count 자동 업데이트
6. Frontend에서 즉시 UI 업데이트

### 댓글 흐름
1. User가 댓글 입력 후 제출
2. commentAPI.createComment() 호출
3. Backend의 CommentViewSet.create() 실행
4. Comment 생성
5. Signal이 Destination.comments_count 자동 업데이트
6. Frontend에서 댓글 목록 새로고침

## 🎯 핵심 기술

### Backend
- **JWT 인증**: Access Token (60분) + Refresh Token (1일)
- **Signal**: 좋아요/댓글 수 자동 업데이트
- **drf-spectacular**: Swagger UI 자동 생성
- **Validation**: Model → Serializer → View 3단계 검증

### Frontend
- **Context API**: 전역 상태 관리
- **Axios Interceptor**: 토큰 자동 관리 및 갱신
- **React Router**: 클라이언트 사이드 라우팅
- **반응형 CSS**: 모바일/태블릿/데스크톱 대응

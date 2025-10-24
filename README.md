# 🕌 India Travel Guide - 인도 여행 가이드

파이썬 부트캠프 미니 프로젝트
**Backend**: Django REST Framework
**Frontend**: React

## 📌 프로젝트 소개

인도의 아름다운 여행지를 소개하는 웹 애플리케이션입니다. 북인도와 남인도의 주요 관광지 정보를 제공하며, 사용자들이 여행지에 좋아요를 누르고 댓글을 남길 수 있습니다.

### 주요 기능

- 🏛️ **북인도/남인도 여행지 카테고리**
  - 타지마할, 델리, 자이푸르 등 북인도 명소
  - 마이소르 궁전, 케랄라, 고아 등 남인도 명소

- 👤 **사용자 인증**
  - 회원가입 / 로그인 (JWT 인증)
  - 프로필 관리 (프로필 이미지, 자기소개)

- ❤️ **소셜 기능**
  - 여행지 좋아요 / 좋아요 취소
  - 댓글 작성, 수정, 삭제
  - 대댓글 지원

- 🔍 **검색 및 필터링**
  - 여행지 검색
  - 지역별 필터링 (북인도/남인도)
  - 인기순/최신순 정렬

## 🛠️ 기술 스택

### Backend
- **Django 5.0.1** - Python 웹 프레임워크
- **Django REST Framework 3.14.0** - RESTful API
- **djangorestframework-simplejwt 5.3.1** - JWT 인증
- **drf-spectacular 0.27.1** - API 문서화 (Swagger UI)
- **django-cors-headers 4.3.1** - CORS 처리
- **django-filter 23.5** - 필터링
- **Pillow 10.2.0** - 이미지 처리
- **SQLite** (개발) / **PostgreSQL** (프로덕션)

### Frontend
- **React 18.2.0** - JavaScript 라이브러리
- **React Router DOM 6.20.0** - 라우팅
- **Axios 1.6.2** - HTTP 클라이언트
- **CSS3** - 스타일링 (반응형 디자인)

## 📁 프로젝트 구조

```
my_mini_project/
├── backend/                # Django 백엔드
│   ├── config/            # Django 설정
│   ├── accounts/          # 사용자 인증 앱
│   ├── destinations/      # 여행지 관리 앱
│   ├── social/            # 좋아요, 댓글 앱
│   ├── manage.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/              # React 프론트엔드
│   ├── public/
│   ├── src/
│   │   ├── components/   # 재사용 컴포넌트
│   │   ├── pages/        # 페이지 컴포넌트
│   │   ├── services/     # API 서비스
│   │   ├── context/      # Context API
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
│
└── README.md
```

## 🚀 설치 및 실행 방법

### 1️⃣ 프로젝트 클론

```bash
git clone <repository-url>
cd my_mini_project
```

### 2️⃣ 백엔드 설정

```bash
# backend 폴더로 이동
cd backend

# 가상환경 활성화 (conda)
conda activate bookmark

# 패키지 설치
pip install -r requirements.txt

# 환경 변수 설정
cp .env.example .env
# .env 파일을 열어서 SECRET_KEY 등을 설정하세요

# 데이터베이스 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 슈퍼유저 생성
python manage.py createsuperuser

# 초기 여행지 데이터 생성
python manage.py init_destinations

# 서버 실행
python manage.py runserver
```

백엔드 서버: http://localhost:8000
Swagger UI: http://localhost:8000/api/schema/swagger-ui/
Admin 페이지: http://localhost:8000/admin/

### 3️⃣ 프론트엔드 설정

```bash
# frontend 폴더로 이동 (새 터미널)
cd frontend

# 패키지 설치
npm install

# 개발 서버 실행
npm start
```

프론트엔드 서버: http://localhost:3000

## 📊 API 엔드포인트

### 인증 (Authentication)
- `POST /api/auth/register/` - 회원가입
- `POST /api/auth/login/` - 로그인 (JWT 토큰 발급)
- `POST /api/auth/token/refresh/` - 토큰 갱신
- `GET /api/auth/profile/` - 프로필 조회
- `PATCH /api/auth/profile/` - 프로필 수정
- `POST /api/auth/password/change/` - 비밀번호 변경

### 여행지 (Destinations)
- `GET /api/destinations/` - 여행지 목록
- `GET /api/destinations/{id}/` - 여행지 상세
- `GET /api/destinations/popular/` - 인기 여행지 Top 10
- `GET /api/destinations/recommended/` - 추천 여행지 Top 10

### 지역 (Regions)
- `GET /api/regions/` - 지역 목록 (북인도/남인도)
- `GET /api/regions/{id}/` - 지역 상세

### 좋아요 (Likes)
- `GET /api/likes/` - 내 좋아요 목록
- `POST /api/likes/toggle/` - 좋아요 토글

### 댓글 (Comments)
- `GET /api/comments/?destination={id}` - 댓글 목록
- `POST /api/comments/` - 댓글 작성
- `PATCH /api/comments/{id}/` - 댓글 수정
- `DELETE /api/comments/{id}/` - 댓글 삭제

## 📸 주요 화면

### 홈 페이지
- 인기 여행지 및 전체 여행지 목록
- 북인도/남인도 빠른 접근 버튼

### 여행지 상세 페이지
- 여행지 정보 (이름, 설명, 위치, 이미지)
- 좋아요 기능
- 댓글 작성 및 대댓글 기능

### 로그인/회원가입
- JWT 기반 인증
- 폼 유효성 검사

### 프로필 페이지
- 사용자 정보 표시 및 수정
- 프로필 이미지 업로드

## 🌍 여행지 데이터

### 북인도 (North India)
1. **타지마할** (Taj Mahal) - 아그라
2. **델리** (Delhi) - 인도의 수도
3. **자이푸르** (Jaipur) - 핑크시티
4. **바라나시** (Varanasi) - 영혼의 도시
5. **아그라 포트** (Agra Fort) - 붉은 요새
6. **우다이푸르** (Udaipur) - 화이트 시티

### 남인도 (South India)
1. **마이소르 궁전** (Mysore Palace) - 카르나타카
2. **케랄라 알레피** (Alleppey Kerala) - 백워터
3. **첸나이** (Chennai) - 남인도 최대 도시
4. **고아** (Goa) - 해변 휴양지
5. **함피** (Hampi) - 고대 유적지
6. **마하발리푸람** (Mahabalipuram) - 해안 사원

## 🔑 주요 기능 상세

### JWT 인증
- Access Token (60분)
- Refresh Token (1일)
- 자동 토큰 갱신 (Axios Interceptor)

### 좋아요 시스템
- 좋아요/좋아요 취소 토글 기능
- 실시간 좋아요 수 업데이트
- 로그인한 사용자만 가능

### 댓글 시스템
- 댓글 작성, 수정, 삭제
- 대댓글 지원 (1단계까지)
- 본인 댓글만 수정/삭제 가능

### 이미지 업로드
- 프로필 이미지 업로드
- 여행지 이미지 (관리자)
- 파일 크기 및 확장자 검증

## 🧪 테스트

### Swagger UI로 API 테스트
http://localhost:8000/api/schema/swagger-ui/ 에서 모든 API를 테스트할 수 있습니다.

### 테스트 계정
관리자 계정을 생성하여 테스트하세요:
```bash
python manage.py createsuperuser
```

## 📝 체크리스트

- [x] GitHub 저장소 생성 및 클론
- [x] backend, frontend 폴더 구조 생성
- [x] 서비스 주제 선정 (인도 여행지 추천)
- [x] BE API 개발 (DRF)
  - [x] User 모델 및 JWT 인증
  - [x] Destination 모델 (여행지)
  - [x] Region 모델 (지역)
  - [x] Like 모델 (좋아요)
  - [x] Comment 모델 (댓글)
  - [x] Serializers
  - [x] ViewSets
  - [x] API 문서화 (Swagger)
- [x] FE 화면 개발 (React)
  - [x] 라우팅 설정
  - [x] 인증 Context
  - [x] 홈 페이지
  - [x] 로그인/회원가입
  - [x] 프로필 페이지
  - [x] 여행지 상세 페이지
  - [x] 지역별 여행지 목록
- [x] README.md 작성
- [ ] GitHub에 푸시
- [ ] 디스코드 스레드에 제출

## 🎨 디자인

- **색상 테마**: 보라색-핑크 그라데이션
- **반응형 디자인**: 모바일, 태블릿, 데스크톱 지원
- **현대적인 UI**: 카드 레이아웃, 부드러운 애니메이션

## 📚 참고 자료

- [Django 공식 문서](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [React 공식 문서](https://react.dev/)
- [drf-spectacular 문서](https://drf-spectacular.readthedocs.io/)

## 👨‍💻 개발자

우창호 (Python 부트캠프)

## 📄 라이선스

이 프로젝트는 교육 목적으로 제작되었습니다.

---

**Made with ❤️ for India Travel Enthusiasts**

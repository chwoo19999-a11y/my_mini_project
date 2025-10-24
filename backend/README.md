# India Travel Guide - Backend

Django REST Framework 기반 인도 여행 가이드 백엔드 API입니다.

## 기술 스택

- Django 5.0.1
- Django REST Framework 3.14.0
- JWT 인증 (djangorestframework-simplejwt 5.3.1)
- drf-spectacular 0.27.1 (Swagger UI)
- SQLite (개발) / PostgreSQL (프로덕션)

## 시작하기

### 1. 가상환경 활성화

```bash
conda activate bookmark
```

### 2. 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정

`.env` 파일을 생성하거나 `.env.example`을 복사하세요:

```bash
cp .env.example .env
```

### 4. 데이터베이스 마이그레이션

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. 슈퍼유저 생성

```bash
python manage.py createsuperuser
```

### 6. 초기 데이터 생성

```bash
python manage.py init_destinations
```

이 명령어는 12개의 인도 여행지 데이터를 자동으로 생성합니다 (북인도 6곳, 남인도 6곳).

### 7. 개발 서버 실행

```bash
python manage.py runserver
```

## 주요 URL

- **API 서버**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/api/schema/swagger-ui/
- **Admin 페이지**: http://localhost:8000/admin/

## API 엔드포인트

### 인증
- `POST /api/auth/register/` - 회원가입
- `POST /api/auth/login/` - 로그인
- `POST /api/auth/token/refresh/` - 토큰 갱신
- `GET /api/auth/profile/` - 프로필 조회
- `PATCH /api/auth/profile/` - 프로필 수정

### 여행지
- `GET /api/destinations/` - 여행지 목록
- `GET /api/destinations/{id}/` - 여행지 상세
- `GET /api/destinations/popular/` - 인기 여행지
- `GET /api/destinations/recommended/` - 추천 여행지

### 지역
- `GET /api/regions/` - 지역 목록

### 좋아요
- `POST /api/likes/toggle/` - 좋아요 토글
- `GET /api/likes/` - 내 좋아요 목록

### 댓글
- `GET /api/comments/?destination={id}` - 댓글 목록
- `POST /api/comments/` - 댓글 작성
- `PATCH /api/comments/{id}/` - 댓글 수정
- `DELETE /api/comments/{id}/` - 댓글 삭제

## 앱 구조

- **accounts**: 사용자 인증 및 프로필 관리
- **destinations**: 여행지 및 지역 관리
- **social**: 좋아요 및 댓글 기능

## 테스트

```bash
pytest
```

## 모델 구조

### User (accounts)
- 커스텀 사용자 모델
- 프로필 이미지, 자기소개

### Region (destinations)
- 북인도/남인도 카테고리

### Destination (destinations)
- 여행지 정보 (이름, 설명, 이미지, 위치)
- 통계 (좋아요 수, 댓글 수, 조회수)

### Like (social)
- 사용자-여행지 좋아요 관계

### Comment (social)
- 댓글 및 대댓글 (1단계)

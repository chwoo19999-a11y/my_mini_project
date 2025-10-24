# 🚀 빠른 시작 가이드

인도 여행 가이드 프로젝트를 빠르게 시작하는 방법입니다.

## 📋 사전 준비

- Python 3.8 이상
- Node.js 14 이상
- Conda (가상환경)

## 1️⃣ 백엔드 설정 및 실행

### 터미널 1 (Backend)

```bash
# 1. backend 폴더로 이동
cd backend

# 2. 가상환경 활성화
conda activate bookmark

# 3. 패키지 설치
pip install -r requirements.txt

# 4. 환경 변수 확인 (.env 파일이 있는지 확인)
# 없다면: cp .env.example .env

# 5. 데이터베이스 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 6. 슈퍼유저 생성 (선택사항)
python manage.py createsuperuser

# 7. 초기 여행지 데이터 생성 (12개 여행지)
python manage.py init_destinations

# 8. 개발 서버 실행
python manage.py runserver
```

✅ 백엔드가 실행되면:
- API 서버: http://localhost:8000
- Swagger UI: http://localhost:8000/api/schema/swagger-ui/
- Admin: http://localhost:8000/admin/

## 2️⃣ 프론트엔드 설정 및 실행

### 터미널 2 (Frontend) - 새 터미널 열기

```bash
# 1. frontend 폴더로 이동
cd frontend

# 2. 패키지 설치
npm install

# 3. 개발 서버 실행
npm start
```

✅ 프론트엔드가 실행되면:
- React 앱: http://localhost:3000

## 🎯 테스트해보기

1. **회원가입**: http://localhost:3000/register
2. **로그인**: http://localhost:3000/login
3. **여행지 둘러보기**: 홈페이지에서 여행지 카드 클릭
4. **좋아요 & 댓글**: 로그인 후 여행지 상세 페이지에서 테스트

## 🔧 문제 해결

### 백엔드 오류

**"No module named 'django'" 오류**
```bash
cd backend
pip install -r requirements.txt
```

**"table doesn't exist" 오류**
```bash
cd backend
python manage.py migrate
```

### 프론트엔드 오류

**"Cannot GET /" 오류**
```bash
cd frontend
npm install
npm start
```

**API 연결 안됨**
- 백엔드가 http://localhost:8000 에서 실행 중인지 확인
- 브라우저 콘솔에서 CORS 에러 확인

## 📊 초기 데이터

`python manage.py init_destinations` 명령어로 생성되는 데이터:

### 북인도 (6개)
1. 타지마할 - 아그라의 상징적인 대리석 묘
2. 델리 - 인도의 수도
3. 자이푸르 - 핑크시티
4. 바라나시 - 영혼의 도시
5. 아그라 포트 - 붉은 요새
6. 우다이푸르 - 화이트 시티

### 남인도 (6개)
1. 마이소르 궁전 - 화려한 궁전
2. 케랄라 알레피 - 백워터 투어
3. 첸나이 - 남인도 최대 도시
4. 고아 - 해변 휴양지
5. 함피 - 고대 유적지
6. 마하발리푸람 - 해안 사원

## 🎨 기능 체험

### 1. 회원가입 & 로그인
- 회원가입 후 로그인
- JWT 토큰 자동 관리

### 2. 여행지 탐색
- 홈페이지에서 인기 여행지 확인
- 북인도/남인도 카테고리 탐색

### 3. 여행지 상세
- 여행지 클릭하여 상세 정보 확인
- 좋아요 버튼 클릭 (로그인 필요)
- 댓글 작성 및 대댓글

### 4. 프로필 관리
- 프로필 이미지 업로드
- 자기소개 수정

## 📝 다음 단계

1. ✅ 프로젝트 실행 완료
2. 🧪 모든 기능 테스트
3. 📸 스크린샷 캡처
4. 💾 GitHub에 푸시
5. 📤 디스코드에 제출

## 💡 팁

- Swagger UI에서 API를 직접 테스트할 수 있습니다
- Admin 페널에서 데이터를 직접 관리할 수 있습니다
- 브라우저 개발자 도구로 API 호출을 확인할 수 있습니다

---

문제가 발생하면 README.md를 참고하세요!

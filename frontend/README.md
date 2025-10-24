# India Travel Guide - Frontend

React 기반 인도 여행 가이드 프론트엔드 애플리케이션입니다.

## 기술 스택

- React 18.2.0
- React Router DOM 6.20.0
- Axios 1.6.2
- CSS3 (반응형 디자인)

## 시작하기

### 설치

```bash
npm install
```

### 개발 서버 실행

```bash
npm start
```

http://localhost:3000 에서 앱이 실행됩니다.

### 빌드

```bash
npm run build
```

프로덕션용 빌드 파일이 `build` 폴더에 생성됩니다.

## 환경 변수

`.env` 파일을 생성하고 다음 변수를 설정하세요:

```
REACT_APP_API_URL=http://localhost:8000/api
```

## 주요 기능

- 🏠 홈 페이지 (인기 여행지, 전체 목록)
- 🔐 로그인/회원가입 (JWT 인증)
- 👤 프로필 관리
- 🗺️ 여행지 상세 정보
- ❤️ 좋아요 기능
- 💬 댓글 및 대댓글
- 🔍 지역별 필터링 (북인도/남인도)
- 📱 반응형 디자인

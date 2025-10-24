# 🎨 인도 여행 가이드 - 디자인 테마

## 색상 팔레트 (Indian Flag Inspired)

### 주요 색상

#### 🧡 사프란 (Saffron) - 용기와 희생
```css
Primary Orange: #FF6B35
Mid Orange: #F7931E
Golden Yellow: #FDB913
```
**사용처:**
- 주요 버튼 배경
- 타이틀 그라데이션
- 강조 포인트
- 여행지 배지

#### 💚 녹색 (Green) - 번영과 풍요
```css
Indian Green: #138808
Light Green: #4CAF50
```
**사용처:**
- 보조 버튼
- 성공 메시지
- 서브 헤더
- 보더 강조

#### ⚪ 흰색 (White) - 평화와 진실
```css
Pure White: #FFFFFF
Cream: #FFF8F0
Light Cream: #FFE8D6
```
**사용처:**
- 카드 배경
- 버튼 텍스트
- 컨테이너 배경

### 그라데이션 패턴

#### 1. 메인 그라데이션 (사프란 → 금색)
```css
background: linear-gradient(135deg, #FF6B35 0%, #F7931E 50%, #FDB913 100%);
```
**사용처:** Navbar, Hero, 주요 버튼

#### 2. 인도 국기 그라데이션
```css
background: linear-gradient(to right,
  #FF6B35 0%, #FF6B35 30%,
  white 30%, white 60%,
  #138808 60%, #138808 90%,
  white 90%
);
```
**사용처:** Region 배너, 특별 섹션

#### 3. 녹색 그라데이션
```css
background: linear-gradient(135deg, #138808 0%, #FF6B35 100%);
```
**사용처:** 회원가입, 보조 버튼

#### 4. 텍스트 그라데이션
```css
background: linear-gradient(135deg, #FF6B35, #F7931E);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
```
**사용처:** 페이지 타이틀, 강조 텍스트

## 타이포그래피

### 제목
- **H1**: 48px, Bold, 그라데이션 효과
- **H2**: 32px, Bold, 주황색 (#FF6B35)
- **H3**: 24px, Semi-bold, 녹색 (#138808)

### 본문
- **일반 텍스트**: 16px, #333
- **보조 텍스트**: 14px, #666

## 컴포넌트 스타일 가이드

### 버튼

#### Primary Button
```css
background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%);
color: white;
border: none;
border-radius: 8px;
padding: 14px 28px;
font-weight: 700;
text-transform: uppercase;
letter-spacing: 1px;
```

**Hover:**
```css
background: linear-gradient(135deg, #F7931E 0%, #FDB913 100%);
box-shadow: 0 8px 20px rgba(255, 107, 53, 0.4);
transform: translateY(-2px);
```

#### Secondary Button
```css
background: #138808;
color: white;
border: 3px solid white;
```

**Hover:**
```css
background: white;
color: #FF6B35;
border-color: #138808;
```

### 카드

```css
background: white;
border-radius: 12px;
box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
border: 2px solid transparent;
transition: all 0.3s;
```

**Hover:**
```css
transform: translateY(-5px);
box-shadow: 0 8px 25px rgba(255, 107, 53, 0.3);
border-color: #FDB913;
```

### 입력 필드

```css
border: 2px solid #e2e8f0;
border-radius: 8px;
padding: 12px 16px;
```

**Focus:**
```css
border-color: #FF6B35;
box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.1);
```

## 애니메이션

### 만다라 회전
```css
@keyframes mandala-rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

### 옴(Om) 펄스
```css
@keyframes om-pulse {
  0%, 100% { opacity: 0.05; transform: translate(-50%, -50%) scale(1); }
  50% { opacity: 0.08; transform: translate(-50%, -50%) scale(1.1); }
}
```

### 연꽃(Lotus) 블룸
```css
@keyframes lotus-bloom {
  0%, 100% {
    opacity: 0.05;
    transform: translate(-50%, -50%) scale(1) rotate(0deg);
  }
  50% {
    opacity: 0.08;
    transform: translate(-50%, -50%) scale(1.15) rotate(180deg);
  }
}
```

## 아이콘 & 이모지

### 페이지별 심볼
- **Navbar Logo**: 🕌 (Mosque)
- **로그인 배경**: 🕉️ (Om Symbol)
- **회원가입 배경**: 🪷 (Lotus Flower)
- **인기 여행지**: 🔥 (Fire)
- **좋아요**: ❤️ (Heart)
- **댓글**: 💬 (Speech Bubble)
- **조회수**: 👁️ (Eye)

## 배경 패턴

### 페이지 배경
```css
background: linear-gradient(to bottom, #FFF8F0 0%, #FFE8D6 100%);
background-attachment: fixed;
```

### 컨테이너 배경
```css
background: linear-gradient(135deg, #FF6B35 0%, #F7931E 50%, #FDB913 100%);
```

## 그림자 효과

### 카드 그림자
```css
box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
```

**Hover:**
```css
box-shadow: 0 8px 25px rgba(255, 107, 53, 0.3);
```

### 버튼 그림자
```css
box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
```

## 보더 스타일

### 강조 보더
```css
border: 3px solid #138808;
```

### 카드 보더
```css
border: 2px solid #FDB913;
```

## 반응형 브레이크포인트

- **Mobile**: max-width: 640px
- **Tablet**: max-width: 768px
- **Desktop**: 769px 이상

## 사용 예시

### 제목 스타일링
```css
.page-title {
  font-size: 48px;
  font-weight: bold;
  background: linear-gradient(135deg, #FF6B35, #F7931E);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

### 섹션 제목 언더라인
```css
.section-title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
  height: 4px;
  background: linear-gradient(90deg, #FF6B35, #F7931E, #FDB913);
  border-radius: 2px;
}
```

## 접근성

- 텍스트와 배경 간 충분한 대비 유지
- 중요한 정보는 색상만으로 전달하지 않기
- 포커스 상태 명확히 표시
- 모든 인터랙티브 요소 충분한 크기 (최소 44x44px)

---

**디자인 철학**: 인도의 전통적인 색상과 현대적인 UI/UX를 조화롭게 결합하여,
사용자에게 인도 여행의 생동감과 문화적 풍요로움을 시각적으로 전달합니다.

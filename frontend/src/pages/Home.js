import { Link } from 'react-router-dom';
import './Home.css';

function Home() {
  return (
    <div className="home-container">
      <header className="home-header">
        <h1>인도 여행 가이드</h1>
        <p className="subtitle">신비로운 인도의 아름다움을 발견하세요</p>
      </header>

      <div className="region-selection">
        <div className="region-card south-india">
          <div className="region-overlay">
            <h2>남인도</h2>
            <p>해변, 백워터, 고대 사원의 천국</p>
            <ul className="region-highlights">
              <li>케랄라의 백워터</li>
              <li>고아의 아름다운 해변</li>
              <li>타밀나두의 고대 사원</li>
              <li>카르나타카의 유적</li>
            </ul>
            <Link to="/south-india" className="explore-btn">
              남인도 탐험하기
            </Link>
          </div>
        </div>

        <div className="region-card north-india">
          <div className="region-overlay">
            <h2>북인도</h2>
            <p>역사, 문화, 히말라야의 장엄함</p>
            <ul className="region-highlights">
              <li>타지마할의 웅장함</li>
              <li>라자스탄의 궁전과 요새</li>
              <li>히말라야 산맥</li>
              <li>영적 성지 바라나시</li>
            </ul>
            <Link to="/north-india" className="explore-btn">
              북인도 탐험하기
            </Link>
          </div>
        </div>
      </div>

      <section className="about-section">
        <h2>왜 인도를 여행해야 할까요?</h2>
        <div className="about-grid">
          <div className="about-card">
            <h3>다양한 문화</h3>
            <p>수천 년의 역사와 다양한 문화가 공존하는 신비로운 나라</p>
          </div>
          <div className="about-card">
            <h3>놀라운 건축물</h3>
            <p>타지마할부터 고대 사원까지, 세계적인 건축 유산</p>
          </div>
          <div className="about-card">
            <h3>자연의 아름다움</h3>
            <p>히말라야부터 열대 해변까지, 다채로운 자연 경관</p>
          </div>
          <div className="about-card">
            <h3>맛있는 음식</h3>
            <p>향신료가 가득한 정통 인도 요리의 천국</p>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Home;

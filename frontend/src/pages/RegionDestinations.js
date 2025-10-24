import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { destinationAPI, regionAPI } from '../services/api';
import './RegionDestinations.css';

const RegionDestinations = () => {
  const { region: regionParam } = useParams();
  const navigate = useNavigate();

  const [destinations, setDestinations] = useState([]);
  const [region, setRegion] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');

  const categories = ['전체', '문화유적', '자연경관', '종교시설', '도시', '해변', '산악지대', '기타'];

  useEffect(() => {
    loadData();
  }, [regionParam]);

  const loadData = async () => {
    setLoading(true);
    setError('');

    try {
      // regionParam은 'north' 또는 'south'
      // 지역 정보 설정
      if (regionParam) {
        setRegion({
          name: regionParam === 'north' ? '북인도' : '남인도',
          description: regionParam === 'north'
            ? '타지마할, 델리, 자이푸르 등 역사적인 건축물과 문화유산이 풍부한 북인도'
            : '마이소르 궁전, 케랄라, 고아 등 아름다운 해변과 자연이 있는 남인도'
        });
      }

      // 여행지 로드
      const destResponse = await destinationAPI.getDestinations();
      const allDestinations = destResponse.data.results || destResponse.data;

      // 클라이언트 사이드에서 필터링 (region_name으로)
      const filtered = regionParam
        ? allDestinations.filter(dest => dest.region_name === (regionParam === 'north' ? '북인도' : '남인도'))
        : allDestinations;

      setDestinations(filtered);
    } catch (err) {
      console.error('Failed to load data:', err);
      setError('데이터를 불러오는데 실패했습니다.');
    } finally {
      setLoading(false);
    }
  };

  // 필터링된 여행지
  const filteredDestinations = destinations.filter(destination => {
    // 검색어 필터
    const matchesSearch = destination.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          destination.description.toLowerCase().includes(searchQuery.toLowerCase());

    // 카테고리 필터
    const matchesCategory = !selectedCategory || selectedCategory === '전체' ||
                           destination.category === selectedCategory;

    return matchesSearch && matchesCategory;
  });

  const handleCategoryChange = (category) => {
    setSelectedCategory(category === '전체' ? '' : category);
  };

  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner"></div>
        <p>로딩 중...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error-container">
        <div className="error-content">
          <i className="error-icon">⚠</i>
          <h2>{error}</h2>
          <button onClick={() => navigate('/')} className="back-button">
            홈으로 돌아가기
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="region-destinations-container">
      <div className="region-header">
        <button onClick={() => navigate('/')} className="back-btn">
          ← 뒤로가기
        </button>

        <div className="region-info">
          {region ? (
            <>
              <h1>{region.name}</h1>
              <p className="region-description">{region.description}</p>
            </>
          ) : (
            <h1>모든 여행지</h1>
          )}
        </div>
      </div>

      <div className="filters-section">
        <div className="search-bar">
          <input
            type="text"
            placeholder="여행지 검색..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
          <i className="search-icon">🔍</i>
        </div>

        <div className="category-filters">
          {categories.map((category) => (
            <button
              key={category}
              onClick={() => handleCategoryChange(category)}
              className={`category-btn ${
                (category === '전체' && !selectedCategory) ||
                category === selectedCategory
                  ? 'active'
                  : ''
              }`}
            >
              {category}
            </button>
          ))}
        </div>
      </div>

      <div className="results-info">
        <p>총 {filteredDestinations.length}개의 여행지</p>
      </div>

      {filteredDestinations.length === 0 ? (
        <div className="no-results">
          <i className="no-results-icon">📍</i>
          <h3>검색 결과가 없습니다</h3>
          <p>다른 검색어나 필터를 시도해보세요.</p>
        </div>
      ) : (
        <div className="destinations-grid">
          {filteredDestinations.map((destination) => (
            <Link
              key={destination.id}
              to={`/destinations/${destination.id}`}
              className="destination-card"
            >
              <div className="card-image">
                {destination.image ? (
                  <img src={destination.image} alt={destination.name} />
                ) : (
                  <div className="card-image-placeholder">
                    <span>이미지 없음</span>
                  </div>
                )}
                <div className="card-overlay">
                  <span className="view-detail">자세히 보기 →</span>
                </div>
              </div>

              <div className="card-content">
                <h3>{destination.name}</h3>
                <p className="card-description">
                  {destination.description.length > 100
                    ? destination.description.substring(0, 100) + '...'
                    : destination.description}
                </p>

                <div className="card-meta">
                  <span className="category-tag">{destination.category}</span>
                  <div className="card-stats">
                    <span className="likes">
                      ♡ {destination.likes_count}
                    </span>
                  </div>
                </div>
              </div>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
};

export default RegionDestinations;

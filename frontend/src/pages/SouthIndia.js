import { Link } from 'react-router-dom';
import { southIndiaData } from '../data/travelData';
import './RegionPage.css';

function SouthIndia() {
  return (
    <div className="region-page">
      <div className="region-header">
        <Link to="/" className="back-btn">Back to Home</Link>
        <h1>{southIndiaData.region}</h1>
        <p className="region-description">{southIndiaData.description}</p>
      </div>

      <div className="cities-container">
        {southIndiaData.cities.map((city) => (
          <div key={city.id} className="city-section">
            <h2 className="city-name">{city.name}</h2>

            <div className="attractions-grid">
              {city.attractions.map((attraction) => (
                <div key={attraction.id} className="attraction-card">
                  <div className="attraction-image">
                    <img
                      src={attraction.image}
                      alt={attraction.name}
                      onError={(e) => {
                        e.target.src = 'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=800';
                      }}
                    />
                  </div>
                  <div className="attraction-content">
                    <h3 className="attraction-name">{attraction.name}</h3>
                    <p className="attraction-description">{attraction.description}</p>
                    <div className="attraction-meta">
                      <span className="best-time">
                        <strong>Best Time:</strong> {attraction.bestTime}
                      </span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>

      <div className="region-footer">
        <Link to="/north-india" className="other-region-btn">
          Explore North India
        </Link>
      </div>
    </div>
  );
}

export default SouthIndia;

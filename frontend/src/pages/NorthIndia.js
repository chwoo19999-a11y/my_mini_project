import { Link } from 'react-router-dom';
import { northIndiaData } from '../data/travelData';
import './RegionPage.css';

function NorthIndia() {
  return (
    <div className="region-page">
      <div className="region-header">
        <Link to="/" className="back-btn">Back to Home</Link>
        <h1>{northIndiaData.region}</h1>
        <p className="region-description">{northIndiaData.description}</p>
      </div>

      <div className="cities-container">
        {northIndiaData.cities.map((city) => (
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
        <Link to="/south-india" className="other-region-btn">
          Explore South India
        </Link>
      </div>
    </div>
  );
}

export default NorthIndia;

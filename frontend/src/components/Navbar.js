import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './Navbar.css';

function Navbar() {
  const { user, logout, isAuthenticated } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          <span className="logo-icon">🕌</span>
          <span className="logo-text">India Travel Guide</span>
        </Link>

        <div className="navbar-menu">
          <Link to="/" className="navbar-link">홈</Link>
          <Link to="/regions/north" className="navbar-link">북인도</Link>
          <Link to="/regions/south" className="navbar-link">남인도</Link>

          {isAuthenticated ? (
            <>
              <Link to="/profile" className="navbar-link">프로필</Link>
              <button onClick={handleLogout} className="navbar-button logout">
                로그아웃
              </button>
            </>
          ) : (
            <>
              <Link to="/login" className="navbar-button login">
                로그인
              </Link>
              <Link to="/register" className="navbar-button register">
                회원가입
              </Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}

export default Navbar;

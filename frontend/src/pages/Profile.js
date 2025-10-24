import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { authAPI } from '../services/api';
import './Profile.css';

const Profile = () => {
  const { user, updateUser } = useAuth();
  const [isEditing, setIsEditing] = useState(false);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState({ type: '', text: '' });

  const [profileData, setProfileData] = useState({
    username: '',
    email: '',
    bio: '',
    profile_image: null
  });

  const [previewImage, setPreviewImage] = useState(null);

  useEffect(() => {
    loadProfile();
  }, []);

  const loadProfile = async () => {
    try {
      const response = await authAPI.getProfile();
      const data = response.data;
      setProfileData({
        username: data.username || '',
        email: data.email || '',
        bio: data.bio || '',
        profile_image: null
      });
      if (data.profile_image) {
        setPreviewImage(data.profile_image);
      }
    } catch (error) {
      console.error('Failed to load profile:', error);
      setMessage({ type: 'error', text: '프로필을 불러오는데 실패했습니다.' });
    }
  };

  const handleChange = (e) => {
    setProfileData({
      ...profileData,
      [e.target.name]: e.target.value
    });
  };

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      // 이미지 파일 유효성 검사
      if (!file.type.startsWith('image/')) {
        setMessage({ type: 'error', text: '이미지 파일만 업로드 가능합니다.' });
        return;
      }

      // 파일 크기 제한 (5MB)
      if (file.size > 5 * 1024 * 1024) {
        setMessage({ type: 'error', text: '이미지 크기는 5MB 이하여야 합니다.' });
        return;
      }

      setProfileData({
        ...profileData,
        profile_image: file
      });

      // 미리보기 생성
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreviewImage(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage({ type: '', text: '' });

    try {
      const updateData = {
        email: profileData.email,
        bio: profileData.bio
      };

      if (profileData.profile_image) {
        updateData.profile_image = profileData.profile_image;
      }

      const response = await authAPI.updateProfile(updateData);

      // AuthContext의 user 정보 업데이트
      updateUser(response.data);

      setMessage({ type: 'success', text: '프로필이 성공적으로 업데이트되었습니다.' });
      setIsEditing(false);

      // 프로필 다시 로드
      await loadProfile();
    } catch (error) {
      console.error('Failed to update profile:', error);
      const errorMsg = error.response?.data?.detail || '프로필 업데이트에 실패했습니다.';
      setMessage({ type: 'error', text: errorMsg });
    } finally {
      setLoading(false);
    }
  };

  const handleCancel = () => {
    setIsEditing(false);
    loadProfile();
    setMessage({ type: '', text: '' });
  };

  return (
    <div className="profile-container">
      <div className="profile-card">
        <div className="profile-header">
          <h1>내 프로필</h1>
          {!isEditing && (
            <button
              onClick={() => setIsEditing(true)}
              className="edit-button"
            >
              편집
            </button>
          )}
        </div>

        {message.text && (
          <div className={`message ${message.type}`}>
            <i className="message-icon">
              {message.type === 'success' ? '✓' : '⚠'}
            </i>
            <span>{message.text}</span>
          </div>
        )}

        <form onSubmit={handleSubmit} className="profile-form">
          <div className="profile-image-section">
            <div className="image-wrapper">
              {previewImage ? (
                <img
                  src={previewImage}
                  alt="Profile"
                  className="profile-image"
                />
              ) : (
                <div className="profile-image-placeholder">
                  <span>{profileData.username.charAt(0).toUpperCase()}</span>
                </div>
              )}
            </div>

            {isEditing && (
              <div className="image-upload">
                <label htmlFor="profile_image" className="upload-button">
                  이미지 변경
                </label>
                <input
                  type="file"
                  id="profile_image"
                  accept="image/*"
                  onChange={handleImageChange}
                  style={{ display: 'none' }}
                />
              </div>
            )}
          </div>

          <div className="form-group">
            <label>사용자명</label>
            <input
              type="text"
              name="username"
              value={profileData.username}
              disabled={true}
              className="disabled"
            />
            <span className="helper-text">사용자명은 변경할 수 없습니다</span>
          </div>

          <div className="form-group">
            <label htmlFor="email">이메일</label>
            <input
              type="email"
              id="email"
              name="email"
              value={profileData.email}
              onChange={handleChange}
              disabled={!isEditing}
              placeholder="이메일을 입력하세요"
            />
          </div>

          <div className="form-group">
            <label htmlFor="bio">자기소개</label>
            <textarea
              id="bio"
              name="bio"
              value={profileData.bio}
              onChange={handleChange}
              disabled={!isEditing}
              placeholder="자신을 소개해주세요"
              rows="4"
            />
          </div>

          {isEditing && (
            <div className="form-actions">
              <button
                type="button"
                onClick={handleCancel}
                className="cancel-button"
                disabled={loading}
              >
                취소
              </button>
              <button
                type="submit"
                className="save-button"
                disabled={loading}
              >
                {loading ? '저장 중...' : '저장'}
              </button>
            </div>
          )}
        </form>

        <div className="profile-stats">
          <div className="stat-item">
            <div className="stat-value">{user?.date_joined ? new Date(user.date_joined).toLocaleDateString() : '-'}</div>
            <div className="stat-label">가입일</div>
          </div>
          <div className="stat-item">
            <div className="stat-value">{user?.likes_count || 0}</div>
            <div className="stat-label">좋아요</div>
          </div>
          <div className="stat-item">
            <div className="stat-value">{user?.comments_count || 0}</div>
            <div className="stat-label">댓글</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;

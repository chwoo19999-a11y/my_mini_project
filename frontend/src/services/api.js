import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

// Axios 인스턴스 생성
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request Interceptor - 토큰 추가
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response Interceptor - 토큰 갱신
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // 401 에러이고 재시도가 아닌 경우
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const refreshToken = localStorage.getItem('refreshToken');
        if (refreshToken) {
          const response = await axios.post(`${API_BASE_URL}/auth/token/refresh/`, {
            refresh: refreshToken,
          });

          const { access } = response.data;
          localStorage.setItem('accessToken', access);

          originalRequest.headers.Authorization = `Bearer ${access}`;
          return api(originalRequest);
        }
      } catch (refreshError) {
        // Refresh 실패 시 로그아웃
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        localStorage.removeItem('user');
        window.location.href = '/login';
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);

// API 함수들
export const authAPI = {
  // 회원가입
  register: (userData) => api.post('/auth/register/', userData),

  // 로그인
  login: (credentials) => api.post('/auth/login/', credentials),

  // 프로필 조회
  getProfile: () => api.get('/auth/profile/'),

  // 프로필 수정
  updateProfile: (profileData) => {
    const formData = new FormData();
    Object.keys(profileData).forEach(key => {
      if (profileData[key] !== null && profileData[key] !== undefined) {
        formData.append(key, profileData[key]);
      }
    });
    return api.patch('/auth/profile/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
  },

  // 비밀번호 변경
  changePassword: (passwordData) => api.post('/auth/password/change/', passwordData),
};

export const destinationAPI = {
  // 여행지 목록
  getDestinations: (params) => api.get('/destinations/', { params }),

  // 여행지 상세
  getDestination: (id) => api.get(`/destinations/${id}/`),

  // 인기 여행지
  getPopular: () => api.get('/destinations/popular/'),

  // 추천 여행지
  getRecommended: () => api.get('/destinations/recommended/'),
};

export const regionAPI = {
  // 지역 목록
  getRegions: () => api.get('/regions/'),

  // 지역 상세
  getRegion: (id) => api.get(`/regions/${id}/`),
};

export const likeAPI = {
  // 좋아요 토글
  toggle: (destinationId) => api.post('/likes/toggle/', { destination: destinationId }),

  // 내 좋아요 목록
  getMyLikes: () => api.get('/likes/'),
};

export const commentAPI = {
  // 댓글 목록
  getComments: (destinationId) => api.get('/comments/', { params: { destination: destinationId } }),

  // 댓글 작성
  createComment: (commentData) => api.post('/comments/', commentData),

  // 댓글 수정
  updateComment: (id, content) => api.patch(`/comments/${id}/`, { content }),

  // 댓글 삭제
  deleteComment: (id) => api.delete(`/comments/${id}/`),
};

export default api;

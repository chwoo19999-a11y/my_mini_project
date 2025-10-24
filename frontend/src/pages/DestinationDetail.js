import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { destinationAPI, likeAPI, commentAPI } from '../services/api';
import { useAuth } from '../context/AuthContext';
import './DestinationDetail.css';

const DestinationDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { user, isAuthenticated } = useAuth();

  const [destination, setDestination] = useState(null);
  const [comments, setComments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const [newComment, setNewComment] = useState('');
  const [commentLoading, setCommentLoading] = useState(false);

  const [editingCommentId, setEditingCommentId] = useState(null);
  const [editingContent, setEditingContent] = useState('');

  const [isLiked, setIsLiked] = useState(false);
  const [likesCount, setLikesCount] = useState(0);
  const [likeLoading, setLikeLoading] = useState(false);

  useEffect(() => {
    loadDestinationData();
  }, [id]);

  const loadDestinationData = async () => {
    setLoading(true);
    setError('');

    try {
      // 여행지 상세 정보 로드
      const destResponse = await destinationAPI.getDestination(id);
      setDestination(destResponse.data);
      setIsLiked(destResponse.data.is_liked);
      setLikesCount(destResponse.data.likes_count);

      // 댓글 로드
      const commentsResponse = await commentAPI.getComments(id);
      setComments(commentsResponse.data);
    } catch (err) {
      console.error('Failed to load destination:', err);
      setError('여행지 정보를 불러오는데 실패했습니다.');
    } finally {
      setLoading(false);
    }
  };

  const handleLikeToggle = async () => {
    if (!isAuthenticated) {
      alert('로그인이 필요합니다.');
      navigate('/login');
      return;
    }

    setLikeLoading(true);

    try {
      await likeAPI.toggle(id);
      setIsLiked(!isLiked);
      setLikesCount(isLiked ? likesCount - 1 : likesCount + 1);
    } catch (err) {
      console.error('Failed to toggle like:', err);
      alert('좋아요 처리 중 오류가 발생했습니다.');
    } finally {
      setLikeLoading(false);
    }
  };

  const handleCommentSubmit = async (e) => {
    e.preventDefault();

    if (!isAuthenticated) {
      alert('로그인이 필요합니다.');
      navigate('/login');
      return;
    }

    if (!newComment.trim()) {
      alert('댓글 내용을 입력해주세요.');
      return;
    }

    setCommentLoading(true);

    try {
      const response = await commentAPI.createComment({
        destination: id,
        content: newComment
      });

      setComments([response.data, ...comments]);
      setNewComment('');
    } catch (err) {
      console.error('Failed to create comment:', err);
      alert('댓글 작성 중 오류가 발생했습니다.');
    } finally {
      setCommentLoading(false);
    }
  };

  const handleCommentEdit = async (commentId) => {
    if (!editingContent.trim()) {
      alert('댓글 내용을 입력해주세요.');
      return;
    }

    try {
      const response = await commentAPI.updateComment(commentId, editingContent);
      setComments(comments.map(comment =>
        comment.id === commentId ? response.data : comment
      ));
      setEditingCommentId(null);
      setEditingContent('');
    } catch (err) {
      console.error('Failed to update comment:', err);
      alert('댓글 수정 중 오류가 발생했습니다.');
    }
  };

  const handleCommentDelete = async (commentId) => {
    if (!window.confirm('댓글을 삭제하시겠습니까?')) {
      return;
    }

    try {
      await commentAPI.deleteComment(commentId);
      setComments(comments.filter(comment => comment.id !== commentId));
    } catch (err) {
      console.error('Failed to delete comment:', err);
      alert('댓글 삭제 중 오류가 발생했습니다.');
    }
  };

  const startEditComment = (comment) => {
    setEditingCommentId(comment.id);
    setEditingContent(comment.content);
  };

  const cancelEditComment = () => {
    setEditingCommentId(null);
    setEditingContent('');
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

  if (!destination) {
    return null;
  }

  return (
    <div className="destination-detail-container">
      <div className="destination-header">
        <button onClick={() => navigate(-1)} className="back-btn">
          ← 뒤로가기
        </button>
      </div>

      <div className="destination-content">
        <div className="destination-image-section">
          {destination.image ? (
            <img
              src={destination.image}
              alt={destination.name}
              className="destination-image"
            />
          ) : (
            <div className="destination-image-placeholder">
              <span>이미지 없음</span>
            </div>
          )}
        </div>

        <div className="destination-info">
          <div className="destination-header-info">
            <h1>{destination.name}</h1>
            <button
              onClick={handleLikeToggle}
              disabled={likeLoading}
              className={`like-button ${isLiked ? 'liked' : ''}`}
            >
              <span className="like-icon">{isLiked ? '❤' : '♡'}</span>
              <span>{likesCount}</span>
            </button>
          </div>

          <div className="destination-meta">
            <span className="region-badge">{destination.region_name}</span>
            <span className="category-badge">{destination.category}</span>
          </div>

          <div className="destination-description">
            <h2>소개</h2>
            <p>{destination.description}</p>
          </div>

          {destination.location && (
            <div className="destination-location">
              <h3>위치</h3>
              <p>{destination.location}</p>
            </div>
          )}

          {destination.best_season && (
            <div className="destination-season">
              <h3>최적 방문 시기</h3>
              <p>{destination.best_season}</p>
            </div>
          )}
        </div>
      </div>

      <div className="comments-section">
        <h2>댓글 ({comments.length})</h2>

        {isAuthenticated ? (
          <form onSubmit={handleCommentSubmit} className="comment-form">
            <textarea
              value={newComment}
              onChange={(e) => setNewComment(e.target.value)}
              placeholder="댓글을 입력하세요..."
              rows="3"
              disabled={commentLoading}
            />
            <button type="submit" disabled={commentLoading}>
              {commentLoading ? '작성 중...' : '댓글 작성'}
            </button>
          </form>
        ) : (
          <div className="login-prompt">
            <p>댓글을 작성하려면 로그인이 필요합니다.</p>
            <button onClick={() => navigate('/login')}>로그인</button>
          </div>
        )}

        <div className="comments-list">
          {comments.length === 0 ? (
            <p className="no-comments">첫 댓글을 작성해보세요!</p>
          ) : (
            comments.map((comment) => (
              <div key={comment.id} className="comment-item">
                <div className="comment-header">
                  <div className="comment-author">
                    <span className="author-name">{comment.user_username}</span>
                    <span className="comment-date">
                      {new Date(comment.created_at).toLocaleString()}
                    </span>
                  </div>

                  {user && user.username === comment.user_username && (
                    <div className="comment-actions">
                      {editingCommentId === comment.id ? (
                        <>
                          <button
                            onClick={() => handleCommentEdit(comment.id)}
                            className="save-btn"
                          >
                            저장
                          </button>
                          <button
                            onClick={cancelEditComment}
                            className="cancel-btn"
                          >
                            취소
                          </button>
                        </>
                      ) : (
                        <>
                          <button
                            onClick={() => startEditComment(comment)}
                            className="edit-btn"
                          >
                            수정
                          </button>
                          <button
                            onClick={() => handleCommentDelete(comment.id)}
                            className="delete-btn"
                          >
                            삭제
                          </button>
                        </>
                      )}
                    </div>
                  )}
                </div>

                <div className="comment-content">
                  {editingCommentId === comment.id ? (
                    <textarea
                      value={editingContent}
                      onChange={(e) => setEditingContent(e.target.value)}
                      rows="3"
                      className="edit-textarea"
                    />
                  ) : (
                    <p>{comment.content}</p>
                  )}
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};

export default DestinationDetail;

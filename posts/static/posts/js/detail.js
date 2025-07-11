// CSRF 토큰 가져오기 함수
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// 공유 버튼 함수
function copyUrl() {
    const currentUrl = window.location.href;
    navigator.clipboard.writeText(currentUrl)
    .then(() => {
        const copyBox = document.querySelector(".copy");
        copyBox.style.display = "block";
        setTimeout(() => {
            copyBox.style.display = "none";
        }, 1000);
    })
    .catch(err => {
        console.error('URL 복사 실패:', err);
        alert("URL 복사에 실패했습니다. 직접 복사해주세요.");
    });
}
window.copyUrl = copyUrl;  // HTML onclick에서 호출되도록 전역 등록

document.addEventListener("DOMContentLoaded", function () {
    // 스크랩 버튼 이벤트
    document.getElementById("scrap-button")?.addEventListener("click", function () {
        const postId = this.dataset.postId;
        const button = this;
        const textDiv = button.querySelector(".button_text");
        const scrappedImgSrc = button.dataset.scrappedImg;
        const unscrappedImgSrc = button.dataset.unscrappedImg;

        fetch(`/posts/${postId}/toggle_scrap/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return response.json();
        })
        .then(data => {
            const imgElement = button.querySelector(".img"); // 이미지 요소 선택
            if (data.scrapped) {
                textDiv.textContent = "스크랩 취소";
                imgElement.src = unscrappedImgSrc;
            } else {
                textDiv.textContent = "스크랩";
                imgElement.src = unscrappedImgSrc;
            }
        })
    });

    // 대댓글 기능 관련 코드 시작
    const clickableComments = document.querySelectorAll('.clickable-comment');
    const parentCommentIdInput = document.getElementById('parent_comment_id'); // 숨겨진 parent_comment_id input
    const commentTextArea = document.querySelector('.comment_content'); // 댓글 textarea
    const replyToInfoDiv = document.getElementById('reply-to-info'); // "누구에게 답글 작성 중" div
    const replyToTextSpan = document.getElementById('reply-to-text'); // 메시지 텍스트 span
    const cancelReplyModeButton = document.getElementById('cancel-reply-mode'); // 취소 버튼

    clickableComments.forEach(commentItem => {
        commentItem.addEventListener('click', function() {
            const commentId = this.dataset.commentId;
            const commentAuthor = this.dataset.commentAuthor;

            // 1. 숨겨진 parent_comment_id 필드에 값 설정
            parentCommentIdInput.value = commentId;

            // 2. 입력창 옆에 누구에게 답글 다는지 표시
            replyToTextSpan.textContent = `@${commentAuthor} 에게 답글 작성 중`;
            replyToInfoDiv.style.display = 'block';

            // 3. 댓글 textarea의 placeholder 변경
            commentTextArea.placeholder = `@${commentAuthor} 님에게 대댓글을 입력하세요.`;

            // 4. 입력창으로 스크롤 이동 및 포커스
            commentTextArea.focus();
            commentTextArea.scrollIntoView({ behavior: 'smooth', block: 'center' });
        });
    });

    // '취소' 버튼 클릭 시 대댓글 모드 해제
    if (cancelReplyModeButton) {
        cancelReplyModeButton.addEventListener('click', function() {
            parentCommentIdInput.value = '';
            replyToInfoDiv.style.display = 'none';
            replyToTextSpan.textContent = '';
            commentTextArea.placeholder = '댓글을 입력하세요.';
            commentTextArea.value = '';
        });
    }

    // 신고하기 팝업
    document.querySelector(".declatation_img")?.addEventListener("click", () => {
        document.querySelector(".warning").style.display = "flex"; // 중앙 정렬 위해 'flex' 사용
    });

    document.querySelector(".yes")?.addEventListener("click", () => {
        alert("게시글이 신고되었습니다."); // 사용자에게 알림
        document.querySelector(".warning").style.display = "none";
    });

    document.querySelector(".no")?.addEventListener("click", () => {
        document.querySelector(".warning").style.display = "none";
    });

    // 경고창 배경 클릭 시 닫기
    document.querySelector(".warning .background_gray")?.addEventListener("click", () => {
        document.querySelector(".warning").style.display = "none";
    });
});
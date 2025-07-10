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

// 스크랩 버튼 이벤트
document.addEventListener("DOMContentLoaded", function () {
document.getElementById("scrap-button")?.addEventListener("click", function () {
    const postId = this.dataset.postId;
    const button = this;
    const textDiv = button.querySelector(".button_text");
    
    fetch(`/posts/${postId}/scrap/`, {
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
        if (data.scrapped) {
            alert("스크랩 완료!");
            textDiv.textContent = "스크랩 취소";
        } else {
            alert("스크랩 취소됨.");
            textDiv.textContent = "스크랩";
        }
    })
    .catch(error => {
        console.error('스크랩 요청 중 오류 발생:', error);
        alert("스크랩 처리 중 오류가 발생했습니다. 로그인 상태를 확인해주세요.");
    });
});
});

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
    document.querySelector(".declatation_img")?.addEventListener("click", () => {
        document.querySelector(".warning").style.display = "block";
    });

    document.querySelector(".yes")?.addEventListener("click", () => {
        document.querySelector(".warning").style.display = "none";
    });

    document.querySelector(".no")?.addEventListener("click", () => {
        document.querySelector(".warning").style.display = "none";
    });
});

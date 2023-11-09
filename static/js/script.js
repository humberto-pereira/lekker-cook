//  hide the comment form "Content" label 
window.addEventListener('load', function() {
    document.querySelector('label[for="id_content"]').style.display = 'none';
});

// This function gets the CSRF token from the cookies
function getCsrfToken() {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim().split('=');
        if (cookie[0] === 'csrftoken') {
            return cookie[1];
        }
    }
    return '';
}


// This script handles the "Like" button click event for comments.
document.addEventListener('DOMContentLoaded', function() {
    var likeButtons = document.querySelectorAll('.like-btn');
    var csrfToken = getCsrfToken(); // Get the CSRF token from the cookies
    likeButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var commentId = this.dataset.commentId;
            var url = `/like_comment/${commentId}/`; // URL to like a comment
            // Use the fetch API to send a POST request to the server
            fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken, // Include the CSRF token
                },
            })
            .then(response => response.json())
            .then(data => {
                if(data.error){
                    alert(data.error); // Alert if there is an error
                } else {
                    // Update the like count
                    var likesCount = document.querySelector(`#likes-count-${commentId}`);
                    if (likesCount) {
                        likesCount.textContent = data.likes_count;
                    } else {
                        console.error('Likes count element not found.')
                    }
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});
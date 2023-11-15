//  hide the comment form "Content" label
window.addEventListener("load", function () {
    document.querySelector('label[for="id_content"]').style.display = "none";
});

// This function gets the CSRF token from the cookies
function getCsrfToken() {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim().split("=");
        if (cookie[0] === "csrftoken") {
            return cookie[1];
        }
    }
    return "";
}

// This script handles the "Like" button click event for comments.
document.addEventListener("DOMContentLoaded", function () {
    var likeButtons = document.querySelectorAll(".like-btn");
    var csrfToken = getCsrfToken(); // Get the CSRF token from the cookies
    likeButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var commentId = this.dataset.commentId;
            // URL to like a comment
            var url = `/like_comment/${commentId}/`;
            // Use the fetch API to send a POST request to the server
            fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken, // Include the CSRF token
                },
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.error) {
                        alert(data.error); // Alert if there is an error
                    } else {
                        // Update the like count
                        var likesCount = document.querySelector(
                            `#likes-count-${commentId}`
                        );
                        if (likesCount) {
                            likesCount.textContent = data.likes_count;
                        } else {
                            console.error("Likes count element not found.");
                        }
                    }
                })
                .catch((error) => {
                    console.error("Error:", error);
                });
        });
    });
});

// star rating

// Rating form interaction and submission
// Function to get the CSRF token from the cookies
function getCsrfToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

// Function to update the visual display of the stars for the user's rating
function updateUserRatingDisplay(rating) {
    const userStars = document.querySelectorAll('.user-rating .rating-star');
    userStars.forEach((star, index) => {
        if (index < rating) {
            star.classList.add('fas');
            star.classList.remove('far');
        } else {
            star.classList.remove('fas');
            star.classList.add('far');
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const ratingForm = document.getElementById('ratingForm');
    const starsInput = document.getElementById('starsInput');

    // Initialize the stars display based on the user's last rating if available
    if (starsInput.value) {
        updateUserRatingDisplay(parseInt(starsInput.value, 10));
    }

    // Rating form submission
    ratingForm.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevent the default form submission

        const formData = new FormData(this);
        const url = this.action;

        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCsrfToken(),
            },
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if(data.success) {
                // Update the average rating display
                document.querySelector('.average-rating span').textContent = `Average Rating: ${data.average_rating.toFixed(1)}`;
            } else {
                // Handle any errors
                alert('There was an error submitting your rating');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Star click event for user rating
    document.querySelectorAll('.user-rating .rating-star').forEach(star => {
        star.addEventListener('click', function() {
            const value = this.dataset.value;
            starsInput.value = value; // Set the rating value
            updateUserRatingDisplay(parseInt(value, 10)); // Update the display with the user's rating
        });
    });
});



//  hide the comment form "Content" label
window.addEventListener("load", function () {
    document.querySelector('label[for="id_content"]').style.display = "none";
});

// This function gets the CSRF token from the cookies
function getCsrfToken() {
    /**
     * Retrieve the CSRF token from the cookies. Iterates through the cookies
     * returns the value of the "csrftoken" cookie if it exists.
     * 
     * Returns string: the CSRF token value if it exists, otherwise an empty string
     */
    
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim().split("=");
        if (cookie[0] === "csrftoken") {
            return cookie[1];
        }
    }
    return "";
}

/**
 * Attaches click event listeners to all elements with the 'like-btn' class after the DOM content is fully loaded. 
 * On clicking a like button, sends a POST request to like the associated comment and updates the like count 
 * displayed on the page. Uses the CSRF token obtained from cookies for the POST request.
 *
 * Utilizes:
 * - `getCsrfToken()`: A function to retrieve the CSRF token from cookies.
 * - Fetch API: To send asynchronous HTTP requests.
 */
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

/**
 * Initializes the user's rating display when the DOM content is fully loaded. Retrieves the user's 
 * last rating from a hidden input field and updates the rating display accordingly.
 *
 * Utilizes:
 * - `updateUserRatingDisplay(rating)`: A function to visually update the rating display based on the provided rating.
 */

document.addEventListener('DOMContentLoaded', function() {
    const ratingForm = document.getElementById('ratingForm');
    const starsInput = document.getElementById('starsInput');

    // Initialize the stars display based on the user's last rating if available
    if (starsInput.value) {
        updateUserRatingDisplay(parseInt(starsInput.value, 10));
    }

/**
 * Attaches an event listener to the rating form to handle its submission. Prevents the default form submission, 
 * sends a POST request with the rating data, and updates the UI based on the server's response.
 *
 * Utilizes:
 * - Fetch API: To send asynchronous HTTP POST requests.
 * - `getCsrfToken()`: To retrieve the CSRF token for the POST request.
 */
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
            displayMessage('Your rating was submitted successfully', 'success');
        } else {
            // Handle any errors
            alert('There was an error submitting your rating');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function displayMessage(text, type) {
    const messageContainer = document.getElementById('message-container'); // You need to have a div with this id in your HTML
    messageContainer.innerHTML = `<div class="alert alert-${type === 'error' ? 'danger' : 'success'}">${text}</div>`;
    messageContainer.style.display = 'block';
    // Hide the message after 5 seconds
    setTimeout(function() {
        messageContainer.style.display = 'none';
    }, 5000);
}

/**
 * Attaches click event listeners to each star in the user-rating section. On clicking a star, updates a hidden input 
 * field with the rating value and calls a function to visually update the rating display.
 *
 * Utilizes:
 * - `updateUserRatingDisplay(rating)`: Function to visually reflect the user's selected rating.
 */
document.querySelectorAll('.user-rating .rating-star').forEach(star => {
    star.addEventListener('click', function() {
        const value = this.dataset.value;
        starsInput.value = value; // Set the rating value
        updateUserRatingDisplay(parseInt(value, 10)); // Update the display with the user's rating
        });
    });
});

/**
 * Automatically dismisses any dismissible alert elements on the page 7 seconds after the DOM content is fully loaded. 
 * This is achieved by removing the 'show' class and then removing the alert element from the DOM.
 */
document.addEventListener('DOMContentLoaded', function() {
    // Get all the alert elements
    const alerts = document.querySelectorAll('.alert-dismissible');
    // set a timeout to remove the alert after 7 seconds
    alerts.forEach(function(alert) {
        setTimeout(function() {
            alert.classList.remove('show');
            setTimeout(() => alert.remove(), 150);
        }, 7000);
    });
});
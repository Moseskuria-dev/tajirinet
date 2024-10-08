// contact.js

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".contact-form");
    
    if (form) {  // Check if form exists
        form.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent the default form submission

            const formData = new FormData(form); // Get form data
            const data = {
                name: formData.get("name"),
                email: formData.get("email"),
                subject: formData.get("subject"),
                message: formData.get("message"),
            };

            // Send the form data using fetch
            fetch("/send-message/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"), // Get CSRF token
                },
                body: JSON.stringify(data), // Convert data to JSON
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json(); // Parse the JSON response
            })
            .then(data => {
                // Handle the success response
                alert("Message sent successfully!");
                form.reset(); // Reset the form
            })
            .catch((error) => {
                // Handle any errors
                alert("There was a problem with your submission: " + error.message);
            });
        });
    }

    // Function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Check if this cookie string begins with the name we want
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

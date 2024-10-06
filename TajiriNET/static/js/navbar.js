document.addEventListener("DOMContentLoaded", function () {
    const navbarToggle = document.getElementById("navbar-toggle");
    const dropdownMenu = document.getElementById("dropdown-menu");

    navbarToggle.addEventListener("click", function () {
        dropdownMenu.classList.toggle("show");
    });

    // Close dropdown when clicking outside
    document.addEventListener("click", function (event) {
        if (!navbarToggle.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.classList.remove("show");
        }
    });
});

// Function to handle the dropdown functionality
document.addEventListener('DOMContentLoaded', function () {
    const aboutButton = document.getElementById('dropdown-about-button');
    const dropdownButtons = document.querySelector('.dropdown-buttons');

    // Show dropdown when About button is clicked
    aboutButton.addEventListener('click', function (event) {
        event.stopPropagation(); // Prevent event from bubbling up
        dropdownButtons.style.display = dropdownButtons.style.display === 'block' ? 'none' : 'block';
    });

    // Hide dropdown when clicking outside the About button
    document.addEventListener('click', function (event) {
        if (!aboutButton.contains(event.target) && !dropdownButtons.contains(event.target)) {
            dropdownButtons.style.display = 'none';
        }
    });
});

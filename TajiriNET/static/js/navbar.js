// JavaScript for Navbar Toggle
document.addEventListener('DOMContentLoaded', function() {
    const navbarToggle = document.getElementById('navbar-toggle');
    const dropdownMenu = document.getElementById('dropdown-menu');

    navbarToggle.addEventListener('click', function() {
        dropdownMenu.classList.toggle('show');
        navbarToggle.classList.toggle('active');
    });

    // Optional: Close the dropdown when clicking outside
    window.addEventListener('click', function(event) {
        if (!navbarToggle.contains(event.target) && !dropdownMenu.contains(event.target)) {
            if (dropdownMenu.classList.contains('show')) {
                dropdownMenu.classList.remove('show');
                navbarToggle.classList.remove('active');
            }
        }
    });
});

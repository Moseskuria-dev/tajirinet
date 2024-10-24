// script.js

// This file can be used for any JavaScript functionality needed for the app.
// Currently, it is empty.
// script.js

// Function to handle search
function searchContent() {
    const input = document.getElementById("searchInput").value.toLowerCase();
    const resultsList = document.getElementById("resultsList");
    const searchModal = document.getElementById("searchModal");

    // Clear previous results
    resultsList.innerHTML = '';

    // Check if the modal is displayed; if not, show it
    if (searchModal.style.display !== 'block') {
        searchModal.style.display = 'block';
    }

    // Sample data - replace this with your actual data source from the HTML
    const data = [
        { title: "Home", url: "/homepage" },
        { title: "About Us", url: "/our-company" },
        { title: "Our Products", url: "/our-services" },
        { title: "Contact", url: "/contact" },
        { title: "Plans", url: "/plans" },
        { title: "Customer Support", url: "/contact" },
        // Add more items as needed
    ];

    // Filter data based on input
    const filteredResults = data.filter(item => item.title.toLowerCase().includes(input));

    // Display results in modal
    if (filteredResults.length > 0) {
        filteredResults.forEach(result => {
            const li = document.createElement("li");
            li.textContent = result.title;
            li.onclick = function() {
                // Handle click on result
                window.location.href = result.url; // Redirect to the URL
            };
            resultsList.appendChild(li);
        });
    } else {
        // Optionally, show a message if no results found
        const li = document.createElement("li");
        li.textContent = "No results found.";
        resultsList.appendChild(li);
    }
}

// Close modal function
function closeModal() {
    const searchModal = document.getElementById("searchModal");
    searchModal.style.display = 'none'; // Hide modal
}

// Optional: Hide modal when clicking outside of it
window.onclick = function(event) {
    const searchModal = document.getElementById("searchModal");
    if (event.target === searchModal) {
        closeModal();
    }
};

// Optional: Hide modal when pressing the Escape key
document.addEventListener('keydown', function(event) {
    if (event.key === "Escape") {
        closeModal();
    }
});

// Add event listener to trigger search when pressing "Enter"
document.getElementById("searchInput").addEventListener('keydown', function(event) {
    if (event.key === "Enter") {
        searchContent(); // Call searchContent function
        event.preventDefault(); // Prevent the default form submission behavior, if any
    }
});

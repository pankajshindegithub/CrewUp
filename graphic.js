document.addEventListener("DOMContentLoaded", function () {
    // Hamburger menu toggle
    const menuToggle = document.querySelector(".menu-toggle");
    const nav = document.querySelector("nav");

    menuToggle.addEventListener("click", function () {
        nav.classList.toggle("active");
    });

    // Adjust search bar width on small screens
    function adjustSearchBar() {
        const searchBar = document.querySelector("input");
        if (window.innerWidth < 768) {
            searchBar.style.width = "60%";
        } else {
            searchBar.style.width = "40%";
        }
    }

    window.addEventListener("resize", adjustSearchBar);
    adjustSearchBar(); // Call once on load

    // Search button functionality
    const searchButton = document.querySelector(".search-btn");
    const searchInput = document.querySelector(".search-container input");

    searchButton.addEventListener("click", function () {
        const query = searchInput.value.trim();

        if (query) {
            console.log("Searching for:", query); // Or trigger your actual search action
        }
    });

    
        // FAQ toggle functionality
        function toggleFAQ(index) {
            const answers = document.querySelectorAll('.faq-answer');
            const icons = document.querySelectorAll('.icon');
    
            if (answers[index].classList.contains('active')) {
                // Close the FAQ (hide the answer)
                answers[index].classList.remove('active');
                icons[index].style.transform = 'rotate(0deg)';
            } else {
                // Open the FAQ (show the answer)
                answers[index].classList.add('active');
                answers[index].scrollIntoView({ behavior: 'smooth' });
                icons[index].style.transform = 'rotate(180deg)';
            }
        }
    
        // Ensure the FAQ toggle works
        const faqItems = document.querySelectorAll('.faq-question');
        faqItems.forEach((item, index) => {
            item.addEventListener('click', function() {
                toggleFAQ(index);
            });
        });
    });
    
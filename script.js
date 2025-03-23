function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('show');
}


document.addEventListener("DOMContentLoaded", function () {
const stickyNav = document.getElementById("stickyServices");

window.addEventListener("scroll", function () {
    const scrollPosition = window.scrollY;
    const triggerHeight = 300; // Show sub navbar after 300px scroll

    if (scrollPosition > triggerHeight) {
        stickyNav.style.display = "block";
    } else {
        stickyNav.style.display = "none";
    }
});

// Mobile Navbar Toggle
document.getElementById("hamburger").addEventListener("click", function () {
    document.getElementById("nav-links").classList.toggle("show");
});
});


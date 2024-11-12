document.addEventListener("DOMContentLoaded", function() {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    function toggleMenu() {
        navLinks.classList.toggle('active');
        hamburger.classList.toggle('active');
    }

    hamburger.addEventListener('click', toggleMenu);

    // Cerrar el menú si se hace clic fuera de él
    document.addEventListener('click', function(event) {
        if (!navLinks.contains(event.target) && !hamburger.contains(event.target)) {
            navLinks.classList.remove('active');
            hamburger.classList.remove('active');
        }
    });
});


// Cambiar el color de fondo del navbar al hacer scroll
window.onscroll = function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
};

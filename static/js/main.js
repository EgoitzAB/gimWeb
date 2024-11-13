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

document.addEventListener('DOMContentLoaded', function() {
    const items = document.querySelectorAll('.grid-item');

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Añadir la clase 'visible' cuando el elemento entra en la pantalla
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.5 // El 50% del elemento debe estar visible
    });

    // Observa cada elemento de la cuadrícula
    items.forEach(item => {
        observer.observe(item);
    });
});
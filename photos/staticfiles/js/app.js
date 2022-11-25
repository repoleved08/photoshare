// Mobile menu
const burgerIcon = document.querySelector('#burger')
const navLinks = document.querySelector('#nav-menu')

burgerIcon.addEventListener('click', () => {
    navLinks.classList.toggle('is-active')
})
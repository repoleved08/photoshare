// Mobile menu
const burgerIcon = document.querySelector('#burger')
const navLinks = document.querySelector('#nav-menu')

burgerIcon.addEventListener('click', () => {
    navLinks.classList.toggle('is-active')
})


// Modal

const addButton = document.querySelector('#signup')
const modalBg = document.querySelector('.modal-background')
const modal = document.querySelector('.modal')

addButton.addEventListener('click', () => {
    modal.classList.add('is-active')
})

modalBg.addEventListener('click', () => {
    modal.classList.remove('is-active')
})
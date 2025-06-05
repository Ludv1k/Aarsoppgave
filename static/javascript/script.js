// Makes it so that the 'first[CHANGE LATER]' redirects you to the site '/hi[CHANGE LATER]'
let nav_signup = document.getElementById("signup")
nav_signup.addEventListener("click", signup_page)
function signup_page() {
    location.href = '/signup'
}

let nav_login = document.getElementById("login")
nav_login.addEventListener("click", login_page)
function login_page() {
    location.href = '/login'
}

document.getElementById('openSidebar').addEventListener('click', () => {
    document.body.classList.toggle('showCart');
});

document.querySelector('.cartTab .close').addEventListener('click', () => {
    document.body.classList.remove('showCart');
});


let logo_nav_home = document.getElementById("logo_nav")
logo_nav_home.addEventListener("click", nav_home)
function nav_home() {
    location.href = '/'
}

let nav_products_btn = document.getElementById("nav_products_btn")
nav_products_btn.addEventListener("click", nav_products)
function nav_products() {
    location.href = '/products'
}
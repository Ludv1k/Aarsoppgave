let login = document.getElementById("login")
if (login) {
    login.addEventListener("click", function () {
        location.href = '/login';
    });
}

let signup = document.getElementById("signup")
if (signup) {
    signup.addEventListener("click", function () {
        location.href = '/signup';
    });
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

let cart_btn = document.getElementById("cart_btn")
cart_btn.addEventListener("click", nav_cart)
function nav_cart() {
    location.href = '/products'
}

// DELETE BELOW

let popup_opn = document.getElementById("popup_btn_opn");
popup_opn.addEventListener("click", openPopup);

function openPopup() {
    document.getElementById("popup").classList.add("open-popup");
}
let popup_cls = document.getElementById("popup_btn_cls")
popup_cls.addEventListener("click", closePopup)
function closePopup() {
    document.getElementById("popup").classList.remove("open-popup");
}

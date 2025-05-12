// Makes it so that the 'first[CHANGE LATER]' redirects you to the site '/hi[CHANGE LATER]'
let nav_signup = document.getElementById("signup")
nav_signup.addEventListener("click", signup_page)

function signup_page() {
    location.href = '/signup'
}
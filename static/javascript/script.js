// Makes it so that the 'first[CHANGE LATER]' redirects you to the site '/hi[CHANGE LATER]'
let nav_btn1 = document.getElementById("test1")
nav_btn1.addEventListener("click", test_side1)

function test_side1() {
    location.href = '/hi'
}
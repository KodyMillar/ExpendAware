
// const loginTab = document.querySelector("#login-tab");
// const registerTab = document.querySelector("#register-tab");

// function selectedTab(e) {
//     console.log(e.target)
//     console.log("hello")
// }

// loginTab.addEventListener("click", selectedTab)
// registerTab.addEventListener("click", selectedTab)

const loginContainer = document.getElementById('login-container');
const registerContainer = document.getElementById('register-container');
registerContainer.style.display = "none";

const loginTab = document.getElementById('login-tab');
const registerTab = document.getElementById('register-tab');

loginTab.addEventListener('click', function() {
    registerContainer.style.display = "none";
    loginContainer.style.display = "flex";
    if (registerTab.classList.contains("active")) {
        registerTab.classList.toggle("active")
        loginTab.classList.toggle("active")
    }
});

registerTab.addEventListener('click', function() {
    registerContainer.style.display = "flex";
    loginContainer.style.display = "none";

    if (loginTab.classList.contains("active")) {
        loginTab.classList.toggle("active")
        registerTab.classList.toggle("active")
    }
});
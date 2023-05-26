/* Side Bar */
closeButton = document.querySelector("#side-menu-close")
sideMenu = document.querySelector("#menu-expand")
menuIcon = document.querySelector("#menu-btn")

function openMenu() {
    sideMenu.style.width = "200px";
    sideMenu.classList.toggle("menu-display");
}

menuIcon.addEventListener("click", openMenu)

function closeMenu() {
    if (sideMenu.style.width !== "0") {
        sideMenu.style.width = "0";
    }
}

closeButton.addEventListener("click", closeMenu)
/* End of Side Bar*/
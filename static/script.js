/* side bar menu
-------------------------------------------*/

closeButton = document.querySelector("#side-menu-close")
sideMenu = document.querySelector("#menu-expand")
menuButton = document.querySelector(".menu")

function openMenu() {
    sideMenu.style.width = "200px";
    sideMenu.classList.toggle("menu-display");
}

menuButton.addEventListener("click", openMenu)

function closeMenu() {
    if (sideMenu.style.width !== "0") {
        sideMenu.style.width = "0";
    }
}

closeButton.addEventListener("click", closeMenu)


/* categories page 
-------------------------------------------*/

const categoriesList = document.querySelectorAll(".category")
const budgetDropDown = document.querySelectorAll(".budget-dropdown")

let categoryIndex = 0;
let compareIndex = 0;

for(let category of categoriesList){
    category.addEventListener("click", (e) => {
        let categoryName = e.target.querySelector("h4").textContent
        category.classList.toggle("category-clicked");
        if (category.classList.contains("category-clicked")){
            for(let budget of budgetDropDown) {
                if (categoryName === budget.id){
                    document.querySelector("#" + budget.id).style.height = "200px";
                }
            }
        }

        else {
        for(let budget of budgetDropDown) {
            if (e.target.querySelector("h4").textContent === budget.id){
                document.querySelector("#" + budget.id).style.height = "0";
            }
        }
        }
        // let compareIndex = 0;
        // for(let category of categoriesList) {
        //     // console.log(compareIndex);
        //     // console.log(categoryIndex)
        //     if (category.classList.contains("category-clicked") && compareIndex !== categoryIndex)
        //         {
        //             category.classList.toggle("category-clicked");
        //         }
        //     compareIndex += 1;
        // }
        // categoryIndex += 1;
        // console.log(categoryIndex);
        // if (categoryIndex === categoriesList.length-1) {
        //     categoryIndex = 0;
        //     console.log(categoryIndex)
        // }
    });
}

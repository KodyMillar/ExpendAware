/* Overview percentage bar on homepage
-------------------------------------------*/
categoryPercentLabel = document.querySelectorAll(".percent-label");

for(let category of categoryPercentLabel) {
    percentage = category.querySelector("label").textContent.replace(" Spent", "");
    if (category.querySelector(".percentage")) {
        percentageGauge = category.querySelector(".percentage");
        percentageGauge.style.width = percentage;
    }
}


/* Homepage button functionality
-------------------------------------------*/
const budgetButton = document.getElementById('add-budget');
const budgetForm = document.getElementById('budget-container');
const expenseButton = document.getElementById('add-expense');
const expenseForm = document.getElementById('expense-container');
const catButton = document.getElementById('add-category');
const catForm = document.getElementById('category-container');
const overview = document.getElementsByClassName('view-section');
const forms = document.getElementsByClassName('container');
forms[0].style.display = "none";

// Show budget form
budgetButton.addEventListener('click', function() {
    budgetForm.style.display = "block";
    expenseForm.style.display = "none";
    catForm.style.display = "none";
    overview[0].style.display = "none";
    forms[0].style.display = "flex"

    budgetButton.classList.add("active")
    expenseButton.classList.remove("active")
    catButton.classList.remove("active")
});

// Show expense form
expenseButton.addEventListener('click', function() {
    budgetForm.style.display = "none";
    expenseForm.style.display = "block";
    catForm.style.display = "none";
    overview[0].style.display = "none";
    forms[0].style.display = "flex"

    expenseButton.classList.add("active")
    budgetButton.classList.remove("active")
    catButton.classList.remove("active")
});

// Show category form
catButton.addEventListener('click', function() {
    budgetForm.style.display = "none";
    expenseForm.style.display = "none";
    catForm.style.display = "block";
    overview[0].style.display = "none";
    forms[0].style.display = "flex"

    catButton.classList.add("active")
    budgetButton.classList.remove("active")
    expenseButton.classList.remove("active")
});


/* alert message */
const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
const appendAlert = (message, type) => {
    const wrapper = document.createElement('div')
    wrapper.innerHTML = 
        `<div class="alert alert-warning d-flex align-items-center alert-dismissible fade show" role="alert" data-bs-dismiss="alert" id="alert-box">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="16" fill="currentColor" class="bi bi-exclamation-circle" viewBox="0 0 16 16">
                <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                <path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/>
            </svg>
            <div>
                ${message}
            </div>
        </div>`

    alertPlaceholder.append(wrapper)
    alertPlaceholder.classList.add("fade")

    setTimeout(() => {
        // removes element from DOM
        wrapper.style.display = "none";

    }, 3000); 
}


// const alertTrigger = document.getElementById('liveAlertBtn')
// if (alertTrigger) {
//     alertTrigger.addEventListener('click', () => {
//     appendAlert("", 'success')
//     })
// }

const addCategoryForm = document.forms["add-category-form"]
const addBudgetForm = document.forms["add-budget-form"]
const addExpenseForm = document.forms["add-expense-form"]

const categoryNames = document.querySelectorAll(".category-name")
const budgetNames = document.querySelectorAll(".budget-name")
const budgetAmount = document.querySelectorAll(".budget-amount")


addCategoryForm.onsubmit = function(e) {
    
    let newCategoryName = addCategoryForm.category.value

    console.log(newCategoryName.trim().toLowerCase())

    for (let category of categoryNames) {
        if (category.textContent.trim().toLowerCase() === newCategoryName.trim().toLowerCase()) {
            appendAlert("Category already exists")
            e.preventDefault();
        }
    }
}

addBudgetForm.onsubmit = function(e) {
    
    for (let budget of budgetNames) {
        if(budget.textContent.trim().toLowerCase() === addBudgetForm.name.value.trim().toLowerCase()) {
            appendAlert("Budget already exists");
            e.preventDefault();
        }
    }
}

for (let budget of budgetAmount) {
    let expenses = budget.querySelectorAll(".totals-expense-amount");
            let expense_total = 0;
            for (let expense of expenses) {
                expense_total += parseInt(expense.textContent);
            }
            
}

addExpenseForm.onsubmit = function(e) {

    for (let budget of budgetAmount) {
        if (addExpenseForm.budget.value === budget.querySelector(".totals-budget-name").textContent) {
            
            let expenses = budget.querySelectorAll(".totals-expense-amount");
            let expense_total = 0;
            for (let expense of expenses) {
                expense_total += parseInt(expense.textContent);
            }
            if ((parseInt(addExpenseForm.amount.value) + expense_total) > parseInt(budget.querySelector(".totals-budget-amount").textContent)) {
                appendAlert("You've reached your budget limit!");
                e.preventDefault();
            }
        }
    }
}




const budgetFr = document.getElementById('budget-from');
const budgetTo = document.getElementById('budget-to');
const amountTr = document.getElementById('transfer-amount');

const categorySF = document.querySelector("#category-sf");
const budgetSF = document.querySelector("#budget-sf");
const amountSF = document.querySelector("#amount-sf");
const categoryST = document.querySelector("#category-st");
const budgetST = document.querySelector("#budget-st");
const amountST = document.querySelector("#amount-st");

const summaryR = document.getElementById('summary-result');
const transferBtn = document.getElementById('transfer-btn');

let previousOption = null;

budgetFr.addEventListener('change', function() {
    // Reset when change budget from 
    budgetTo.value = 'defaultOption';
    budgetTo.disabled = false;
    amountTr.disabled = true;
    amountTr.value = "";
    categorySF.innerHTML = ``;
    budgetSF.innerHTML = ``;
    amountSF.innerHTML = ``;
    categoryST.innerHTML = ``;
    budgetST.innerHTML = ``;
    amountST.innerHTML = ``;
    
    // Enable the previously disabled option (previousOption = budgetToOption)
    if (previousOption !== null) {
        previousOption.disabled = false;
    }

    // Chose <option> and then <option>.value
    const selectedValue = budgetFr.options[budgetFr.selectedIndex].value;
    // Disable the currently selected option
    const budgetToOption = budgetTo.querySelector(`option[value="${selectedValue}"]`);
    budgetToOption.disabled = true;
    previousOption = budgetToOption;
});

budgetTo.addEventListener('change', function() {
    amountTr.value = "";
    amountTr.disabled = false;
    categorySF.innerHTML = ``;
    budgetSF.innerHTML = ``;
    amountSF.innerHTML = ``;
    categoryST.innerHTML = ``;
    budgetST.innerHTML = ``;
    amountST.innerHTML = ``;
});

amountTr.addEventListener('input', function() {
    const amountTrValue = parseFloat(amountTr.value);
    const budgetFrOption = budgetFr.options[budgetFr.selectedIndex];
    const budgetToOption = budgetTo.options[budgetTo.selectedIndex];

    const budgetFrObject = JSON.parse(budgetFrOption.value.replace(/'/g, '"'));
    const budgetToObject = JSON.parse(budgetToOption.value.replace(/'/g, '"'));
    
    categorySF.innerHTML = `${budgetFrObject['category']}`
    budgetSF.innerHTML = `${budgetFrObject['name']}`

    categoryST.innerHTML = `${budgetToObject['category']}`
    budgetST.innerHTML = `${budgetToObject['name']}`

    if (`${budgetFrObject['amount'] - amountTrValue}` >= 0) {
        amountSF.innerHTML = `$${budgetFrObject['amount'] - amountTrValue}`
        let ccc = parseInt(budgetToObject['amount']) + amountTrValue;
        amountST.innerHTML = `$${parseInt(budgetToObject['amount']) + amountTrValue}`;
    } else {
        amountSF.innerHTML = `Insufficient\nfunds`
        let abc = budgetFrObject['amount'] + budgetToObject['amount']
        amountST.innerHTML = `$${parseInt(budgetFrObject['amount']) + parseInt(budgetToObject['amount'])}`
    }
});

transferBtn.addEventListener('click', function() {
    if (amountTr.value === "") {
        alert('Missing Values');
        event.preventDefault();
    }

    const amountTrValue = parseFloat(amountTr.value);
    const budgetFrOption = budgetFr.options[budgetFr.selectedIndex];
    const budgetToOption = budgetTo.options[budgetTo.selectedIndex];

    const budgetFrObject = JSON.parse(budgetFrOption.value.replace(/'/g, '"'));
    const budgetToObject = JSON.parse(budgetToOption.value.replace(/'/g, '"'));
    
    if (`${budgetFrObject['amount'] - amountTrValue}` < 0) {
        alert('Insufficient Funds');
        event.preventDefault();
    }

});
    
    // Active Tab //
    const loginTab = document.getElementById('login-tab');
    const regTab = document.getElementById('reg-tab');

    const loginForm = document.getElementById('login-form');
    const regForm = document.getElementById('reg-form');
    regForm.style.display = "none";

    // Show Login Form & Hide Register Form//
    loginTab.addEventListener('click', function() {
        regForm.style.display = "none";
        loginForm.style.display = "flex";

        regTab.classList.remove("active")
        loginTab.classList.add("active")
    });

    // Show Register Form & Hide Login Form//
    regTab.addEventListener('click', function() {
        regForm.style.display = "flex";
        loginForm.style.display = "none";

        regTab.classList.add("active")
        loginTab.classList.remove("active")
    });
// End of Active Tab //



// Login Alert //
    document.addEventListener('DOMContentLoaded', function() {
        // Get the flash message
        const flashMessage = document.getElementById('flash-messages');
        
        // Check if the flash message exists
        if (flashMessage) {
            // Show & Remove message in 0 second (need this to display message first)
            setTimeout(function() {flashMessage.classList.remove('show');}, 0);
            // Set a timeout to remove flashout display
            setTimeout(function() {flashMessage.style.display = 'none';}, 4000);
        }
    });
// End of Login Alert //



// Register Alert //
    // User input in Register Form //
    const regPwd1 = document.getElementById('reg-pwd1');
    const regPwd2 = document.getElementById('reg-pwd2');
    const regName = document.getElementById('reg-name');
    const regEmail = document.getElementById('reg-email');
    const regBtn = document.getElementById('reg-btn');
    const regSecurityA = document.getElementById('reg-security-a');
    
    // Alert Display IDs //
    const regOverlay = document.getElementById('reg-overlay');
    const regAlertBox = document.getElementById('reg-alert-box');
    const regAlertMessage = document.getElementById('reg-alert-message');
    const regAlertExitBtn = document.getElementById('reg-alert-exit-btn');
    
    // Alert Function //
    function showAlert(message) {
        regAlertMessage.innerHTML = message;
        regAlertBox.style.display = 'block';
        regOverlay.style.display = "flex";
        event.preventDefault();
    }

    // Click the button to either login or exit alert // 
    regAlertExitBtn.addEventListener('click', function(event) {
        if (regAlertMessage.innerHTML !== "Success!") {
            event.preventDefault();
        }
        regOverlay.style.display = 'none';
    });
    
    // Click overlay to exit alert  //
    regOverlay.addEventListener('click', function(event) {
        regOverlay.style.display = 'none';
    });

    // Fetch login JSON and Use Alert Function //
    fetch('login.json')
    .then(response => response.json())
    .then(data => {
        // Handle the retrieved JSON data
        regBtn.addEventListener('click', function(event) {
            const emailExists = data.some(x => x.email === regEmail.value);
            regAlertExitBtn.innerHTML = "x";
            if (regPwd1.value === "" || 
                regPwd2.value === "" || 
                regName.value === "" || 
                regEmail.value === "" || 
                regSecurityA.value == "" ||
                !regEmail.value.includes('@')) {

            } else if (emailExists) {
                showAlert("This email is already used")
            } else if (regPwd1.value.length < 8) {
                showAlert("Password must be longer than 7 characters");
            } else if (regPwd1.value !== regPwd2.value) {
                showAlert("Both passwords are not matched");
            } else {
                regAlertExitBtn.innerHTML = "login";
                showAlert("Success!");
            }
        });
    })
    .catch(error => {
        // Handle any errors
    });
// End of Register Alert //



// Remember Me //
    const rmbMe = document.getElementById('rmb-me');
    const loginEmail = document.getElementById('login-email');
        
    // Check if the checkbox parameter exists in the URL
    // window.location.search string portion of the URL from a question mark [?]
    // urlParams is useful when refreshing the page with a specific URL.
    // localStorage is useful for maintaining data and state even when the browser is closed and reopened
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('remember') === 'true') {
        rmbMe.checked = true;
        loginEmail.value = localStorage.getItem('email');
    } else if (localStorage.getItem('rememberEmail') === 'true') {
        rmbMe.checked = true;
        loginEmail.value = localStorage.getItem('email');
    }
    
        
    // Add or remove the checkbox parameter when the checkbox state changes
    rmbMe.addEventListener('change', () => {
        if (rmbMe.checked) {
            urlParams.set('remember', 'true');
            localStorage.setItem('rememberEmail', true);
            localStorage.setItem('email', loginEmail.value);
        } else {
            urlParams.delete('remember');
            localStorage.setItem('rememberEmail', false);
            localStorage.removeItem('email');
        }

        // Update the URL with the modified parameters
        const newUrl = `${window.location.pathname}?${urlParams.toString()}`;
        window.history.replaceState({}, '', newUrl);
    });

    // This ensures input does not disappear (must have)
    loginEmail.addEventListener('input', () => {
        if (rmbMe.checked) {
            localStorage.setItem('email', loginEmail.value);
        }
    });
// End of Remember Me //


// Forget Password //
    // User input in Reset Form //
    const fgtPwd1 = document.getElementById('fgt-pwd1');
    const fgtPwd2 = document.getElementById('fgt-pwd2');
    const fgtEmail = document.getElementById('fgt-email');
    const fgtSecurityA = document.getElementById('fgt-security-a');
    const fgtBtn = document.getElementById('fgt-btn');
    const loginFgtLink = document.getElementById('login-fgt-link');
    
    // Alert Display IDs //
    const fgtOverlay = document.getElementById('fgt-overlay');
    const fgtBox = document.getElementById('fgt-box');
    const fgtExitBtn = document.getElementById('fgt-exit-btn');
    
    // Click to exit form // 
    fgtExitBtn.addEventListener('click', function(event) {
        event.preventDefault();
        fgtOverlay.style.display = 'none';
    });
    
    // Click overlay to exit alert  //
    fgtOverlay.addEventListener('click', function(event) {
        if (event.target === fgtOverlay) {
            //fgtOverlay.style.display = 'none';
            //refreshPage();
        }
    });

    // Click forgot link to show form
    loginFgtLink.addEventListener('click', () => {
        fgtOverlay.style.display = "block";
    });

    // Fetch login JSON and Rest Password //
    fetch('login.json')
    .then(response => response.json())
    .then(data => {
        // Handle the retrieved JSON data
        fgtBtn.addEventListener('click', function(event) {
            const emailExists = data.some(x => x.email === fgtEmail.value);
            const findUser = data.find(x=> x.email === fgtEmail.value)
            const fgtEmailError = document.getElementById('fgt-email-error');

            if (fgtEmail.value === "" || !findUser) {
                fgtEmailError.textContent = "email does not exist";
                event.preventDefault();
                return;
            }
            fgtEmailError.textContent = "";
            fgtEmail.disabled = true;

            const fgtSecurityBox = document.getElementById("fgt-security-box");
            const fgtPwdBox = document.getElementById("fgt-pwd-box");
            const fgtSecurityQ = document.getElementById('fgt-security-q')
            const fgtSecurityError = document.getElementById("fgt-security-error");
            const jsonSecurityA = findUser.answer;
            const jsonSecurityQ = findUser.question;
            

            if (fgtSecurityBox.style.display === "") {
                event.preventDefault();
                fgtSecurityBox.style.display = "block";
                fgtSecurityQ.innerHTML = jsonSecurityQ;

            } 

            if (fgtSecurityA.value === "" ) {
                event.preventDefault();
                return;
            } else if (jsonSecurityA !== fgtSecurityA.value) {
                event.preventDefault();
                fgtSecurityError.textContent = "Incorrect Answer!";
                return;
            } 
            
            if (jsonSecurityA === fgtSecurityA.value) {
                //event.preventDefault();
                fgtSecurityA.disabled = true;
                fgtPwdBox.style.display = "flex";
                fgtPwdBox.style.flexDirection = "column";
                fgtSecurityError.textContent = "";
            }
            
            if (fgtPwd1.value === "") {
                event.preventDefault();
            }
            if (fgtPwd1.value !== fgtPwd2.value) {
                event.preventDefault();
                document.getElementById("fgt-pwd-error").textContent = "Passwords are not matched!"
            } else if (fgtPwd1.value.length < 8 && fgtPwd1.value !== "") {
                event.preventDefault();
                document.getElementById("fgt-pwd-error").textContent = "Password must be longer than 8 characters"
            } else if (fgtPwd1.value === fgtPwd2.value && fgtPwd1.value !== "") {
                fgtEmail.disabled = false;
            }
        });
    })
    .catch(error => {
        // Handle any errors
    });

// End of Forget Password //


function refreshPage() {
    location.reload();
}
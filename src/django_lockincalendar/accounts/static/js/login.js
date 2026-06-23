const passwordInput = document.getElementById('inputPassword');
const toggleBtn = document.querySelector('.password-toggle');
const eyeIcon = document.querySelector('.password-field .bi-eye, .password-field .bi-eye-slash');

eyeIcon.addEventListener('click', function () {
    const isHidden = passwordInput.type === 'password';
    
    passwordInput.type = isHidden ? 'text' : 'password';

    eyeIcon.className = isHidden ? 'bi bi-eye-slash' : 'bi bi-eye';

    toggleBtn.setAttribute('aria-label', isHidden ? 'Hide password' : 'Show password');

    passwordInput.focus();
});
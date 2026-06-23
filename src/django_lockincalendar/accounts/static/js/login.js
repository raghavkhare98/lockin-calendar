const passwordInput = document.getElementById('inputPassword');
const eyeIcon = document.querySelector('.password-field .bi-eye, .password-field .bi-eye-slash');

let actual = '';
let revealTimer = null;
let revealed = false;

function render(showLast) {
    if (revealed) {
        passwordInput.value = actual;
    } else {
        const dots = '*'.repeat(actual.length);
        passwordInput.value = (showLast && actual.length > 0)
            ? dots.slice(0, -1) + actual.slice(-1)
            : dots;
    }
    passwordInput.selectionStart = passwordInput.selectionEnd = passwordInput.value.length;
}

passwordInput.addEventListener('beforeinput', function (e) {
    if (e.inputType === 'insertText' && e.data) {
        actual += e.data;
        e.preventDefault();
        clearTimeout(revealTimer);
        render(true);
        revealTimer = setTimeout(() => render(false), 500);
    } else if (e.inputType === 'deleteContentBackward') {
        actual = actual.slice(0, -1);
        e.preventDefault();
        clearTimeout(revealTimer);
        render(false);
    }
});

passwordInput.addEventListener('paste', function (e) {
    e.preventDefault();
    const text = (e.clipboardData || window.clipboardData).getData('text');
    actual += text;
    clearTimeout(revealTimer);
    render(false);
});

eyeIcon.addEventListener('click', function () {
    revealed = !revealed;
    clearTimeout(revealTimer);
    this.classList.toggle('bi-eye', !revealed);
    this.classList.toggle('bi-eye-slash', revealed);
    render(false);
    passwordInput.focus();
});

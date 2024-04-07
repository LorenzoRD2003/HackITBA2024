// ex2.js

document.addEventListener('DOMContentLoaded', function() {
    const verifyButton = document.querySelector('button[type="button"]');
    verifyButton.addEventListener('click', function() {
        location.reload();
    });
});

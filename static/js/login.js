/**
 * @fileoverview Description of this file.
 */

const form = document.getElementById('loginForm');

form.addEventListener('submit', (event) => {
  // Save the values to localStorage
  event.preventDefault();

  fetch(form.action, {
    method: 'POST',
    body: new FormData(form)  // Send form data
  })
      .then(response => {
        if (response.ok) {
          window.location.href = '/';
        } else {
          console.error(response);
        }
      })
      .catch(error => {
        console.error('Error during form submission:', error);
      });
});

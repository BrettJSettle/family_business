/**
 * @fileoverview Description of this file.
 */

const form = document.getElementById('joinForm');

form.addEventListener('submit', (event) => {
  // Save the values to localStorage
  event.preventDefault();

  fetch(form.action, {
    method: 'POST',
    body: new FormData(form)  // Send form data
  })
      .then(response => {
        if (response.ok) {
          // Redirect on success
          window.location.href = '/';
          //   window.location.href = '/game';
        } else {
          // Handle errors if needed
          console.error('Form submission failed');
        }
      })
      .catch(error => {
        console.error('Error during form submission:', error);
      });
});

window.addEventListener('load', () => {});
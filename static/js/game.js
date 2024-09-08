/**
 * @fileoverview JS methods for Family Business.
 */

/**
 * Updates the hit list with the given data.
 * @param {!Array<!Object>} hitListData The data to display.
 */
function updateHitList(hitListData) {
  const hitListDiv = document.getElementById('hit-list');
  hitListDiv.innerHTML = ''; // Clear previous images

  for (const card of hitListData) {
      const img = document.createElement('img');
      img.src = card.imageUrl; // Assuming your card data has an imageUrl property
      img.alt = card.name;
      hitListDiv.appendChild(img);
  }
}

function updatePlayers(playerData) {
  const hitListDiv = document.getElementById('player-list');
  hitListDiv.innerHTML = ''; // Clear previous images

  for (const card of hitListData) {
      const img = document.createElement('img');
      img.src = card.imageUrl; // Assuming your card data has an imageUrl property
      img.alt = card.name;
      hitListDiv.appendChild(img);
  }
}
function checkGameReady() {
  fetch("/game/test/state")
    .then(response => response.json())
    .then(data => {
      if (!data.ready) {
        // Create the modal elements
        const modal = document.getElementById('ready-modal');
        modal.style.display = 'block';

        const readyButton = document.getElementById('readyButton');
        // Add an event listener to the button (you'll need to implement the actual ready logic)
        readyButton.addEventListener('click', () => {
          // ... your logic to send a ready signal to the server ...
          modal.remove(); // Close the modal
        });
      }
    })
    .catch(error => {
      console.error('Error fetching game state:', error);
      // Handle the error gracefully, perhaps display an error message to the user
    });
}

window.addEventListener('load', () => {
  checkGameReady();
  let lobby = localStorage.getItem("lobby");
  let header_text = document.getElementById("game-header-text");
  header_text.innerText = "Game: " + lobby;
    // Example 1: Fetching data from a local JSON file
  fetch('/game/' + lobby + '/state') 
      .then(response => response.json())
      .then(data => {
          console.log("Data from JSON file:", data);
          // Process the fetched data here
      })
      .catch(error => console.error('Error fetching JSON:', error));

  // Example 2: Making a GET request to a local API endpoint
  // fetch('/api/hitlist') 
  //     .then(response => response.json())
  //     .then(data => {
  //     //     if (!response.ok) {
  //     //         throw new Error('Network response was not ok');
  //     //     }
  //     //     return response.json(); 
  //     // })
  //     // .then(profileData => {
  //         console.log("User profile data:", data);
  //         // Update the webpage with the profile data
  //     })
  //     .catch(error => console.error('Error fetching profile:', error));
});
// Define a function to fetch a word from the API
function getWord() {
    fetch('/give-word', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response data, which contains the word
        const word = data.sentence;
        console.log('Received word:', word);
  
        // You can use the word in your application here
        // For example, update the DOM to display the word
        document.getElementById('wordDisplay').textContent = word;
      })
      .catch((error) => {
        console.error('Error fetching word:', error);
      });
  }
  
  // Call the getWord function when your page loads or when an event triggers it
  // For example, you can call it when a button is clicked
  document.getElementById('getWordButton').addEventListener('click', getWord);
  
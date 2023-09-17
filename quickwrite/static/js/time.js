function startTimer() {
    let seconds = 15;
    const timerElement = document.getElementById('timer');
  
    function updateTimer() {
      if (seconds >= 0) {
        timerElement.textContent = seconds + ' seconds remaining';
        seconds--;
        setTimeout(updateTimer, 1000); // Call the function again after 1 second
      } else {
        timerElement.textContent = 'Time is up!';
      }
    }
  
    updateTimer(); // Start the timer
  }
  
  startTimer();
  
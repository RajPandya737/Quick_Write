function getOCRResult() {
  var canvas = document.getElementById("canvas");
  var imageBase64 = canvas.toDataURL("image/png");

  fetch("/get-ocr", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ image: imageBase64 }),
  })
    .then((response) => response.json())
    .then((data) => {
      var ocrResultElement = document.getElementById("ocrResult");
      ocrResultElement.innerText = "Guess: " + data.ocr;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function checkEqual() {
  getOCRResult();
  wordDisplay = document.getElementById("wordDisplay").innerHTML;
  ocrResult = document.getElementById("ocrResult").innerHTML.slice(7);
  console.log(wordDisplay)
  console.log(ocrResult)
  if (
    ocrResult.toLowerCase() === wordDisplay.toLowerCase() &&
    ocrResult != "�"
  ) {
    console.log("Match");
    score++;
    document.getElementById("score").innerHTML = "Score: " +score;
    resetCanvas()
  }
}

function resetCanvas() {
  // Clear the entire canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Fill the canvas with white color
  ctx.fillStyle = "white";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}


var score = 0; // Replace 42 with your actual score value
setInterval(function(){
  checkEqual(score)
}, 2000);

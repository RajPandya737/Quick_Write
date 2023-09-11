// ocr-script.js

// Function to send a POST request to /get-ocr
function getOCRResult() {
    // Get the canvas image data
    var canvas = document.getElementById("canvas");
    var imageBase64 = canvas.toDataURL("image/png");
  
    // Send the image data to the server
    fetch("/get-ocr", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ image: imageBase64 }),
    })
      .then((response) => response.json())
      .then((data) => {
        // Display the OCR result on the web page
        var ocrResultElement = document.getElementById("ocrResult");
        ocrResultElement.innerText = data.ocr;
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  function checkEqual () {
    getOCRResult()
    wordDisplay = document.getElementById("wordDisplay").innerHTML
    ocrResult = document.getElementById("ocrResult").innerHTML
    if (ocrResult.toLowerCase() === wordDisplay.toLowerCase() && ocrResult != "�"){
      console.log("Match")
    }
  }
  
  setInterval(checkEqual, 2000);
  
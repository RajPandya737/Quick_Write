const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

window.addEventListener("resize", function () {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
});

const mouse = {
  x: undefined,
  y: undefined,
  mode: 1,
};



canvas.addEventListener("mousedown", function (event) {
  mouse.x = event.clientX;
  mouse.y = event.clientY;
  mouse.isDrawing = true;
});

canvas.addEventListener("mouseup", function () {
  mouse.isDrawing = false;
});

canvas.addEventListener("mousemove", function (event) {
  if (mouse.isDrawing && mouse.mode === 1) {
    mouse.x = event.clientX;
    mouse.y = event.clientY;
    drawCircle();
  } else if (mouse.isDrawing && mouse.mode === 0) {
    mouse.x = event.clientX;
    mouse.y = event.clientY;
    eraseCircle();
  }
});

function drawCircle(x, y) {
  ctx.fillStyle = "black";
  ctx.beginPath();
  ctx.arc(mouse.x, mouse.y, 10, 0, Math.PI * 2);
  ctx.fill();
}

function eraseCircle(x, y) {
  ctx.fillStyle = "white";
  ctx.beginPath();
  ctx.arc(mouse.x, mouse.y, 10, 0, Math.PI * 2);
  ctx.fill();
}

function changeBrush() {
  if (mouse.mode === 1) {
    mouse.mode = 0;
  } else {
    mouse.mode = 1;
  }
  console.log(mouse.mode)
}

function save() {
  var canvas = document.getElementById("yourCanvasId");
  var imageDataUrl = canvas.toDataURL("image/png");
}

// Function to save the canvas drawing as an image on the server
function save() {
  const dataURL = canvas.toDataURL("image/png");
  fetch("/save-image", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ image: dataURL }),
  })
    .then((response) => {
      if (response.ok == false) {
        console.error("Failed to save image on the server.");
      }
    })
    .catch((error) => {
      console.error("Error while saving image:", error);
    });
}

// Call the saveDrawingOnServer function every second using setInterval
document.getElementById("changeBrush").addEventListener("click", changeBrush);
setInterval(save, 2000);

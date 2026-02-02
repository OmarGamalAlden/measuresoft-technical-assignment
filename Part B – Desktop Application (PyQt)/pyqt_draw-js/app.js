const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const shapeSelect = document.getElementById("shape");
const colorInput = document.getElementById("color");
const clearBtn = document.getElementById("clear");

let start = null;
let end = null;
let isDrawing = false;

let shape = "line";
let color = "#000000";

// mouse down
canvas.addEventListener("mousedown", (e) => {
  start = { x: e.offsetX, y: e.offsetY };
  end = null;
  isDrawing = true;
});

// mouse move
canvas.addEventListener("mousemove", (e) => {
  if (!isDrawing) return;

  end = { x: e.offsetX, y: e.offsetY };
  redraw();
});

// mouse up
canvas.addEventListener("mouseup", (e) => {
  if (!isDrawing) return;

  end = { x: e.offsetX, y: e.offsetY };
  redraw();

  // stop drawing after mouse release
  isDrawing = false;
  start = null;
  end = null;
});

// draw current shape
function redraw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  if (!start || !end) return;

  const x1 = start.x;
  const y1 = start.y;
  const x2 = end.x;
  const y2 = end.y;

  ctx.beginPath();
  ctx.strokeStyle = color;
  ctx.lineWidth = 2;

  if (shape === "line") {
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
    return;
  }

  const x = Math.min(x1, x2);
  const y = Math.min(y1, y2);
  const w = Math.abs(x2 - x1);
  const h = Math.abs(y2 - y1);

  if (shape === "rect") {
    ctx.strokeRect(x, y, w, h);
  }

  if (shape === "ellipse") {
    ctx.beginPath();
    ctx.strokeStyle = color;
    ctx.ellipse(x + w / 2, y + h / 2, w / 2, h / 2, 0, 0, Math.PI * 2);
    ctx.stroke();
  }
}

// controls
shapeSelect.addEventListener("change", () => {
  shape = shapeSelect.value;
});

colorInput.addEventListener("change", () => {
  color = colorInput.value;
  console.log("Selected color:", color);
});

clearBtn.addEventListener("click", () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  start = null;
  end = null;
  isDrawing = false;
});

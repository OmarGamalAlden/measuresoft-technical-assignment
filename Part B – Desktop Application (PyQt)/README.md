---

# 📄 README — Part B

## Desktop Application (PyQt)

**Folder:** `Part B – Desktop Application (PyQt)`

### Project Structure

```
Part B – Desktop Application (PyQt)/
│
├─ pyqt_draw-py/
│   ├─ canvas.py
│   ├─ main.py
│
├─ pyqt_draw-js/
│   ├─ index.html
│   ├─ app.js
│   ├─ style.css
├─ README.md
```

---

### Overview

This task is a simple desktop drawing application that allows the user
to draw basic shapes using the mouse.

The same idea was implemented twice:

- Once using **Python (PyQt)**
- Once using **JavaScript (HTML Canvas)**

The focus of this task is understanding **mouse events and drawing logic**,
not building a complex UI.

---

### Features

- Draw line, rectangle, and ellipse
- Mouse-based drawing (click, drag, release)
- Change drawing color
- Clear the canvas

---

### Python Version (PyQt)

- Uses PyQt widgets
- Handles mouse press, move, and release events
- Drawing is done using `QPainter`

### JavaScript Version

- Uses HTML `<canvas>`
- Handles `mousedown`, `mousemove`, `mouseup`
- Drawing is done using Canvas 2D context

---

### How to Run

**Python version**

```bash
python main.py
```

**JavaScript version**

- Open `index.html` in the browser

---

### Notes

- The goal was logic clarity, not advanced UI
- Both versions follow the same drawing flow
- Code was kept simple and readable

---

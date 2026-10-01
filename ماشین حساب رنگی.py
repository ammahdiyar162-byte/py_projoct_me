from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QGridLayout
)
import sys

#rang ha 
style_map = {
    "numbers": {"base": "#dfe6e9", "hover": "#b2bec3", "pressed": "#636e72"},
    "ops":     {"base": "#fab1a0", "hover": "#e17055", "pressed": "#d63031"},
    "clear":   {"base": "#ff7675", "hover": "#d63031", "pressed": "#b71c1c"}
}

#rang dokme haye dige 
button_config = {
    "7": "numbers", "8": "numbers", "9": "numbers", "/": "ops",
    "4": "numbers", "5": "numbers", "6": "numbers", "*": "ops",
    "1": "numbers", "2": "numbers", "3": "numbers", "-": "ops",
    "0": "numbers", ".": "numbers", "C": "clear",   "+": "ops"
}

#barname asli

app = QApplication(sys.argv)
win = QWidget()
win.resize(300, 420)
win.setWindowTitle("ماشین حساب ")

grid = QGridLayout()

display = QLineEdit()
display.setFixedHeight(50)
display.setStyleSheet("font-size: 24px; padding: 5px; border: 1px solid #b2bec3;")
grid.addWidget(display, 0, 0, 1, 4)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"]
]

for r in range(4):
    for col in range(4):
        tx = buttons[r][col]
        buton = QPushButton(tx)
        

        style_key = button_config.get(tx, "numbers")
        colors = style_map.get(style_key)
        

        buton.setStyleSheet(f"""
            QPushButton {{
                font-size: 20px;
                padding: 17px;
                background-color: {colors['base']};
                border-radius: 8px;
                border: 1px solid #b2bec3;
            }}
            QPushButton:hover {{
                background-color: {colors['hover']};
            }}
            QPushButton:pressed {{
                background-color: {colors['pressed']};
                border: 2px solid #2d3436;
            }}
        """)
        
        grid.addWidget(buton, r + 1, col)


btn_equal = QPushButton("=")
btn_equal.setStyleSheet("""
    QPushButton {
        font-size: 20px; padding: 10px; background-color: #74b9ff; border-radius: 8px;
    }
    QPushButton:hover { background-color: #0984e3; }
    QPushButton:pressed { background-color: #0984e3; border: 2px solid #000; }
""")
grid.addWidget(btn_equal, 5, 0, 1, 4)

win.setLayout(grid)
win.show()
sys.exit(app.exec())

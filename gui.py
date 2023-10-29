from PIL import ImageTk, Image, ImageDraw
import tkinter as tk
import numpy as np
from tensorflowTesting import testing

# Constants
classes=[0,1,2,3,4,5,6,7,8,9]
width = 500
height = 500
center = height//2
white = (255, 255, 255)
green = (0,128,0)
window_width = 720  # Set the window width
window_height = 720  # Set the window height
font_size = 14  # Adjust font size



def paint(event):
    x1, y1 = (event.x - 10), (event.y - 10)
    x2, y2 = (event.x + 10), (event.y + 10)
    cv.create_oval(x1, y1, x2, y2, fill="black",width=40)
    draw.line([x1, y1, x2, y2],fill="black",width=40)

# Function to make predictions
def model():
    filename = "image.png"
    image1.save(filename)
    pred = testing()
    predicted_class = classes[np.argmax(pred[0])]
    accuracy = round(pred[0][np.argmax(pred[0])] * 100, 3)
    result_text = f"{predicted_class}\nAccuracy: {accuracy}%"
    txt.delete('1.0', tk.END)
    txt.insert(tk.INSERT, result_text)

# Function to clear the canvas and text
def clear():
    cv.delete('all')
    draw.rectangle((0, 0, width, height), fill=(255, 255, 255, 0))
    txt.delete('1.0', tk.END)

# Create the main window
root = tk.Tk()
root.geometry(f"{window_width}x{window_height}")
root.resizable(1, 1)
root.configure(bg='lightblue')
root.resizable(0,0)
# Set the heading label
heading_label = tk.Label(root, bd=0, bg='lightgray', font=f'Helvetica {font_size} bold', height=1, text="Handwritten Digit Recognition")
heading_label.pack()

# Create the canvas
cv = tk.Canvas(root, width=width, height=height, bg='lightgray')
cv.pack()

# Create the image and drawing object
image1 = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image1)

# Create the text widget
txt = tk.Text(root, bd=3, exportselection=0, bg='palegoldenrod', font=f'Helvetica {font_size}', padx=10, pady=10, height=5, width=20)
txt.pack()

# Bind events to the canvas
cv.pack(expand=tk.YES, fill=tk.BOTH)
cv.bind("<B1-Motion>", paint)

# Create buttons
btnModel = tk.Button(text="Predict", command=model, bg='lightgray')
btnClear = tk.Button(text="Clear", command=clear, bg='lightgray')

btnModel.pack()
btnClear.pack()
txt.pack()

root.title('HandWritten Digit Recognition')
root.mainloop()

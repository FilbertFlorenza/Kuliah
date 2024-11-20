#Made by Shelinna
import tkinter as tk

def x_loop():
    global x
    if x > 20:  
        x = 1
    label.config(text=str(x))  
    
   
    color = f"#{(x * 10) % 256:02x}{(x * 20) % 256:02x}{(x * 30) % 256:02x}"
    root.config(bg=color)  

    
    label.config(bg=color)  

 
    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
    brightness = (r * 299 + g * 587 + b * 114) / 1000  
    if brightness < 128:  
        text_color = "white"
    else:  
        text_color = "black"
    
   
    label.config(fg=text_color)

    x += 1  
    root.after(1000, x_loop) 

x = 1  # Start from 1
root = tk.Tk()


label = tk.Label(root, text=str(x),font="Arial", bg="white", fg="black", width=5, height=2)
label.pack(pady=20)

x_loop()  

root.mainloop()

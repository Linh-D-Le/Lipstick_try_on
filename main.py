from tkinter import *
from PIL import Image, ImageTk
import glob
from tkinter import filedialog
from tkinter.filedialog import askopenfile

root = Tk()
root.title("Let's try lipstick on!")
root.iconbitmap("lipstick_icon.ico")

app_width = 700
app_height = 700

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - app_width)/2
y = (screen_height - app_height)/2
# Set the window to screen's center
root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

# Set background image for window
bg = Image.open("background.png")
bg = ImageTk.PhotoImage(bg.resize((app_width,app_height), Image.ANTIALIAS))
bg_canvas = Canvas(root)
bg_canvas.pack(fill="both", expand=True)
bg_canvas.create_image(0,0, image=bg, anchor="nw")

# Create lipsticks image list
lipsticks = []
lipsticks_name = ["Floral", "Glacier", "Juniper", "Maple", "Musk", "Rainforest", "Shore"]
for lipstick in glob.glob("lipstick_images/*.jpg"):
    lipsticks.append(lipstick)

lipstick_label = Label(root)
lipstick_label.place(x=300, y=0)

count = -1
def switch(i):
    lipstick = lipsticks[i]
    image = Image.open(lipstick)
    pic = ImageTk.PhotoImage(image.resize((150, 200), Image.ANTIALIAS))
    lipstick_label.configure(image=pic, text=lipsticks_name[i], compound=TOP, font=("Halvetica", 10), fg="red")
    lipstick_label.image = pic

def next():
    global count
    if count == (len(lipsticks)-1):
        switch(0)
        count = 0
    else:
        switch(count+1)
        count += 1
    root.after(2000, next)
next()

shade_frame = Frame(root)
shade_frame.place(x=15, y=230)

# Create label for shades
shades = []
for shade in glob.glob("shades/*.jpg"):
    shades.append(shade)
for shade in glob.glob("shades/*.png"):
    shades.append(shade)

def show_shade(i):
    shade_img = Image.open(shades[i])
    shade_img = ImageTk.PhotoImage(shade_img.resize((80,40), Image.ANTIALIAS))
    shade_label = Label(shade_frame, image=shade_img)
    shade_label.image = shade_img
    return (shade_img)

def upload():
    try:
        f_types = [("Jpg Files", "*.jpg"),("PNG Files","*.png"), ("JPEG Files","*.jpeg")]  
        root.filename = filedialog.askopenfilename(title="Uploading a photo", filetypes=f_types)
        uploading_img = Image.open(root.filename)
        uploading_img = ImageTk.PhotoImage(uploading_img.resize((300,300), Image.ANTIALIAS))
        uploading_img_label.image = uploading_img
        test_canvas.create_image(40,10, anchor=NW, image=uploading_img)
        test_canvas.lower(uploading_img)
    except AttributeError:
        uploading_img_label.configure(text="Please upload a photo!", fg="white")

def button_click(s):
    if s == shades[0]:
        test_shade = Image.open(r"samples/floral.jpg")
    elif s == shades[1]:
        test_shade = Image.open(r"samples/glacier.jpg")
    elif s == shades[2]:
        test_shade = Image.open(r"samples/juniper.jpg")
    elif s == shades[3]:
        test_shade = Image.open(r"samples/maple.jpg")
    elif s == shades[4]:
        test_shade = Image.open(r"samples/musk.jpg")
    elif s == shades[5]:
        test_shade = Image.open(r"samples/rainforest.jpg")
    elif s == shades[6]:
        test_shade = Image.open(r"samples/shore.jpg")

    test_canvas.image = ImageTk.PhotoImage(test_shade.resize((50,50), Image.ANTIALIAS))
    my_test_shade = test_canvas.create_image(160, 150, anchor=NW, image=test_canvas.image)

    def left(event):
        x = -20
        y = 0
        test_canvas.move(my_test_shade, x, y)
    
    def right(event):
        x = 20
        y = 0
        test_canvas.move(my_test_shade, x, y)

    def up(event):
        x = 0
        y = -20
        test_canvas.move(my_test_shade, x, y)

    def down(event):
        x = 0
        y = 20
        test_canvas.move(my_test_shade, x, y)

    root.bind("<Left>", left)
    root.bind("<Right>", right)
    root.bind("<Up>", up)
    root.bind("<Down>", down)

for i in range(len(shades)):
    show_shade(i)
    shade_button0 = Button(shade_frame, image=show_shade(0), command= lambda:button_click(shades[0]))
    shade_button1 = Button(shade_frame, image=show_shade(1), command= lambda:button_click(shades[1]))
    shade_button2 = Button(shade_frame, image=show_shade(2), command= lambda:button_click(shades[2]))
    shade_button3 = Button(shade_frame, image=show_shade(3), command= lambda:button_click(shades[3]))
    shade_button4 = Button(shade_frame, image=show_shade(4), command= lambda:button_click(shades[4]))
    shade_button5 = Button(shade_frame, image=show_shade(5), command= lambda:button_click(shades[5]))
    shade_button6 = Button(shade_frame, image=show_shade(6), command= lambda:button_click(shades[6]))

    shade_button0.grid(row=1, column=0, padx=5, pady=5)
    shade_button1.grid(row=1, column=1, padx=5, pady=5)
    shade_button2.grid(row=1, column=2, padx=5, pady=5)
    shade_button3.grid(row=1, column=3, padx=5, pady=5)
    shade_button4.grid(row=1, column=4, padx=5, pady=5)
    shade_button5.grid(row=1, column=5, padx=5, pady=5)
    shade_button6.grid(row=1, column=6, padx=5, pady=5)

test_canvas = Canvas(root)
test_canvas.place(x=20, y=300)
test_canvas.create_text(195, 120, text="Your photo here", font=("Helvetica",20), fill="silver")

# Make label of updated photo appeared in front of test_canvas
label_frame = LabelFrame(test_canvas)
uploading_img_label = Label(label_frame)
uploading_img_label.place(x=0, y=0)

test_canvas.create_window(100, 100, window=label_frame, anchor="w")

# Label for instructions
instruction_label = Label(root, 
                        text="- Upload your photo\n- Choose a shade\n- Use arrow keys to move shade",
                        font=("Helvetica", 10), fg="red", bg="#f1d2ce")
instruction_label.place(x=510, y=500)


my_btn = Button(root, text="Upload a photo", font=("Halvetica",10), fg="green", bg="yellow", command=upload)
my_btn.place(x=165, y=310)

root.mainloop()
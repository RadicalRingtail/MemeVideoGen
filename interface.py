from video import *
from tkinter import *
from tkinter import filedialog, messagebox
import random, string, config

window = Tk()
window.title('Meme Video Gen (v0.1)') 
window.resizable(False, False)

v = StringVar()
v.set('Current video source directory: \n' + config.folder)
directory_label = Label(textvariable=v)

def open_directory():
    directory = filedialog.askdirectory(parent=window, title='Choose a folder of videos to import...')
    config.folder = str(directory)
    v.set('Current video source directory: \n' + config.folder)

button1 = Button(text='Open', command=open_directory)

param_label1 = Label(text='min clip length')
param1 = Entry(window, width=3)
param1.insert(0, config.min_clip_length)

param_label2 = Label(text='max clip length')
param2 = Entry(window, width=3)
param2.insert(0, config.max_clip_length)

param_label3 = Label(text='width')
param3 = Entry(window, width=4)
param3.insert(0, config.width)

param_label4 = Label(text='height')
param4 = Entry(window, width=4)
param4.insert(0, config.height)

param_label5 = Label(text='Frame Rate')
param5 = Entry(window, width=2)
param5.insert(0, config.fps) 

directory_label.grid(row=0, column=0, columnspan=4)
button1.grid(row=1, column=1)

param_label1.grid(row=2, column=0)
param1.grid(row=2, column=1)
param_label2.grid(row=3, column=0)
param2.grid(row=3, column=1)
param_label3.grid(row=4, column=0)
param3.grid(row=4, column=1)
param_label4.grid(row=4, column=2)
param4.grid(row=4, column=3)
param_label5.grid(row=5, column=0)
param5.grid(row=5, column=1)

def create_video():
    config.max_clip_length = float(param1.get())
    config.min_clip_length = float(param2.get())
    config.width = int(param3.get())
    config.height = int(param4.get())
    config.fps = int(param5.get())

    print(config.max_clip_length + config.min_clip_length)

    import_clips()
    title = ''.join(random.choice(string.ascii_letters) for i in range(10))
    make_new_video(title)
    messagebox.showinfo(title='Done!', message='Video generated successfully!')

button2 = Button(text='Generate video', command=create_video)
button2.grid(row=6, column=1)

window.mainloop()


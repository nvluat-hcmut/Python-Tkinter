from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import  *
from tkinter import ttk
import  _thread
from pytube import YouTube

window = Tk()
window.geometry("490x180")
window.title("Youtube Downloader")
window.resizable(False, False)
window.configure(bg='white')

direct = ""
def open_path():
    global direct 
    direct = filedialog.askdirectory()
    entry_path.set(direct)
    if len(direct) == 0:
        msb_path = messagebox.showwarning('warning', 'Please insert path!')
    else:
        pass

def show_progress_bar(stream, chunk, bytes_remaining):
    progress = int (((stream.filesize - bytes_remaining)/stream.filesize)*100)


def Download():
    url = link_entry.get()
    Selected = cbb_types.get()
    if len(url) == 0:
        msb_path = messagebox.showwarning('warning', 'Please insert path!')
    else:
        pass
    Yt = YouTube(url, on_progress_callback = show_progress_bar)
    if(Selected == options[0]):
        typ = Yt.streams.get_highest_resolution()
    elif(Selected == options[1]):
        typ = Yt.streams.filter(progressive = True, file_extension = ". mp4").first()
    elif(Selected == options[2]):
        typ = Yt.streams.filter(only_audio = True).first()

    typ.download(direct)
    label_status.config(text = "Video Downloader")

    name = typ.title
    size = typ.filesize/1024000
    size = round (size, 1)
    tb_filename.insert(0.0, "Video name: \n" + name + "\n Video file : \n" + str(size) + "MB\n")



def expand_window():
    window.geometry("490x320")

def shorten_window():
    window.geometry("490x180")

# Add image
image = PhotoImage(file="img1.png")
label_image = Label(image=image)
label_image.place(x = 0, y = 92)



# Label youtube url
link = Label(window, text = "Youtube URL", background = 'white', foreground = 'black', font = 'arial 10')
link.place(x = 20, y = 10)

# Entry nhap link youtube
entry_url = StringVar()
link_entry = Entry(window, width = 52, textvariable = entry_url)
link_entry.place(x = 130, y = 10)

# Label duong dan
path = Label(window, text = "Output Directory", background = 'white', foreground = 'black', font = 'arial 10')
path.place(x = 20, y = 40)

# Entry nhap link dia chi tai ve
entry_path = StringVar()
link_path = Entry(window, width = 52, textvariable = entry_path)
link_path.place(x = 130, y = 40)

# Button brower
btn_brower = Button(window, width = 10, text = "Brower", command = open_path)
btn_brower.place(x = 380, y = 38)

# Label che do tai
Download_type = Label(window, text = "Download type", background = 'white', foreground = 'black', font = 'arial 10')
Download_type.place(x = 20, y = 70)

# ComboBox chat luong video
options = ["High quality Video", "Low quality Video", "Audio"]
cbb_types = ttk.Combobox(window, values = options, width = 22)
cbb_types.current(0)
cbb_types.place(x = 130, y =70)

# Label Status
label_status = Label(window, text = "", background = 'white', foreground = 'black', font = 'arial 10')
label_status.place(x = 300, y = 70)

# Thanh tien trinh
bar = ttk.Progressbar(window, length = 320)
# bar.place(x = 130, y = 110)

# Button DownLoad
btn_download = Button(window, width = 10, text = "Download", command = lambda:_thread.start_new_thread(Download,()))
btn_download.place(x = 170, y = 120)

# Button Expand
btn_expand = Button(window, width = 10, text = "Expand", command = expand_window)
btn_expand.place(x = 303, y = 120)

# Button Shorten
btn_shorten = Button(window, width = 10, text = "Shorten", command = shorten_window)
btn_shorten.place(x = 380, y = 120)

# Textbox ten va kich thuoc file
tb_filename = Text(window ,width = 45, height = 6, font = 'arial 10')
tb_filename.insert(0.0,"Programmed by Mr Law \n")
tb_filename.place(x = 130, y = 190)




window.mainloop()
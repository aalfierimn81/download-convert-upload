import tkinter 
import os
import tkinter.ttk

class pyYTDownload:
    def __init__(self, root):
        yt.geometry(f"{600}x{300}")
        self.yt_path = "/home/andrea/Scrivania/temp/youtube/"

        self.filelabelText = "Link:"
        self.filelabel = tkinter.Label (root, text=self.filelabelText)
        self.filelabel.place(x=120, y=20)

        self.fileentry = tkinter.Entry(root, width=50)
        self.fileentry.place(x=200, y=20)
        
        self.start_download_button = tkinter.Button(root, text="Download", command=self.__ytdownload)
        self.start_download_button.place(x=120, y=110)

        self.close_button = tkinter.Button(root, text="Close", command=self.__close, state=tkinter.DISABLED)
        self.close_button.place(x=120, y=150)

    def __ytdownload (self):
        CMD = "yt-dlp "
        command = CMD + self.fileentry.get()
        os.chdir(self.yt_path)
        os.system(command)
        self.close_button['state'] = tkinter.NORMAL
    
    def __close(self):
        yt.destroy()

yt = tkinter.Tk()
appyt = pyYTDownload (yt)
yt.title("Youtube download")
yt.mainloop()
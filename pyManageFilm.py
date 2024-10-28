import tkinter 
import os
import tkinter.ttk

class pyMagageFilm:
    def __init__(self, root):
        root.geometry(f"{600}x{300}")
        
        self.select_option_1 = tkinter.Button(root, text="1. Convert for chromecast", command=self.__convert)
        self.select_option_1.place(x=40, y=20)
        
        self.select_option_2a = tkinter.Button(root, text="2. Upload for chromecast", command=self.__upload)
        self.select_option_2a.place(x=40, y=80)

        self.select_option_3 = tkinter.Button(root, text="3. Youtube download", command=self.__youtubedownload)
        self.select_option_3.place(x=40, y=140)

        self.select_option_c = tkinter.Button(root, text="Close", command=self.__destroy)
        self.select_option_c.place(x=40, y=200)

    def __convert(self):
        CMD = "python3 pyManage/pyConvert.py"
        os.system(CMD)
    
    def __upload(self):
        CMD = "python3 pyManage/pyUpload.py"
        os.system(CMD)
    
    def __youtubedownload(todo):
       CMD = "python3 pyManage/pyYTDownload.py"
       os.system(CMD)
    
    def __destroy(self):
        root.destroy()


# Create the root window
root = tkinter.Tk()

# Create the image browser and start the main loop
app = pyMagageFilm(root)
root.title("Film Manager")
root.mainloop()


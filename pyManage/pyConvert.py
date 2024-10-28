import tkinter 
from tkinter import Label
from tkinter import filedialog
import os

class pyConvert:
    def __init__(self, root):
        convert.geometry(f"{600}x{300}")
        self.chromecast_path = "/home/andrea/Scrivania/temp/chromecast/"
        self.initdir = "/home/andrea/Scrivania/temp"
        self.root_dir = os.getcwd()
        self.select_file_button = tkinter.Button(root, text="Select File", command=self.__selectfile)
        self.select_file_button.place(x=120, y=10)

        self.filelabelText = "File:"
        self.filelabel = tkinter.Label (root, text=self.filelabelText)
        self.filelabel.place(x=120, y=60)

        self.fileentry = tkinter.Entry(root, width=50)
        self.fileentry.place(x=200, y=60)
        self.fileentry.config(state=tkinter.DISABLED)
        
        self.start_conversion_button = tkinter.Button(root, text="Start", command=self.__handbrakeconvert, state=tkinter.DISABLED)
        self.start_conversion_button.place(x=120, y=110)

        self.close_button = tkinter.Button(root, text="Close", command=self.__destroy, state=tkinter.DISABLED)
        self.close_button.place(x=120, y=160)

    def __selectfile(self):
        self.filename = filedialog.askopenfile(initialdir=self.initdir)
        self.fileentry.config(state=tkinter.NORMAL)
        self.fileentry.insert(0, self.filename.name)
        self.start_conversion_button['state'] = tkinter.NORMAL
        self.fileentry.config(state=tkinter.DISABLED)
        
    
    def __handbrakeconvert(self):
        CMD1 = "HandBrakeCLI -i " #$filename
        CMD2 = " -o " # $output
        CMD3= " -Z \"Chromecast 1080p60 Surround\" "
        #input = str(self.filename.name).replace(' ','_')
        #os.rename (self.filename.name, input)
        o1 = self.filename.name.split('/')
        output = o1[-1]
        o2 = output.split('.')
        outputname = o2[0]
        command = CMD1 + self.filename.name + CMD2 + self.chromecast_path + outputname + ".mkv" + CMD3
        #command = CMD1 + input + CMD2 + self.chromecast_path + outputname + ".mkv" + CMD3
        os.system(command)
        self.close_button['state'] = tkinter.NORMAL

    def __destroy(self):
        convert.destroy()

convert = tkinter.Tk()
appconvert = pyConvert (convert)
convert.title("Conversione")
convert.mainloop()
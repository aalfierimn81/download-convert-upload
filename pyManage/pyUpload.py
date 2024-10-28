
import tkinter 
from tkinter import Label
from tkinter import filedialog
import tkinter.ttk
import ftplib

class pyUpload:
    def __init__(self, root):
        upload.geometry(f"{600}x{300}")
        self.chromecast_path = "/home/andrea/Scrivania/temp/chromecast/"
        self.select_file_button = tkinter.Button(root, text="Select File", command=self.__selectfile)
        self.select_file_button.place(x=120, y=10)

        self.filelabelText = "File:"
        self.filelabel = tkinter.Label (root, text=self.filelabelText)
        self.filelabel.place(x=120, y=60)

        self.fileentry = tkinter.Entry(root, width=50)
        self.fileentry.place(x=200, y=60)
        self.fileentry.config(state=tkinter.DISABLED)
        
        self.start_conversion_button = tkinter.Button(root, text="Transfer", command=self.__upload, state=tkinter.DISABLED)
        self.start_conversion_button.place(x=120, y=110)

        self.close_button = tkinter.Button(root, text="Close", command=self.__close, state=tkinter.DISABLED)
        self.close_button.place(x=120, y=150)

    def __selectfile(self):
        self.filename = filedialog.askopenfile(initialdir=self.chromecast_path)
        self.fileentry.config(state=tkinter.NORMAL)
        self.fileentry.insert(0, self.filename.name)
        self.start_conversion_button['state'] = tkinter.NORMAL
        self.fileentry.config(state=tkinter.DISABLED)

    def __upload(self):
        HOSTNAME='192.168.178.29'
        USERNAME='andsrv'
        PASSWORD='alF81@gross1'
        
        ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
        print("Connectiong...")
        ftp_server.cwd("hassio/media")
        print("Connected!")
        file = open(self.filename.name,'rb')               # file to send
        splits=self.filename.name.split('/')
        myfile=splits[-1]
        print("Transfer in progress...")
        ftp_server.storbinary('STOR '+myfile, file)        # send the file
        file.close()
        ftp_server.quit()
        print("Transfer complete")
        self.close_button['state'] = tkinter.NORMAL

    def __close(self):
        upload.destroy()

upload = tkinter.Tk()
appupload = pyUpload (upload)
upload.title("Upload")
upload.mainloop()
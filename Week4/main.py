'''
A user interface for users to be able to download youtube download
'''

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import pytube.exceptions as py_except


def main():
    root = tk.Tk()
    root.title("This is a youtube donwloader")
    root.geometry("800x400")
    root.columnconfigure(0, weight=1)

    # ytdLable
    ytdLable = tk.Label(root, text="Enter your URL")
    ytdLable.grid()

    # EnteryBox
    ytdEntryVar = tk.StringVar()
    ytdEntry = tk.Entry(root, width=50, textvariable=ytdEntryVar)
    ytdEntry.grid()

    # URL Error Msg
    ytdError = tk.Label(root, text="Error", fg='red')
    ytdError.grid()

    # savePath
    savePath = tk.Label(root, text="Save The File")
    savePath.grid()

    # Location Error Msg
    saveError = tk.Label(root, text="Location Error", fg='red')
    saveError.grid()

    # button save file
    saveEntry = tk.Button(
        root, bg='red', text='Choose Path', command=open_location(saveError))
    saveEntry.grid()

    # Type to download
    ytdQuality = tk.Label(root, text="Select Type")
    ytdQuality.grid()

    # Choices
    choices = ['720p', '144p', "Only Audio"]
    ytdChoices = ttk.Combobox(root, values=choices)
    ytdChoices.grid()

    # Download
    downloadbtn = tk.Button(root, text="Download",
                            command=download_video(ytdChoices, ytdEntry, ytdError, choices))
    downloadbtn.grid()

    # foorter
    footer = tk.Label(root, text="Created By Abuzer ALACA")
    footer.grid()

    root.mainloop()


def download_video(ytdChoices, ytdEntry, ytdError, choices):
    choice = ytdChoices.get()
    url = ytdEntry.get()
    print(url)

    if len(url) > 1:
        ytdError.config(text="", fg='green')
        try:
            yt = YouTube(url)
        except py_except.RegexMatchError:
            ytdError.config(
                text='This is not a valid youtube URL, Please enter a valid url')

        if choice == choices[0]:
            selected = yt.streams.filter(progressive=True).first()
        elif choice == choices[1]:
            selected = yt.streams.filter(
                progressive=True, file_extension='mp4').first()
        elif choice == choices[2]:
            selected = yt.streams.filter(
                only_audio=True, file_extension='mp4').first()
        else:
            ytdError.config(text='Url Tekrar Giriniz')

        selected.download()
    else:
        ytdError.config(text='Please, Enter a Valid URL', fg='red')


folder_name = ''


def open_location(saveError):
    ''' This func choses the file to where to save the files'''
    global folder_name

    folder_name = filedialog.askdirectory()
    if len(folder_name) > 1:
        saveError.config(text=folder_name, fg='green')
    else:
        saveError.config(text='Please, Choose a Path', fg='red')


if __name__ == "__main__":
    main()

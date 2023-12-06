import tkinter as tk
from tkinter import messagebox
import customtkinter
from pytube import YouTube
import os
def get_default_download_directory():
    home_directory = os.path.expanduser("~")  
    if os.name == 'posix':  
        return os.path.join(home_directory, 'Downloads')
    elif os.name == 'nt': 
        return os.path.join(home_directory, 'Downloads')
    else:
        return home_directory
default_download_directory = get_default_download_directory()
def startDownload():
    try:
        youtube_link = link.get()
        youtube_object = YouTube(youtube_link)

        selected_format = format_var.get()

        if selected_format == 'MP4':
            video_stream = youtube_object.streams.get_highest_resolution()
            video_stream.download()
            messagebox.showinfo("Download Completed", "Video downloaded successfully!")
        elif selected_format == 'MP3':
            audio_stream = youtube_object.streams.filter(only_audio=True).first()
            audio_stream.download()
            messagebox.showinfo("Download Completed", "Audio downloaded successfully!")
        video_stream.download(default_download_directory)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')
app = customtkinter.CTk()
app.geometry('356x224')
app.title('Youtube Downloader')

title = customtkinter.CTkLabel(app, text='Insert a YouTube link!')
title.pack(padx=10, pady=10)

link = customtkinter.CTkEntry(app, width=160)
link.pack(pady=10)

format_var = tk.StringVar(value='MP4')
mp4_radio = customtkinter.CTkRadioButton(app, text='MP4', variable=format_var, value='MP4')
mp3_radio = customtkinter.CTkRadioButton(app, text='MP3', variable=format_var, value='MP3')
mp4_radio.pack()
mp3_radio.pack()

download = customtkinter.CTkButton(app, text='Download', command=startDownload)
download.pack(padx=10, pady=10)
app.mainloop()

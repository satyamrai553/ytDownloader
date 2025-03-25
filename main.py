import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

def download_video():
    url = url_entry.get().strip()
    folder = folder_path.get()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return

    if not folder:
        messagebox.showerror("Error", "Please select a folder.")
        return

    ydl_opts = {
        'outtmpl': f"{folder}/%(title)s.%(ext)s",
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        'ffmpeg_location': r"C:\Program Files\ffmpeg-2025-03-24-git-cbbc927a67-essentials_build\bin",
        'merge_output_format': 'mp4',  # Ensure output is mp4
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            messagebox.showinfo("Success", f"Downloaded: {info['title']}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download: {str(e)}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

# Create GUI Window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x250")

# Input URL
tk.Label(root, text="Enter YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Select Folder
folder_path = tk.StringVar()
tk.Label(root, text="Save to:").pack(pady=5)
tk.Entry(root, textvariable=folder_path, width=40).pack(side=tk.LEFT, padx=5)
tk.Button(root, text="Browse", command=browse_folder).pack(side=tk.LEFT, padx=5)

# Download Button
tk.Button(root, text="Download Video", command=download_video, bg="green", fg="white").pack(pady=20)

root.mainloop()
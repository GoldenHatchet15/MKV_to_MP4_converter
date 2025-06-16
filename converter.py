import subprocess
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_mkv_to_mp4(file_path):
    if not file_path.endswith(".mkv"):
        messagebox.showerror("Invalid File", "Please select an MKV file.")
        return

    output_file = os.path.splitext(file_path)[0] + ".mp4"

    command = [
        "ffmpeg",
        "-i", file_path,
        "-c:v", "copy",
        "-c:a", "copy",
        output_file
    ]

    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", f"File converted successfully:\n{output_file}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Conversion failed:\n{e}")

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select MKV File",
        filetypes=[("MKV files", "*.mkv")]
    )
    if file_path:
        convert_mkv_to_mp4(file_path)

# GUI Setup
root = tk.Tk()
root.title("MKV to MP4 Converter")
root.geometry("300x150")

label = tk.Label(root, text="Convert MKV to MP4", font=("Helvetica", 14))
label.pack(pady=20)

button = tk.Button(root, text="Select File", command=select_file)
button.pack(pady=10)

root.mainloop()

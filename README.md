
# 🎥 MKV to MP4 Converter (Python + Tkinter + FFmpeg)

A simple Python GUI application that converts `.mkv` video files to `.mp4` using FFmpeg. Built with `Tkinter` so you can just click and convert — no command-line hassle!

---

## 🚀 Features

- Select `.mkv` files using a file browser
- Converts to `.mp4` using fast stream copy (no re-encoding)
- Works locally on Linux, WSL, and more with GUI support

---

## 🛠 Requirements

### ✅ System

- Python 3.6+
- FFmpeg installed and in your system path

### ✅ Python Dependencies

- Only standard libraries are used: `tkinter`, `os`, `subprocess`

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mkv-to-mp4-converter.git
cd mkv-to-mp4-converter
```

### 2. Install FFmpeg and Tkinter

#### On Ubuntu / WSL:

```bash
sudo apt update
sudo apt install ffmpeg python3-tk
```

#### On macOS (with Homebrew):

```bash
brew install ffmpeg
```

---

## 🖥️ How to Use

```bash
python3 mkv_to_mp4.py
```

1. A window will open.
2. Click **"Select File"**.
3. Choose a `.mkv` file.
4. The app will convert it to `.mp4` in the same folder.

---

## 🐧 WSL Note (Windows Subsystem for Linux)

If you're using WSL (especially on Windows 10), you'll need an X server like **VcXsrv** to view GUI apps. On Windows 11 with WSLg, GUI support is built-in.

---

## 📄 License

MIT License. Use it freely and modify to your needs!!!!

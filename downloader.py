import subprocess
import os
from config import DOWNLOAD_PATH

os.makedirs(DOWNLOAD_PATH, exist_ok=True)

def download_video(url, quality):
    filename = f"{DOWNLOAD_PATH}/video.%(ext)s"
    cmd = [
        "yt-dlp",
        "-f", f"bv*[height<={quality}]+ba/b",
        "--merge-output-format", "mp4",
        "-o", filename,
        url
    ]
    subprocess.run(cmd)
    return find_file()

def download_audio(url):
    filename = f"{DOWNLOAD_PATH}/audio.%(ext)s"
    cmd = [
        "yt-dlp",
        "-x", "--audio-format", "mp3",
        "-o", filename,
        url
    ]
    subprocess.run(cmd)
    return find_file()

def download_video_no_audio(url, quality):
    filename = f"{DOWNLOAD_PATH}/mute.%(ext)s"
    cmd = [
        "yt-dlp",
        "-f", f"bv*[height<={quality}]",
        "-o", filename,
        url
    ]
    subprocess.run(cmd)
    return find_file()

def find_file():
    files = os.listdir(DOWNLOAD_PATH)
    return os.path.join(DOWNLOAD_PATH, files[0])
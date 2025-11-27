import os
import yt_dlp

def download_yt_video(url):
    # Check empty URL
    if not url.strip():
        print("Error: No URL provided!")
        return

    # Download options
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'outtmpl': '%(title)s.%(ext)s',   # Auto filename
        'progress_hooks': [progress_hook],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("\nStarting download...")
            ydl.download([url])
            print("\nDownload completed successfully!")
    except Exception as e:
        print(f"Error: {e}")


# Progress bar
def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '').strip()
        speed = d.get('_speed_str', '')
        eta = d.get('eta', '')

        print(f"\r⬇ Downloading: {percent} | Speed: {speed} | ETA: {eta}s", end="")

    elif d['status'] == 'finished':
        print("\nDownload finished, now merging audio & video...")


if __name__ == "__main__":
    video_url = input("Paste Link here: ").strip()
    download_yt_video(video_url)

    print("\nSaved in folder:", os.getcwd())

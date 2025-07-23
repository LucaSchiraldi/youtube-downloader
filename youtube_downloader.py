from pytube import YouTube

def download_video(url, resolution="720p"):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4', res=resolution).first()

        if stream:
            print(f"Downloading: {yt.title}")
            stream.download()
            print("✅ Download complete!")
        else:
            print(f"No stream found with resolution {resolution}.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)

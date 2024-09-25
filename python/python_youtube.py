from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=KMsBnsIQuHs"

try:
    yt = YouTube(video_url)
    
    stream = yt.streams.get_highest_resolution()

    print("Downloading...")
    stream.download()

    print("Download complete!")

except Exception as e:
    print(f"An error occurred: {e}")

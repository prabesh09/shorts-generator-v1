from pytube import YouTube


def download_video(video_url):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        print("Downloading...")
        video_stream.download(output_path="./downloads", filename="downloaded.mp4")
        print("Download Completed!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

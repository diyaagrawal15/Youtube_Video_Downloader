from pytube import YouTube
link = "https://youtu.be/0U9-KUx0SD8"
youtube_1 = YouTube(link)
# print(youtube_1.title)
# print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("Enter the quality you need to download from the list: "))
videos[strm].download()
print("Successful")

# Playlist downloading extension
# from pytube import Playlist
# py = Playlist("https://www.youtube.com/playlist?list=PLu0W_9lII9aiS4rUVp2jXwIvCruo27sG6")
#
# print(f'Downloading:  {py.title}')
# for video in py.videos:
#     video.streams.first().download();
#

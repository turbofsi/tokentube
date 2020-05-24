from pytube import YouTube
from pytube import Playlist

ytd = YouTube('https://www.youtube.com/watch?v=LGzDEu7Sh5g&list=RDxoH29SM3e8I&index=12')
ytd.streams.filter().first().download()
# ytd.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

# play_list = Playlist('https://www.youtube.com/playlist?list=RDxoH29SM3e8I&pbjreload=10')

# for video in play_list:
#     print ('hello')
#     print (str(video.streams.filter(progressive=true)))
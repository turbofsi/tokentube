import moviepy.editor as mp

clip = mp.VideoFileClip("test1.mp4")
clip.audio.write_audiofile("少年.mp3")
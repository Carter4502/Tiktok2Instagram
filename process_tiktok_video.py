from moviepy.editor import *
from moviepy.video.fx.all import *
from os import listdir
from os.path import isfile, join
import random
from TikTokApi import TikTokApi
import string
import uuid

# Created by Carter Belisle
# Utilizing Unofficial Tiktok API and MoviePy

# Description: This program will download a video from an tiktok url, add audio to it from a folder of audio files,
# and then crop the video to fit the aspect ratio of an instagram post and output it to a folder of your choice.


PATH_TO_AUDIO = "" # path to folder of .mp3 audio files for your videos
OUTPUT_FILE_DIR = "" # path to folder to store videos
VERIFY_FP = "" # follow this tutorial to get your verifyFp https://medium.com/analytics-vidhya/download-tiktoks-with-python-dcbd79a5237f

def downloadTiktokVideo(link, name):
	did = ''.join(random.choice(string.digits) for num in range(19))
	api = TikTokApi.get_instance(custom_verifyFp=VERIFY_FP, custom_device_id=did)
	data = api.get_video_by_url(link)
	path_to_download = OUTPUT_FILE_DIR + "/{}.mp4".format(name)
	with open(path_to_download, 'wb') as output:
		output.write(data)
	return path_to_download 

def getRandomMusicFile(path):
	all_files = [f for f in listdir(path) if isfile(join(path, f))]
	return random.choice(all_files)

def overwriteAudio(video, audio):
	audio = audio.subclip(0, video.duration)
	audio_clip = CompositeAudioClip([audio])
	video.audio = audio_clip
	return video

def prepVideo(video_path, audio_path):
	video = VideoFileClip(video_path)
	audio = AudioFileClip(audio_path)
	video = overwriteAudio(video, audio)
	video = crop(video, x_center = video.w / 2, y_center = video.h / 2, width = video.w, height = video.w)
	return video

def download_crop_add_audio(link_to_video):
	file_name = str(uuid.uuid1().hex)
	downloaded_path = downloadTiktokVideo(link_to_video, file_name)
	audio = getRandomMusicFile(PATH_TO_AUDIO)
	video = prepVideo(downloaded_path, PATH_TO_AUDIO + "\\" + audio)
	video.write_videofile(OUTPUT_FILE_DIR + "/" + file_name + "_edited.mp4")

def main():
	while True:
		tiktok_link = input("Tiktok URL: ")
		download_crop_add_audio(tiktok_link)
		again = input("Would you like to do another? ")
		if (again.lower() == "yes" or again.lower() == "Y"):
				continue
		break

if __name__ == "__main__":
	main()

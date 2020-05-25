from moviepy.editor import *
from moviepy.video.fx.resize import resize
import os, random, pickle, config

videos = []
clips = []

#############
# functions #
#############

def import_clips():
    for file in os.listdir(config.folder):
        try:
            print('importing ' + file + '...')

            current_clip = VideoFileClip(str(config.folder + '/' + file))
            resize = current_clip.resize((config.width, config.height))
            videos.append(resize)

        except Exception as e:
            
            print('error importing clip ' + file + '(' + str(e) + ')')

"""    if os.path.exists('tmp'):
        pass
    else:
        os.mkdir('tmp')"""

def make_new_video(title):
    random.shuffle(videos)

    for clip in videos[0:config.amount_of_clips]:

        length = round(random.uniform(config.min_clip_length, config.max_clip_length), 2)

        if length >= clip.duration:
            length = round(random.uniform(0, clip.duration), 2)

        start = round(random.uniform(0,clip.duration - length), 2)
        print('start: ' + str(start) + '\n' + 'end: ' + str(length))

        clips.append(clip.subclip(start, start+length))

    video = concatenate_videoclips(clips, method='compose')
    video.write_videofile(title + ".mp4", temp_audiofile="temp-audio.m4a", 
                          remove_temp=True, codec="mpeg4", audio_codec="aac", fps=config.fps)

    clips.clear()
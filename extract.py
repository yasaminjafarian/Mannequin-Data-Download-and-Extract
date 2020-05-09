import cv2

import glob
import os.path
import numpy as np
import os
from os import listdir
from os.path import isfile, join

def get_mp4_filenames(dir):
    files = glob.glob(os.path.join(dir, '*.mp4'))
    return files

def get_time_steps(frame_file):
    mat = np.genfromtxt(frame_file, delimiter=" ")
    time_steps_micSec = mat[...,0]
    time_steps_milSec = time_steps_micSec/1000
    if not np.shape(time_steps_milSec):
        num_of_time_steps = 0
    else:
        num_of_time_steps = np.shape(time_steps_milSec)[0]

    return time_steps_milSec, num_of_time_steps

num_of_frames = 750
for f in range(0,num_of_frames):
    print('processing frame number %5d from %5d files' % (f, num_of_frames))
    path = '../data/'+str(f)+'/'
    files = get_mp4_filenames(path)
    if len(files) > 0:
        frames_dir = path + 'frames/'
        if not os.path.isdir(frames_dir):
            os.mkdir(frames_dir)
        video_path = files[0]
        time_steps_milSec, num_of_time_steps = get_time_steps(path + 'frames.txt')

        for TS in range(num_of_time_steps):
            time_step = time_steps_milSec[TS]
            vidcap = cv2.VideoCapture(video_path)
            vidcap.set(cv2.CAP_PROP_POS_MSEC, time_step)
            success, image = vidcap.read()
            if success:
                cv2.imwrite(frames_dir+str(TS)+".jpg", image)
            else:
                print("couldn't write the image on TS %3d"%(TS))




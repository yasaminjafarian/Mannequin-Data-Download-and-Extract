# Mannequin-Data-Download

This is a python implementation of downloading and extracting the videos for mannequin paper (https://arxiv.org/pdf/1904.11111.pdf)

## download txt files
1. download the mannequin dataset from here (https://google.github.io/mannequinchallenge/www/download.html)
2. extract the files in a directory (e.g. ~/MannequinChallenge)

## download videos
1. I use pytube3 for downloading the videos. more information at (https://towardsdatascience.com/the-easiest-way-to-download-youtube-videos-using-python-2640958318ab)

2. Install pytube3 for python3:
- $ pip install pytube3

3. make a folder code in the extracted directory each folder and put the download.py there (e.g. ~/MannequinChallenge/train/code/download.py)

4. run the download.py:
- $ python download.py

5. your data will be downloaded in data folder in extracted directory (e.g. ~/MannequinChallenge/train/data/)
each folder in the data directory represent each txt file.

## extract the frames
1. once you downloaded the videos from youtube, you should extract the frames for each video based on the frame timesteps given in the txt files.

2. for that I use opencv library. you can install it:
- $ pip install opencv-python

3. again for each dataset (train,test, or validation) put the extract.py in the code folder (e.g. ~/MannequinChallenge/train/code/extract.py)

4. change the variable "num_of_frames" in line 25 to the number of folders in data directory (e.g. ~/MannequinChallenge/train/data/)

5. run extract.py:
- $ python extract.py

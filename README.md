# Mannequin-Data-Download

This is a python implementation of downloading the videos for mannequin paper (https://arxiv.org/pdf/1904.11111.pdf)

## Download txt files
1. download the mannequin dataset from here (https://google.github.io/mannequinchallenge/www/download.html)
2. extract the files in a directory (e.g. ~/MannequinChallenge)

## download videos
1. I use pytube3 for downloading the videos. more information at (https://towardsdatascience.com/the-easiest-way-to-download-youtube-videos-using-python-2640958318ab)

2. Install pytube3 for python3:
- $ pip install pytube3

3. make a folder code in the extracted directory and put the download.py there (e.g. ~/MannequinChallenge/code/download.py)

4. run the download.py:
- $ python download.py

5. your data will be downloaded in data folder in extracted directory (e.g. ~/MannequinChallenge/data/)
each folder in the data directory represent each txt file.

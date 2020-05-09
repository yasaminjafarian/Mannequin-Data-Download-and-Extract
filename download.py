from pytube import YouTube
# misc
import os
import shutil
import math
import datetime
# plots
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join


def read_link_from_file(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines[0]

def write_link_in_file(out_filename,link):
    outF = open(out_filename, "w")
    outF.write(link)
    outF.write("\n")
    outF.close()

def write_frames_data_in_file(in_filename, out_filename):
    f = open(in_filename)
    lines = f.readlines()
    f.close()

    outF = open(out_filename, "w")
    for i in range(1,len(lines)):
        outF.write(lines[i])
    outF.close()

files_path = '../'
out_path = '../data/'

txtfiles = [f for f in listdir(files_path) if isfile(join(files_path, f))]

for f in range(0,len(txtfiles)):

    print('processing file number %5d from %5d files'%(f, len(txtfiles)))

    # make the folder for each data
    out_frame_path = out_path + str(f)
    if not os.path.isdir(out_frame_path):
        os.mkdir(out_frame_path)

    # creat the file names for each file
    txtfile = txtfiles[f]
    in_filename = files_path + txtfile
    out_frame_path = out_frame_path+'/'
    out_filename = out_frame_path + 'frames.txt'
    link_filename = out_frame_path + 'link.txt'
    org_filename = out_frame_path + 'org_txt_name.txt'

    # get the link for the video
    link = read_link_from_file(in_filename)

    # write files in data directory
    write_link_in_file(link_filename, link)
    write_frames_data_in_file(in_filename, out_filename)
    write_link_in_file(org_filename, txtfile)


    # write video in the data directory
    try:
        video = YouTube(link)
        video.streams.get_by_itag(18).download(out_frame_path)
    except Exception as e:
        print("problem faced while processing file number %5d."%(f))
        print(e)
        continue



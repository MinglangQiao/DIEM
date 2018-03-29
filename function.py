import numpy as np
import os
from video_subjects import *
import json
import imageio



def get_dir_files(file_path):

    f = []
    for root, dirs, files in  os.walk(file_path):
        f = dirs
        break

    return  f


def get_all_video_config():

    for i_video in range(len(video_list)):
        video_name = video_list[i_video]
        video_path = ('./all_video/' + video_name + '/video/' +
                      video_name + '.mp4')

        FRAMERATE, FRAMESCOUNT, IMAGEWIDTH, IMAGEHEIGHT = get_video_config(
            video_path)


        save_txt(video_name, FRAMESCOUNT, IMAGEWIDTH, IMAGEHEIGHT)

        print("video: %d"%i_video)


def read_all_video_config():

    video_config = []

    path = 'Data/Video_config/'
    read_path =  path + '0329_video_config.txt'
    f = open(read_path, 'r')
    lines = f.readlines()

    for line in lines:
        line = line.split()
        video_config.append([line[0], line[1], line[2], line[3]])

    return video_config

def get_one_video_fixations():

    pass


def get_all_video_fxiation():
    pass


def get_video_config(video_path):
    file_in_1 = video_path
    # # get the paramters
    # # get the paramters
    video = imageio.get_reader(file_in_1, 'ffmpeg')

    FRAMERATE= round(video._meta['fps'])
    FRAMESCOUNT = video._meta['nframes']
    Frame_size  = video._meta['source_size']
    IMAGEWIDTH = round(Frame_size[0])
    IMAGEHEIGHT = round(Frame_size[1])
    Second_total = FRAMESCOUNT / FRAMERATE

    return FRAMERATE,  FRAMESCOUNT,  IMAGEWIDTH, IMAGEHEIGHT


def save_txt(video_name, FRAMESCOUNT, IMAGEWIDTH, IMAGEHEIGHT):

    path = 'Data/Video_config/'

    save_path =  path + '0329_video_config.txt'
    save_data = ( str(video_name) + '\t' + str(FRAMESCOUNT) + '\t'  +
                  str(IMAGEWIDTH)  + '\t' + str(IMAGEHEIGHT) + '\n' )

    f = open(save_path, 'a')
    f.write(save_data)
    f.close()

def extract_fixations(video_name):
    """
    extract one subject's fixation data

    :parameter
    video_name：


    :return:
    subject_num: the number of subject in one video
    fixations: a m x n list, where m is the subject_num, n is the fiaxtion data
               length one video's fixations

    """
    










































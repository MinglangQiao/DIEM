import numpy as np
import os
from video_subjects import *
import json
import imageio



def get_dirs(file_path):

    f = []
    for root, dirs, files in  os.walk(file_path):
        f = dirs
        break

    return  f

def get_all_files(file_path):
    """
    get all files in a directory

    :paramer

    file_path:

    :return:

    f:
    """

    f = []
    for (dirpath, dirnames, filenames) in os.walk(file_path):
        f.extend(filenames)
        break

    return f

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

def extract_one_video_fixations(video_name):
    """
    extract one subject's fixation data

    :parameter
    video_name：

    :return:
    fixations: one video's fixations, a m x n list, where m is the subject_num,
               n is the fiaxtion data length
    """

    file_path = './all_video/' + video_name + '/event_data/'
    all_subjects = get_all_files(file_path)

    one_video_fixation = []

    for i_subject in range(len(all_subjects)):
        subject_name = all_subjects[i_subject]
        read_path = file_path + subject_name

        one_subject_data = read_fixation_txt(read_path)
        one_video_fixation.append(one_subject_data)

    return one_video_fixation


def extract_all_video_fixations():

    all_video_fixation = []
    for i_video in range(len(video_list)):
        video_name = video_list[i_video]

        one_video_fixation = extract_one_video_fixations(video_name)



def read_fixation_txt(path):
    """
    read the fixation txt

    :param
    path:

    :return:
    one_subject_data: [frame, left_x, left_y, left_dil, left_event, right_x,
        %         right_y, right_dil, right_event]

    """

    read_path = path

    one_subject_data = []
    f = open(read_path, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.split()
        one_subject_data.append([line[0], line[1], line[2], line[3], line[4],
                             line[5], line[6], line[7], line[8]])

    return one_subject_data


def filter_fixation_data(one_video_fixation):
    """
    from the raw data get the valid fixation data：
    1) the left event and right event
    2) and the x and y value should be smaller than the frame width and height


    :param
    one_subject_data:

    :return:

    filterd_one_video_data:

    """
    subject_num = len(one_video_fixation)



    return filterd_one_video_data







































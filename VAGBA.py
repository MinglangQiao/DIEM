import numpy as np
import os
from video_subjects import *
import json
import imageio
from config import  *
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
from function import *


def get_video_list(path = VAGBA_path_video_list_path):
    """

    :param path:
    :return:
    """
    video_list = get_all_files(path)
    for i in video_list:
        print("'%s',"%i[:-9])

    return video_list

def get_subject_list(path = VAGBA_path_subject_list_path):
    """

    :param path:
    :return:
    """
    video_list = get_dirs(path)
    for i in video_list:
        print("'%s',"%i[:])

    return video_list


def get_all_fixations():

    total_fixation_num = 0
    for i_subject in range(len(VAGBA_subject_list)):
        valid_video = 0
        for j_video in range((len(VAGBA_video_list))):

            data_path = (VAGBA_path_subject_list_path  + '/'+ VAGBA_subject_list[i_subject]
                         + '/' + VAGBA_video_list[j_video] + '.1920x1080.e-ceyeS')

            try:
                f = open(data_path, 'r')
                lines = f.readlines()
                data_list = []
                for line in lines:
                    line = line.split()
                    data_list.append(line)

                fixation_data = data_list[3:]

                for i_frame in range(VAGBA_one_video_frame):
                    one_frame_start = i_frame * VAGBA_fixation_num_each_frame
                    one_frame_end = (i_frame + 1) * VAGBA_fixation_num_each_frame

                    invalid_num = 0
                    for i2_frame in range(one_frame_start, one_frame_end):
                    # for i2_frame in range(82, 90):
                        if 'NaN' in fixation_data[i2_frame]:
                            invalid_num += 1

                    if invalid_num < 8:
                        total_fixation_num += 1

                    a =122

                valid_video += 1

            except Exception as e:
                print('file not exist !: ', e)

            print('>>i_subject: %d/%d, valid_video: %d, total_fixation_num: %d' % (
                i_subject, len(VAGBA_subject_list), valid_video, total_fixation_num))

        print('>>i_subject: %d/%d, valid_video: %d, total_fixation_num: %d'%(
            i_subject, len(VAGBA_subject_list), valid_video, total_fixation_num))



















def main():
    get_all_fixations()
























if __name__ == '__main__':
    main()
import numpy as np
from config import *
from function import *
import time
import matplotlib.pyplot as plt


def get_video_list(path = SAVAM_path_video_list_path):
    """

    :param path:
    :return:
    """
    f = open(path, 'r')
    lines = f.readlines()
    video_list = []
    for line in lines:
        line = line.split()
        video_list.append(line)
        print(line, end = ',\n')

    return video_list

def get_user_list(path = SAVAM_path_user_list_path):
    """

    :param path:
    :return:
    """
    f = open(path, 'r')
    lines = f.readlines()
    user_list = []
    for line in lines:
        line = line.split()
        user_list.append(line)
        print(line, end=',\n')

    return user_list


def get_total_frames():
    """

    :return:
    """

    total_frame = 0
    for i_video in range(len(SAVAM_video_list)):
        video_name = (SAVAM_video_list[i_video][0] + '_' +
                      SAVAM_video_list[i_video][1] + '_' +
                      SAVAM_video_list[i_video][2] + '_' + 'left'

                      )
        FRAMERATE, FRAMESCOUNT, IMAGEWIDTH, IMAGEHEIGHT =  get_video_config(
            video_name, video_path = SAVAM_video_path)


        total_frame += FRAMESCOUNT
        # print(">>total_frame:%d"%total_frame)
        a1 = SAVAM_video_list[i_video]
        a1.append(FRAMESCOUNT)
        a1.append(FRAMERATE)
        print('%s,'%a1)

def get_total_fixations():
    """

    :return:
    """
    all_video_fixation_num = 0
    for i_video in range(len(SAVAM_video_list)):
        for i_subject in range(len(SAVAM_user_list)):

            frame_total = SAVAM_video_list[i_video][3]
            record_name = (SAVAM_video_list[i_video][0] + '_' +
                           SAVAM_video_list[i_video][1] + '_' +
                           SAVAM_video_list[i_video][2] + '_' +
                           SAVAM_user_list[i_video][0] + '_' +
                           SAVAM_user_list[i_video][1] + '_' +
                           SAVAM_user_list[i_video][2] + '_' +
                           SAVAM_user_list[i_video][3] + '_' +
                           SAVAM_user_list[i_video][4] + '.txt'
                           )
            data_path = SAVAM_path_filtered_data_path + record_name

            f = open(data_path, 'r')
            lines = f.readlines()
            all_data = [line.split() for line in lines]
            record_len = len(all_data)

            for i_frame in range(frame_total):
                ## for each frame interval
                one_frame_start =  i_frame * sample_of_each_frame
                one_frame_end = (i_frame + 1) * sample_of_each_frame
                if one_frame_start >= record_len:
                    print('======== error: one_frame_start: %d >= record_len:'
                          ' %d'%(one_frame_start, record_len))
                    break
                if one_frame_end >= record_len:
                    one_frame_end = (record_len -1)

                valid_record = 0
                valid_frame = 0
                for i_record in range(one_frame_start, one_frame_end):
                    left_x = float(all_data[i_record][1])
                    left_y = float(all_data[i_record][2])
                    right_x = float(all_data[i_record][3])
                    right_y = float(all_data[i_record][4])

                    if (left_x != 0 and left_y != 0 and right_x != 0 and
                        right_y != 0):

                        valid_record += 1
                        valid_frame = 1
                        break

                if valid_frame == 1:
                    all_video_fixation_num += 1
                else:
                    pass
                    # print('>>>> invalid fixation of one frame: i_frame: %d, '
                    #       'i_record: %d'%(i_frame, one_frame_start))

            print('>>>>i_video: %d/%d, i_subject: %d/%d, all_video_fixation_num:'
                  ' %d'%(i_video, len(SAVAM_video_list), i_subject,
                      len(SAVAM_user_list), all_video_fixation_num))


















































if __name__ == '__main__':
    get_total_fixations()
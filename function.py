import numpy as np
import os
from video_subjects import *
import json
import imageio
from config import  *
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage



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
    """

    :return:
    [line[0], line[1], line[2], line[3]]: [video_name, frames, frame_width,
    frame_height]
    """

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

    return one_video_fixation, all_subjects


def extract_all_video_fixations(all_video_config):

    all_video_fixation = []
    for i_video in range(len(video_list)):
        video_name = video_list[i_video]

        one_video_fixation, all_subjects = extract_one_video_fixations(
            video_name)
        one_video_eye_fixation = filter_fixation_data(i_video,
                                                      all_subjects,
                                                      one_video_fixation,
                                                      all_video_config)

        save_filter_fixations(one_video_eye_fixation, video_name)

        debug = True

    return one_video_eye_fixation


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
        one_subject_data.append([float(line[0]), float(line[1]), float(line[2]),
                                 float(line[3]), float(line[4]), float(line[5]),
                                 float(line[6]), float(line[7]), float(line[8])]
                                )

    return one_subject_data


def filter_fixation_data(video_index, all_subjects,
                         one_video_fixation, all_video_config):
    """
    from the raw data get the valid fixation data：
    1) the left event and right event
    2) and the x and y value should be smaller than the frame width and height


    :param
    video_index:
    one_video_fixation：
    all_video_config：

    :return:

    one_video_eye_fixation: [[[f1_s1_x, f1_s1_y], [f1_s2_x, f1_s2_y]],
    [[f2_s1_x, f2_s1_y], [f2_s2_x, f2_s2_y]]]

    """
    subject_num = len(one_video_fixation)
    frame_width = float(all_video_config[video_index][2])
    frame_height = float(all_video_config[video_index][3])
    frame_num  = len(one_video_fixation[0])
    IMG_W = round(DIEM_IMG_H * frame_width / frame_height / 32) * 32
    offsetX = (1280 - frame_width) / 2
    offsetY = (960 - frame_height) / 2

    one_video_eye_fixation = [[] for i in range(frame_num) ]

    for i_frame in range(frame_num):

        for i_subject in range(subject_num):
            # as some subjects may loose some frames, this subject's selected
            #  data may have problem, so we diacard them
            if frame_num == len(one_video_fixation[i_subject]):

                one_subject_one_frame_data = one_video_fixation[i_subject][
                    i_frame]
                x1 = one_subject_one_frame_data[1] - offsetX
                y1 = one_subject_one_frame_data[2] - offsetY
                x2 = one_subject_one_frame_data[5] - offsetX
                y2 = one_subject_one_frame_data[6] - offsetY

                if (one_subject_one_frame_data[4] == 1 and
                    one_subject_one_frame_data[8] == 1 and
                    x1 >= 3 and y1 >= 3 and x2 >= 3 and y2 >= 3 and
                    x1 <  (frame_width -3) and x2 < (frame_width -3) and
                    y1 <  (frame_width -3) and y2 <  (frame_width -3)):

                    one_video_eye_fixation[i_frame].append([round((x1 + x2)/2),
                    round((y1 + y2)/2)])
                else:
                    one_video_eye_fixation[i_frame].append([-1, -1])

                print('>>>>>>i_video: %d, video_name: %s,  i_subject: %d'%(
                    video_index, video_list[video_index], i_subject))

    return one_video_eye_fixation

def save_filter_fixations(one_video_eye_fixation, video_name):
    """

    :param
    one_video_eye_fixation:

    :return:

    """

    np.save("Data/extract_fixations/ " + video_name + ".npy", one_video_eye_fixation)

def read_extract_fixations(video_name):

    one_video_fixation = np.load("Data/extract_fixations/ " + video_name + ".npy")

    return one_video_fixation

def verify_data(one_video_fixation, video_name):

    frame_num = len(one_video_fixation)

    for i_frame in range(frame_num):
        one_frame_data = one_video_fixation[i_frame]
        one_frame_x = [one_frame_data[i][0] for i in range(len(one_frame_data))]
        one_frame_y = [one_frame_data[i][1] for i in range(len(one_frame_data))]

        one_frame_x = [i for i in one_frame_x if i != -1]
        one_frame_y = [i for i in one_frame_y if i != -1]

        figure = plt.figure()
        ax1 = figure.add_subplot(111)
        ax1.scatter(one_frame_x, one_frame_y, c='b', marker='*', alpha=1)
        ax1.set_xlim([0, screen_width])
        ax1.set_ylim([0, screen_heigth])
        ax1.set_title(video_name + '>>>i_frame: ' + str(i_frame) + '>>>' +
                      'fixations:' + str(len(one_frame_x)))

        # plt.show()
        path_figure = ('Data//fixation_visualization/' +
                        video_name + '_' + str(i_frame) +
                           '.png')

        plt.savefig(path_figure)

def plot_data(data1, data2):
    figure = plt.figure()

    ax1 = figure.add_subplot(211)
    ax1.imshow(data1, cmap='gray')
    ax1.set_xlim([0, screen_width])
    ax1.set_ylim([0, screen_heigth])

    ax2 = figure.add_subplot(212)
    ax2.imshow(data2, cmap='gray')
    ax2.set_xlim([0, screen_width])
    ax2.set_ylim([0, screen_heigth])

    plt.show()

def cal_consistent(one_video_fixation, video_name):

    frame_num = len(one_video_fixation)
    subject_num = len(one_video_fixation[0])
    all_subject_ave_cc = []

    for i_subject in range(subject_num):

        for i_frame in range(frame_num):

            one_subject_ave_cc = []

            one_frame_data = one_video_fixation[i_frame]
            one_frame_x = [one_frame_data[i][0] for i in
                           range(len(one_frame_data))]
            one_frame_y = [one_frame_data[i][1] for i in
                           range(len(one_frame_data))]

            if (one_frame_x[i_subject] != -1 and one_frame_y[i_subject] != -1):

                ground_fixaton = [[one_frame_x[i_subject],
                                  one_frame_y[i_subject]]]

                pre_fixaton = [one_frame_data[i] for i in
                               range(subject_num) if i != i_subject and
                               one_frame_data[i][0] != -1 and
                               one_frame_data[i][1] != -1]

                ground_hmap = np.zeros((screen_heigth, screen_width))
                for fix in ground_fixaton:
                    ground_hmap[fix[1]-1][fix[0]-1] = 255

                pre_hmap = np.zeros((screen_heigth, screen_width))
                for fix in pre_fixaton:
                    pre_hmap[fix[1]-1][fix[0]-1] = 255

                ground_hmap = ndimage.gaussian_filter(ground_hmap,
                    sigma=(ground_sigma , ground_sigma ), order=0)
                pre_hmap = ndimage.gaussian_filter(pre_hmap,
                    sigma=(pre_figma, pre_figma), order=0)

                # plot_data(ground_hmap, pre_hmap)

                cc = calc_cc_score(ground_hmap,  pre_hmap)
                print('>>>i_subject: %d, i_frame: %d/%d, cc: %f'%(i_subject,
                     i_frame, frame_num, cc))
                one_subject_ave_cc.append(cc)


        # !!!!!!!!!!!!! please add figure to observe lile visdom

        one_subject_ave_cc = np.mean(one_subject_ave_cc) # check
        print('>>> one_subject_ave_cc: %f'%one_subject_ave_cc)

        all_subject_ave_cc.append(one_subject_ave_cc)

    all_subject_ave_cc = np.mean(all_subject_ave_cc)
    print('>>>>>> all_subject_ave_cc: %f' %all_subject_ave_cc)

    return all_subject_ave_cc



def calc_cc_score(gtsAnn, resAnn):
    """
    Computer CC score. A simple implementation
    :param gtsAnn : ground-truth fixation map
    :param resAnn : predicted saliency map
    :return score: int : score
    """

    fixationMap = gtsAnn - np.mean(gtsAnn)
    if np.max(fixationMap) > 0:
        fixationMap = fixationMap / np.std(fixationMap)
    salMap = resAnn - np.mean(resAnn)
    if np.max(salMap) > 0:
        salMap = salMap / np.std(salMap)

    if np.max(fixationMap) > 0 and np.max(salMap) > 0:
        return np.corrcoef(salMap.reshape(-1), fixationMap.reshape(-1))[0][1]
    else:
        return 0











































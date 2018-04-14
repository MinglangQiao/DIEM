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
                    y1 <  (frame_height -3) and y2 <  (frame_height -3)):

                    one_video_eye_fixation[i_frame].append([round((x1 + x2)/2),
                    round((y1 + y2)/2)])
                # else:
                    # pass
                    # one_video_eye_fixation[i_frame].append([-1, -1])

                print('>>>>>>i_video: %d, video_name: %s,  i_subject: %d'%(
                    video_index, video_list[video_index], i_subject))

    return one_video_eye_fixation

def save_filter_fixations(one_video_eye_fixation, video_name):
    """

    :param
    one_video_eye_fixation:

    :return:

    """

    np.save("Data/extract_fixations/ " + video_name + ".npy",
            one_video_eye_fixation)

def read_extract_fixations(video_name):

    one_video_fixation = np.load("Data/extract_fixations/ " + video_name
                                 + ".npy")

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

    # data1 = data[0]
    # data2 = data[1]
    ax1 = figure.add_subplot(211)
    ax1.imshow(data1, cmap='jet')
    ax1.set_xlim([0, int(screen_width/down_sample_rate)])
    ax1.set_ylim([0, int(screen_heigth/down_sample_rate)])

    ax2 = figure.add_subplot(212)
    ax2.imshow(data2, cmap='jet')
    ax2.set_xlim([0, int(screen_width/down_sample_rate)])
    ax2.set_ylim([0, int(screen_heigth/down_sample_rate)])

    # ax3 = figure.add_subplot(111)
    # ax3.plot(data)

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

                ground_fixaton = [[int(one_frame_x[i_subject]/down_sample_rate),
                                  int(one_frame_y[i_subject]/down_sample_rate)]]

                pre_fixaton = [(one_frame_data[i]/down_sample_rate).astype(int)
                               for i in range(subject_num) if i != i_subject
                               and one_frame_data[i][0] != -1 and
                               one_frame_data[i][1] != -1]


                ground_hmap = np.zeros((int(screen_heigth/down_sample_rate),
                                        int(screen_width/down_sample_rate)))
                for fix in ground_fixaton:
                    ground_hmap[fix[1]-1][fix[0]-1] = 255

                pre_hmap = np.zeros((int(screen_heigth/down_sample_rate),
                                     int(screen_width/down_sample_rate)))
                for fix in pre_fixaton:
                    pre_hmap[fix[1]-1][fix[0]-1] = 255

                ground_hmap = ndimage.gaussian_filter(ground_hmap,
                    sigma=(ground_sigma, ground_sigma ), order=0)
                pre_hmap = ndimage.gaussian_filter(pre_hmap,
                    sigma=(pre_figma, pre_figma), order=0)

                plot_data(ground_hmap, pre_hmap)

                cc = calc_cc_score(ground_hmap,  pre_hmap)
                print('>>>i_subject: %d, i_frame: %d/%d, cc: %f'%(i_subject,
                     i_frame, frame_num, cc))
                one_subject_ave_cc.append(cc)


        one_subject_ave_cc = np.mean(one_subject_ave_cc) # check
        all_subject_ave_cc.append(one_subject_ave_cc)

        print('>>> one_subject_ave_cc: %f'%one_subject_ave_cc)

    all_subject_ave_cc = np.mean(all_subject_ave_cc)
    print('>>>>>> all_subject_ave_cc: %f' %all_subject_ave_cc)

    return all_subject_ave_cc


def cal_consist_v2(one_video_fixation, video_name, one_video_config):

    frame_width = int(one_video_config[2])
    frame_height = int(one_video_config[3])

    frame_num = len(one_video_fixation)
    subject_num = len(one_video_fixation[0])
    all_pair_cc = []

    for i_pair in range(pair_start, pair_end):

        one_pair_cc = []
        for i_subject in range(i_pair):

            one_subject_cc = []
            for i_frame in range(frame_num):

                if i_frame%frame_step == 0 and (len(one_video_fixation[i_frame])
                    >= i_pair):

                    one_frame_data = np.array(one_video_fixation[i_frame])


                    ground_fixation = [(one_frame_data[i]/down_sample_rate)
                                        .astype(int) for i in range(i_pair)
                                        if i == i_subject]

                    predict_fixation = [(one_frame_data[i]/down_sample_rate)
                                        .astype(int) for i in range(i_pair)
                                        if i != i_subject]

                    ground_hmap = np.zeros((int(frame_height / down_sample_rate),
                                            int(frame_width / down_sample_rate)))
                    for fix in ground_fixation:
                        y = fix[1]
                        x = fix[0]
                        ground_hmap[y][x] = 255

                    pre_hmap = np.zeros((int(frame_height / down_sample_rate),
                                         int(frame_width / down_sample_rate)))
                    for fix in predict_fixation:
                        y = fix[1]
                        x = fix[0]
                        pre_hmap[y][x] = 255

                    ground_hmap = ndimage.gaussian_filter(ground_hmap,
                        sigma=(ground_sigma, ground_sigma ), order=0)
                    pre_hmap = ndimage.gaussian_filter(pre_hmap,
                        sigma=(pre_figma, pre_figma), order=0)

                    # plot_data(ground_hmap, pre_hmap)
                    cc = calc_cc_score(ground_hmap, pre_hmap)
                    # print('>>>i_pair: %d, i_subject: %d, i_frame: %d/%d, cc: %f'%(
                    #       i_pair, i_subject, i_frame, frame_num, cc))

                    one_subject_cc.append(cc)

            one_subject_cc = np.mean(one_subject_cc)
            one_pair_cc.append(one_subject_cc)

        one_pair_cc = np.mean(one_pair_cc)
        all_pair_cc.append(one_pair_cc)
        save_const_cc(one_pair_cc, video_name)
        print("=============>i_pair: %d one_pair_cc: %s"%(i_pair, one_pair_cc))


    return all_pair_cc


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


def get_one_video_fixation_num(one_video_fixation):

    frame_num = len(one_video_fixation)
    one_video_fixation_num = 0
    one_frame_fixation_num = 0

    for i_frame in range(frame_num):
        one_frame_fixation_num = len(one_video_fixation[i_frame])
        one_video_fixation_num += one_frame_fixation_num

    return one_video_fixation_num


def get_all_video_frame():
    pass


def save_txt(path, data1, data2, video_name):
    """
    :param
    one_video_eye_fixation:
    data: fixation num

    :return:

    """

    save_path = path + "Fixation_num.txt"
    f = open(save_path, "a")
    save_data = video_name +'\t' + str(data1) + '\t' + str(data2) + '\n'
    f.write(save_data)

def save_const_cc(data, video_name, path = "Data/const_cc/"):

    save_path = path + video_name + '.txt'
    f = open(save_path, "a")
    save_data = str(data) + '\n'
    f.write(save_data)
    f.close()

def get_all_subject(all_video_config):

    all_subject_num = 0
    for i_video in range(len(all_video_config)):
        file_path = "all_video/" + all_video_config[i_video][0] + "/event_data/"

        files = get_all_files(file_path)
        subject_num = len(files)
        all_subject_num += subject_num
        print(">>>>>>>>i_video: %d, subject_num: %d"%(i_video, subject_num))

    return all_subject_num


def result_process():

    all_video_data = []
    for i_video in range(len(video_list)):

        read_path = 'Data/const_cc/' + video_list[i_video] + ".txt"

        f = open(read_path, "r")
        lines = f.readlines()
        one_video_data = []

        for line in lines:
            line = line.split()
            one_video_data.append(line)

        one_video_data_1 = [one_video_data[i][0] for i in
                            range(len(one_video_data))]
        if ('nan' in one_video_data_1) == False:
            all_video_data.append(one_video_data_1)


    ## ave_frame
    ave_result = []
    for i_pair in range(SET_Value - pair_start):

        one_pair_result = []
        one_pair_result = [float(all_video_data[i_video][i_pair])
                           for i_video in range(len(all_video_data))]

        print(">>>>>>>>>>>>> len(one_pair_result): ", len(one_pair_result))

        # if ('nan' in all_video_data[i_video][i_pair]) == False

        one_pair_result = np.mean(one_pair_result)
        ave_result.append(one_pair_result)

    return ave_result

def plot_data_v2(data):
    figure = plt.figure()

    ax1 = figure.add_subplot(111)
    ax1.plot(data)

    plt.show()


def remap_3d_to_2d(head_lat, head_lon, head_rotate, eye_lon, eye_lat, frame_width, frame_height):
    '''
    project the 3d coordinate into 2d coordinate in the 2d screen
    the head_lat, head_lon, head_rotate are in degree
    the eye_lon, eye_lat are in radian
    Parameters
    ----------
    heng: x location in frame
    shu: y location in frame
    lonwhole: head_lon + eye_lon
    latwhole: head_lat + eye_lat
    but I still not clear about the math theroy of the translation
    '''

    from numpy import sin, cos, tan, pi
    from math import acos, atan2
    # import numpy as np

    'parameter'
    dw = 1080 # the fov horizontal size in pixel
    dh = 1200 # the fov vertical size in pixel
    fvx = 110 # the horizontal degree of fov
    fvy = 113 # the vertical degree of fov
    w = 4096 # the output frame size ?
    h = 2048 # the output frmae height ?
    E = [0, 0, 0]

    'convert the head 3d to 2d'
    fovx = pi * fvx / 180 # transfor degree to radian
    fovy = pi * fvy / 180
    fx = dw / (2 * tan(fovx / 2))
    fy = dh / (2 * tan(fovy / 2))
    K = np.array([[fx, 0, dw/2], [0, fy, dh/2], [0, 0, 1]])
    R = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    E[0] = sin(eye_lon) * cos(eye_lat)
    E[1] = sin(eye_lat)
    E[2] = cos(eye_lon) * cos(eye_lat)
    E = np.array(E) * np.array([-1, -1, 1]) # multily in corresponding location
    ee = np.dot(np.dot(K, R.T), E.T) # standard matrix multiply
    e = ee/ee[2]

    'restore the head rotate'
    U = e[0] * cos(head_rotate * pi / 180) - e[1] * sin(head_rotate * pi / 180) # horizontal
    V = e[0] * sin(head_rotate * pi / 180) + e[1] * cos(head_rotate * pi / 180) #vertical

    'combine the 2d fov(U,V) with head(lat, lon) project to the 3d sphere'
    E = [] # clear E
    K = np.mat([[fx, 0, dw/2], [0, -fy, dh/2], [0, 0, 1]])

    phi = (head_lat.astype('float') * pi / 180)
    tht = (head_lon.astype('float') * pi / 180)
    R = np.array([[cos(tht), sin(tht) * sin(phi), sin(tht) * cos(phi)], [0, cos(phi), -sin(phi)],
                  [-sin(tht), cos(tht) * sin(phi), cos(tht) * cos(phi)]])

    e = np.array([U, V, 1]).T
    e = np.array(e)
    q = np.dot(np.array(K.I), e.T) # jizhi
    P = (q * np.array([1, 1, -1])) / np.linalg.norm(q) #if q is 1-d martix, the same as matlab,if 2-d has some difference
    E = np.dot(R , P)

    head_lat = acos(E[1])
    head_lon = atan2(E[0], -E[2])

    'project to the panaramic frame: big_x, big_y'
    big_x = head_lon * frame_width / (2 * pi) # center is 0
    big_y = head_lat * frame_height / pi # top is 0, buttom is frame_height
    heng = big_x + frame_width / 2
    shu = big_y
    lonwhole = head_lon
    latwhole = head_lat

    return heng, shu, lonwhole, latwhole


def resume_hmap(im, frame_index, frame_width, frame_height):
    """
    get the frame image which include the fixation

    :param
    im: frame image
    :param frame_index:
    :return:
    """

    fig = plt.figure()
    implot = plt.imshow(pic)

    'get eye position in one frame'
    heng, shu, lon_whole, lat_whole = remap_3d_to_2d(
        one_video_lat[i_subject][i_frame], one_video_lon[i_subject][i_frame],
        one_video_rot[i_subject][i_frame], one_video_eye_lon[i_subject][
        i_frame], one_video_eye_lat[i_subject][i_frame], frame_width,
        frame_height)



def get_video_config(video_name, video_path = CRCNS_video_path):

    file_in_1 = video_path + video_name + '.mpg'
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






























































































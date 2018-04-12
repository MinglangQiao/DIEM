import numpy as np
from config import *
from function import *
import time
import matplotlib.pyplot as plt

def main():

    # all_videos = get_dirs(file_path = video_path)
    # get_all_video_config()

    all_video_config = read_all_video_config()
    # all_video_fixation = extract_all_video_fixations(all_video_config)
    # N  = get_all_subject(all_video_config)
    # print(">>>>>>>>>....all_subject_num: ", N)

    all_video_result = result_process()

    plot_data_v2(all_video_result)
    # print(">>>>>>>>>>>>> t", all_video_result)
    all_video_cc = []
    all_video_frames = 0

    # read data
    for i_video in range(Num_videos):
        video_name = video_list[i_video]
        one_video_frame_num = int(all_video_config[i_video][1])
        all_video_frames += one_video_frame_num
        one_video_config = all_video_config[i_video]

        one_video_fixation = read_extract_fixations(video_name)

        # one_video_fixation_num = get_one_video_fixation_num(one_video_fixation)
        # one_video_ave_fixation_one_frame = int(one_video_fixation_num/
        #                                        one_video_frame_num)

        # save_txt(path = "Data/",
        #          data1 = one_video_fixation_num,
        #          data2 = one_video_ave_fixation_one_frame,
        #          video_name = video_name)

        # verify_data(one_video_fixation, video_name)

        # one_video_cc = cal_consistent(one_video_fixation, video_name)

        all_pair_cc_of_one_video = cal_consist_v2(one_video_fixation,
                                                  video_name,
                                                  one_video_config)


        print('>>>>>>i_video: %d'%i_video)
        print('>>>>>>>>: all_video_frames: %d'%all_video_frames)


        # a = 1































































































if __name__ == '__main__':
    main()
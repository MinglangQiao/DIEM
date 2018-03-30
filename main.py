import numpy as np
from config import *
from function import *
import time
import matplotlib.pyplot as plt

def main():

    # all_videos = get_dirs(file_path = video_path)
    # get_all_video_config()
    # all_video_fixation = extract_all_video_fixations(all_video_config)

    all_video_config = read_all_video_config()

    # read data
    for i_video in range(Num_videos):
        video_name = video_list[i_video]

        one_video_fixation = read_extract_fixations(video_name)

        # verify_data(one_video_fixation, video_name)

        cal_consistent(one_video_fixation, video_name)

        print('>>>>>>i_video: %d'%i_video)


        # a = 1































































































if __name__ == '__main__':
    main()
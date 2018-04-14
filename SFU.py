from config import *
from function import *
import csv

def get_video_list(path = SFU_data_path):

    file = get_all_files(path)

    for i_video in file:
        if i_video[-8:-1] != "mask.cs":
            print("'%s',"%i_video[:-11])

def get_total_frames(SFU_frame_list, SFU_video_list):

    all_frame = 0
    for i in range(len(SFU_video_list)):
        all_frame += SFU_frame_list[SFU_video_list[i]]

    print('total frame: %d'%all_frame)


def get_total_fixation(SFU_data_path):

    get_total_fixation_num = 0
    for i_video in range(len(SFU_video_list)):

        one_video_data = []
        one_video_mask = []

        video_name = SFU_video_list[i_video]
        video_data_path = SFU_data_path + '/' +  video_name + "-Screen.csv"
        video_mask_path = SFU_data_path + '/' + video_name + "-mask.csv"

        f_video_data = csv.reader(open(video_data_path, "r"))
        for line in f_video_data:
            # line = line.split()
            one_video_data.append(line)

        f_mask_data =  csv.reader(open(video_mask_path, "r"))
        for line in f_mask_data:
            one_video_mask.append(line)

        video_frame = len(one_video_data) - 2

        for i_frame in range(2, video_frame + 2):

            for i_subject in range(SFU_subject_num):
                subject_data_start = i_subject * 4
                subject_data_end = (i_subject + 1) * 4
                one_person_data = one_video_mask[i_frame][subject_data_start:
                                                       subject_data_end]

                if float(one_person_data[0]) * float(one_person_data[1]) == 1or(
                    float(one_person_data[2]) * float(one_person_data[3]) == 1):

                    get_total_fixation_num += 1

            print("i_video: %d, i_frame: %d, fixation_num: %d"%(i_video, i_frame,
                get_total_fixation_num))

        print("===== i_video: %d, , fixation_num: %d " % (i_video,
            get_total_fixation_num))

















def main():
    get_total_fixation(SFU_data_path)






if __name__ == "__main__":
    main()
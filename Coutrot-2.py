from config import *
from function import *
import scipy.io as sio

def get_all_files_1(path = Coutrot_2_data_path):
    f =  get_all_files(path)
    for i in f:
        print("'%s',"%i)

def get_all_frames(path = Coutrot_2_data_path):

    all_video_frame = 0

    data = sio.loadmat(path)["Coutrot_Database2"]
    # all_video_data = data[0][0][0][0][0][0][0][0][0][0][1]
    one_mode_data = data["Visual"]
    one_video_data = one_mode_data["clip_1"]
    one_video_eye_data = one_video_data["data"]

    one_vdieo_data_1 = all_video_data[0] # clip_1
    one_vdieo_data_2 = one_vdieo_data_1[0] # data
    one_vdieo_data_2_1 = one_vdieo_data_1[1] # info
    one_vdieo_data_3 = one_vdieo_data_2_1[3]

    for i_video in range(1, Coutrot_2_video_num+1):
        one_vdieo_data = all_video_data["clip_%d"%i_video]
        one_video_eye_data = one_vdieo_data["data"]
        one_video_video_data = one_vdieo_data["info"]
        one_video_frame = one_video_video_data["nframe"]
        all_video_frame += one_video_frame

        print(all_video_frame)

    print(">>>> all_video_frame: %d"%all_video_frame)


def get_all_fixations():
    pass


def main():
    get_all_frames()


if __name__ == "__main__":
    main()
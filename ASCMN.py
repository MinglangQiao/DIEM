from config import *
from function import *
import scipy.io as sio

def get_all_files_1(path = ASCMN_data_path ):
    f =  get_all_files(path)
    for i in f:
        print("'%s',"%i)

def get_all_frames(path = ASCMN_data_path ):

    all_video_frame = 0
    for i_video in range(len(ASCMN_video_list)):
        mat_path = path + ASCMN_video_list[i_video]
        data=sio.loadmat(mat_path)
        one_video_frame = data["nFrames"][0][0]
        all_video_frame += (one_video_frame)
        print(all_video_frame)

    print(">>>> all_video_frame: %d"%all_video_frame)


def get_all_fixations():
    pass


def main():
    get_all_frames()


if __name__ == "__main__":
    main()
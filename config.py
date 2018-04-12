

########################## for DIEM # ################################
data_base = 'DIEM'
Num_videos = 84

screen_width = 1280
screen_heigth = 960

# downsample the frame size and sigma
down_sample_rate = 5
ground_sigma = int(7.5 * 5/down_sample_rate)
pre_figma = int(7.5 * 5/down_sample_rate)
frame_step = 10

video_path = './all_video'

all_fixation_num = 240452
DIEM_ave_fixation = 58

SET_Value = 43

pair_start = 2
pair_end = SET_Value

Finding_N_subjects = 9

############################ for CRCNS ########################################
CRCNS_path = "数据库_data/CRCNS/crcns-eye1-1/CRCNS-DataShare/"

frame_path = CRCNS_path + "MPGSIZES.txt"
# see the README.txt for detail
CRCNS_start_frame = 271




########################## for DIEM # ################################
data_base = 'DIEM'
Num_videos = 84

screen_width = 1280
screen_heigth = 960

# downsample the frame size and sigma
down_sample_rate = 5
ground_sigma = int(4.5 * 5/down_sample_rate)
pre_figma = int(4.5 * 5/down_sample_rate)
frame_step = 5


video_path = './all_video'

all_fixation_num = 240452
ave_fixation = 58
SET_Value = 28

pair_start = 2
pair_end = SET_Value


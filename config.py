

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
CRCNS_path = "数据库_data/CRCNS/crcns-eye1-1/"

CRCNS_video_path = "数据库_data/CRCNS/crcns-eye1-1/stimuli/"
CRCNS_frame_path = CRCNS_path + "MPGSIZES.txt"
CRCNS_data_path = "数据库_data/CRCNS/crcns-eye1-2/data-orig"

# see the README.txt for detail
CRCNS_trash_frame = 270
CRCNS_video_num = 50
CRCNS_valid_frame = 32989
CRCNS_valid_fixation = 118785
CRCNS_ave_fixation = 3.60



CRCNS_video_list = [
'beverly01.mpg',
'beverly03.mpg',
'beverly05.mpg',
'beverly06.mpg',
'beverly07.mpg',
'beverly08.mpg',
'gamecube02.mpg',
'gamecube04.mpg',
'gamecube05.mpg',
'gamecube06.mpg',
'gamecube13.mpg',
'gamecube16.mpg',
'gamecube17.mpg',
'gamecube18.mpg',
'gamecube23.mpg',
'monica03.mpg',
'monica04.mpg',
'monica05.mpg',
'monica06.mpg',
'saccadetest.mpg',
'standard01.mpg',
'standard02.mpg',
'standard03.mpg',
'standard04.mpg',
'standard05.mpg',
'standard06.mpg',
'standard07.mpg',
'tv-action01.mpg',
'tv-ads01.mpg',
'tv-ads02.mpg',
'tv-ads03.mpg',
'tv-ads04.mpg',
'tv-announce01.mpg',
'tv-music01.mpg',
'tv-news01.mpg',
'tv-news02.mpg',
'tv-news03.mpg',
'tv-news04.mpg',
'tv-news05.mpg',
'tv-news06.mpg',
'tv-news09.mpg',
'tv-sports01.mpg',
'tv-sports02.mpg',
'tv-sports03.mpg',
'tv-sports04.mpg',
'tv-sports05.mpg',
'tv-talk01.mpg',
'tv-talk03.mpg',
'tv-talk04.mpg',
'tv-talk05.mpg'
]

CRCNS_subjects = [
    'VN',
    'ND',
    'JZ',
    'NM',
    'JA',
    'CZ',
    'VC',
    'RC'
]



################################  SFU   #####################################

SFU_data_path = '数据库_data/SFU/SFU_etdb/CSV'


SFU_total_frames = 3150
SFU_subject_num = 15
SFU_total_fixation = 47061
SFU_ave_fixation = 14.94

SFU_video_list = [
    'harbour',
    'stefan',
    'mother',
    'crew',
    'soccer',
    'city',
    'foreman',
    'mobile',
    'bus',
    'tempete',
    'flower',
    'hall'
]


SFU_frame_list = {
    'harbour': 300,
    'stefan': 90,
    'mother': 300,
    'crew': 300,
    'soccer':300,
    'city': 300,
    'foreman': 300,
    'mobile': 300,
    'bus': 150,
    'tempete': 260,
    'flower': 250,
    'hall': 300
}























































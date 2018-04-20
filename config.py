

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

all_video_frames = 240452
all_fixation_num = 13897289
DIEM_ave_fixation = 57.80

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

################################   ASCMN  #####################################

ASCMN_data_path = "数据库_data/ASCMN/ACCV2012_database/raw_data/"

ASCMN_video_list = [
'raw_data_video14.mat',
'raw_data_video9.mat',
'raw_data_video24.mat',
'raw_data_video15.mat',
'raw_data_video2.mat',
'raw_data_video20.mat',
'raw_data_video18.mat',
'raw_data_video23.mat',
'raw_data_video21.mat',
'raw_data_video11.mat',
'raw_data_video10.mat',
'raw_data_video22.mat',
'raw_data_video12.mat',
'raw_data_video4.mat',
'raw_data_video5.mat',
'raw_data_video17.mat',
'raw_data_video3.mat',
'raw_data_video19.mat',
'raw_data_video6.mat',
'raw_data_video1.mat',
'raw_data_video13.mat',
'raw_data_video7.mat',
'raw_data_video16.mat',
'raw_data_video8.mat'
]


################################  Coutrot-2  ##################################

Coutrot_2_data_path = "数据库_data/coutrot_database2.mat"
Coutrot_2_video_num = 15


############################### coutrot-1 #####################################
all_frames = 26140
all_fixations = 1742344
subjects = 72


############################## SAVAM ##########################################
SAVAM_path_user_list_path = './数据库_data/SAVAM/gaze_data/list_user.txt'
SAVAM_path_video_list_path = './数据库_data/SAVAM/gaze_data/list_video.txt'
SAVAM_path_filtered_data_path = ('./数据库_data/SAVAM/gaze_data/'
                                 'filtered_gaze_data/')

SAVAM_video_path = './数据库_data/SAVAM/sources/all_video/'

SAVAM_total_frames = 18360 # only 41 videos
SAVAM_total_fixations = 1023758
SAVAM_ave_fixation = 55.76
sample_of_each_frame = 20



## [videoname, sequence, start frame in sequence, total_frame, frame_rate]

SAVAM_video_list = [
['v01', 'Hugo', '2172', 450, 25],
['v02', 'Dolphin', '131474', 450, 25],
['v03', 'StepUp', '67443', 450, 25],
['v04', 'LIVE1', '0', 450, 25],
['v05', 'LIVE2', '0', 450, 25],
['v06', 'LIVE3', '0', 450, 25],
['v07', 'Avatar', '142222', 450, 25],
['v08', 'Dolphin', '127156', 450, 25],
['v09', 'StepUpRevolution', '119518', 450, 25],
['v10', 'VQEG01', '0', 400, 25],
['v11', 'VQEG02', '0', 400, 25],
['v12', 'VQEG03', '0', 400, 25],
['v13', 'IntoTheDeep', '36475', 450, 25],
['v14', 'Pirates', '47241', 450, 25],
['v15', 'Sanctum', '147749', 450, 25],
['v16', 'StepUp', '17153', 450, 25],
['v17', 'SpiderMan', '76686', 450, 25],
['v18', 'StepUp', '76411', 450, 25],
['v19', 'Avatar', '206134', 442, 25],
['v20', 'DriveAngry', '2820', 445, 25],
['v21', 'Pirates', '25246', 448, 25],
['v22', 'VQEG04', '0', 400, 25],
['v23', 'VQEG05', '0', 400, 25],
['v24', 'VQEG06', '0', 400, 25],
['v25', 'Dolphin', '17437', 450, 25],
['v26', 'Galapagos', '14830', 450, 25],
['v27', 'UnderworldAwakening', '69044', 450, 25],
['v28', 'VQEG10', '0', 325, 25],
['v29', 'Avatar', '46279', 450, 25],
['v30', 'Dolphin', '79095', 450, 25],
['v31', 'DriveAngry', '83142', 450, 25],
['v32', 'Dolphin', '81162', 450, 25],
['v33', 'Hugo', '87461', 450, 25],
['v34', 'VQEG07', '0', 400, 25],
['v35', 'VQEG08', '0', 400, 25],
['v36', 'VQEG09', '0', 400, 25],
['v37', 'UnderworldAwakening', '91276', 450, 25],
['v38', 'StepUp', '82572', 450, 25],
['v39', 'Avatar', '98125', 450, 25],
['v42', 'MSOffice', '242', 950, 25],
['v43', 'Panasonic', '373', 450, 25]

]








SAVAM_user_list = [
['u001', 'm', '21', '1', 'bwd'],
['u002', 'm', '35', '1', 'fwd'],
['u003', 'm', '24', '1', 'fwd'],
['u004', 'm', '24', '1', 'fwd'],
['u005', 'f', '26', '1', 'fwd'],
['u006', 'm', '19', '1', 'fwd'],
['u007', 'f', '23', '1', 'fwd'],
['u008', 'm', '24', '1', 'fwd'],
['u009', 'm', '21', '3', 'bwd'],
['u010', 'm', '24', '1', 'fwd'],
['u010', 'm', '24', '2', 'bwd'],
['u011', 'f', '56', '1', 'fwd'],
['u012', 'm', '19', '1', 'fwd'],
['u013', 'f', '27', '1', 'fwd'],
['u014', 'f', '24', '1', 'fwd'],
['u014', 'f', '24', '2', 'bwd'],
['u015', 'm', '24', '1', 'fwd'],
['u016', 'm', '21', '1', 'bwd'],
['u017', 'f', '18', '1', 'bwd'],
['u018', 'm', '21', '1', 'bwd'],
['u018', 'm', '21', '2', 'fwd'],
['u019', 'm', '21', '1', 'bwd'],
['u020', 'm', '27', '1', 'fwd'],
['u021', 'm', '19', '1', 'bwd'],
['u021', 'm', '19', '2', 'fwd'],
['u022', 'm', '23', '1', 'fwd'],
['u023', 'f', '21', '1', 'bwd'],
['u024', 'm', '20', '1', 'fwd'],
['u025', 'm', '21', '1', 'bwd'],
['u026', 'm', '21', '1', 'fwd'],
['u027', 'm', '19', '1', 'fwd'],
['u028', 'm', '22', '1', 'fwd'],
['u028', 'm', '22', '2', 'bwd'],
['u029', 'm', '19', '1', 'bwd'],
['u029', 'm', '21', '1', 'bwd'],
['u030', 'f', '19', '1', 'bwd'],
['u030', 'f', '19', '3', 'fwd'],
['u031', 'm', '24', '1', 'fwd'],
['u032', 'f', '20', '1', 'fwd'],
['u033', 'm', '21', '1', 'fwd'],
['u034', 'f', '20', '1', 'bwd'],
['u035', 'm', '20', '1', 'fwd'],
['u035', 'm', '20', '2', 'bwd'],
['u036', 'm', '19', '1', 'fwd'],
['u037', 'f', '19', '1', 'bwd'],
['u038', 'f', '23', '1', 'fwd'],
['u039', 'm', '21', '1', 'bwd'],
['u040', 'f', '25', '1', 'bwd'],
['u041', 'f', '22', '1', 'bwd'],
['u042', 'm', '21', '1', 'fwd'],
['u043', 'm', '20', '1', 'bwd'],
['u043', 'm', '20', '2', 'fwd'],
['u044', 'f', '20', '1', 'fwd'],
['u045', 'f', '40', '1', 'bwd'],
['u046', 'm', '39', '1', 'fwd'],
['u046', 'm', '39', '2', 'bwd'],
['u047', 'm', '20', '1', 'bwd'],
['u048', 'm', '21', '1', 'bwd']
]

































from config import *
from function import *

def get_total_frame(path = CRCNS_frame_path):
    all_frame = 0
    all_data = []
    f = open(path)
    lines = f.readlines()
    for line in lines:
        line = line.split()
        all_data.append(line)

    for i_video in range(1, 51):
        all_frame += float(all_data[i_video][1])
        print(all_data[i_video][1])

    all_frame = all_frame - CRCNS_trash_frame * CRCNS_video_num
    print(">>>> total_valid_frame: %d"%all_frame)
    a = 1

def get_video_frame(video_name, path = CRCNS_frame_path):
    all_frame = 0
    all_data = []
    f = open(path)
    lines = f.readlines()
    for line in lines:
        line = line.split()
        all_data.append(line)

    for i_video in range(1, 51):

        if video_name == all_data[i_video][0][:-4]:
            frame_num = all_data[i_video][1]

    return int(frame_num)



def get_subject_list(path = CRCNS_data_path):
    f =  get_dirs(path)
    for i in f:
        print("'%s',"%i)


def get_video_list(path = CRCNS_frame_path):
    all_frame = 0
    all_data = []
    f = open(path)
    lines = f.readlines()
    for line in lines:
        line = line.split()
        all_data.append(line)

    for i_video in range(1, 51):
        video_name = all_data[i_video][0]
        print("'%s',"%video_name)

    a = 1

def get_all_valid_fixation(path = CRCNS_data_path):

    all_data = []
    all_fixation_num = 0
    for i_subject in range(len(CRCNS_subjects)):
    # for i_subject in range(7, 8):
        subject_name = CRCNS_subjects[i_subject]

        for i_video in range(len(CRCNS_video_list)):
        # for i_video in range(0, 4):

            # !!!!!!!!!!!!!!!! remember to clear each time
            all_data = []
            video_name = CRCNS_video_list[i_video][:-4]
            video_frame = get_video_frame(video_name)

            try:
                data_path = (path + '/' + subject_name + '/' +
                             video_name + '.e-ceyeS')

                f = open(data_path, 'r')
                lines = f.readlines()
                for line in lines:
                    line = line.split()
                    all_data.append(line)
                ## !!! remenber to close each time
                f.close()

                record_eye_num = len(all_data) - 3
                record_each_frame =  record_eye_num/video_frame

                for i_frame in range(271, video_frame):

                    frame_start =  int(i_frame * record_each_frame) + 3
                    frame_end =  int((i_frame+1) * record_each_frame) + 3
                    # print("===i_subject: %d, i_video: %d, frame_start: %d, "
                    #       "frame_end: %d, record_eye_num: %d"%(i_subject,
                    #     i_video, frame_start, frame_end, record_eye_num))
                    if frame_end >= record_eye_num:
                        frame_end = record_eye_num  - 1

                    for i_fixation_frame in range(frame_start, frame_end):
                        if float(all_data[i_fixation_frame][3]) == 0:
                            all_fixation_num += 1
                            break
                        else:
                            pass
                            # print(">>> debug:", all_data[i_fixation_frame][3])

                    # satart_frame = CRCNS_trash_frame + 3
                    # fixation_each_frame =

                print("video_frame: %d, i_video: %d, record_eye_num: "
                      "%d, frame_start: %d, frame_end: %d"%
                      (video_frame, i_video, record_eye_num, frame_start, frame_end))
            except Exception as e:
                print(">>>>>>>> file error: %s, i_video: %d, record_eye_num: "
                      "%d, frame_start: %d, frame_end: %d"%
                      (e, i_video, record_eye_num, frame_start, frame_end))

        print('================================ i_subject: %d i_video: %s, fix_num: %d' % (
            i_subject, i_video, all_fixation_num))



def main():

    # get_total_frame()
    get_all_valid_fixation()
    # for i_video in range(len(CRCNS_video_list)):
    #     video_name = CRCNS_video_list[i_video][:-4]
    #     get_all_valid_fixation(video_name, path=CRCNS_frame_path)







if __name__ == "__main__":
    main()

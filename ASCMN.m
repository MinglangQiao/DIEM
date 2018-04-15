clear all;
close all;
disp('======================== begin =================================')

all_frame = 0;
all_fixations = 0;

for i = 1:24
    i_video = strcat('raw_data_video', num2str(i));
    i_video = strcat(i_video, '.mat');
    data = load(i_video);
    n_frames = data.nFrames
    all_frame = all_frame + n_frames;
    one_video_data = data.raw_data;
    one_video_subject = length(one_video_data(1, 1, :));
    
    for i_subject = 1:one_video_subject
       one_subject_data = one_video_data(:, :, i_subject);
       
       for i_frame = 1:n_frames 
           one_frame_x = one_subject_data(1, i_frame);
           one_frame_y = one_subject_data(2, i_frame);
           
           if one_frame_x ~= -1 & one_frame_y  ~= -1
               all_fixations = all_fixations + 1;
           end
           
       end
    end
end
all_fixations
all_frame 
ave_fixation = all_fixations / all_frame
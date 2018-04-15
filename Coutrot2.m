data1 = load('coutrot_database2.mat');

all_data = data1.Coutrot_Database2;
one_mode_data =  all_data.Visual;
all_video_frame = [];
all_video_fixation = 0;

for i=1:15
   i_video = strcat('clip_', num2str(i));
   one_video_data = one_mode_data.(i_video);
   one_video_eye_data = one_video_data.data;
   one_video_config_data = one_video_data.info;
   one_video_frame = one_video_config_data.nframe;
   all_video_frame = [all_video_frame, one_video_frame];
   one_video_subject = length(one_video_eye_data(1, 1, :));
   
   for i_subject = 1:one_video_subject
       one_subject_data = one_video_eye_data(:, :, i_subject);
       
       for i_frame = 1:one_video_frame
           one_frame_x = one_subject_data(1, i_frame);
           one_frame_y = one_subject_data(2, i_frame);
           
           if one_frame_x ~= 'NaN' & one_frame_y  ~= 'NaN'
               all_video_fixation = all_video_fixation + 1;
           end
           
       end
       
       
   end
      
end


one_mode_data_Audio =  all_data.AudioVisual;
all_video_frame_Audio = [];
all_video_fixation_Audio = 0;

for i=1:15
   i_video_Audio = strcat('clip_', num2str(i));
   one_video_data_Audio = one_mode_data_Audio.(i_video_Audio);
   one_video_eye_data_Audio = one_video_data_Audio.data;
   one_video_config_data_Audio = one_video_data_Audio.info;
   one_video_frame_Audio = one_video_config_data_Audio.nframe;
   all_video_frame_Audio = [all_video_frame_Audio, one_video_frame_Audio];
   one_video_subject_Audio = length(one_video_eye_data_Audio(1, 1, :));
   
   for i_subject = 1:one_video_subject_Audio
       one_subject_data_Audio = one_video_eye_data_Audio(:, :, i_subject);
       
       for i_frame = 1:one_video_frame_Audio
           one_frame_x = one_subject_data_Audio(1, i_frame);
           one_frame_y = one_subject_data_Audio(2, i_frame);
           
           if one_frame_x ~= 'NaN' & one_frame_y  ~= 'NaN'
               all_video_fixation_Audio = all_video_fixation_Audio + 1;
           end
           
       end
       
       
   end
      
end

%% get the frams
total_frames = 0;
for i = 1: 15
    total_frames = total_frames + max( all_video_frame_Audio(i),  all_video_frame(i)); 
end

total_fixation = all_video_fixation + all_video_fixation_Audio
















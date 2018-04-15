data1 = load('coutrot_database1.mat');

all_mode_fixation = 0;
all_mode_frame = [];
for i_mode= 1: 5
    all_data = data1.Coutrot_Database1;
    mode = {'LandscapesSounds', 'FacesSounds', 'SameCatSounds', 'OriginalSounds', 'MovObjectsSounds'};
    one_mode_data = all_data.(mode{i_mode});
    mode_len = length(fieldnames(one_mode_data));
    one_video_modes = fieldnames(one_mode_data);

    all_video_frame = [];
    all_video_fixation = 0;

    for i=1:60
       i_video = strcat('clip_', num2str(i));
       if  ismember(i_video, one_video_modes) == 1
             disp(i_video)
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
           
       else
           all_video_frame = [all_video_frame, 0];
       end 
    end
    all_mode_fixation = all_mode_fixation + all_video_fixation;
    all_mode_frame{i_mode} = all_video_frame;
end

all_frame = [];
for i_video= 1:60
    one_mode_frame = [];
    for i_mode= 1:5
       one_mode_frame = [one_mode_frame, all_mode_frame{i_mode}(i_video)];
    end
    
    all_frame(i_video) = max(one_mode_frame);
end

all_frames = sum(all_frame)

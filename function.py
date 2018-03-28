import numpy as np
import os
from video_subjects import *


def get_dir_files(file_path):

    f = []
    for root, dirs, files in  os.walk(file_path):
        f = dirs
        break

    return  f


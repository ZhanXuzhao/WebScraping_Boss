__author_ = "zhanxuzhao"
import time
import os


def create_csv_file_path_by_time(suffix):
    dir_path = get_up_level_dir_path(__file__) + "/data"
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    file_path = dir_path + "/%s_job_info_%s.csv" % (time.strftime("%Y%m%d_%H%M", time.localtime()), suffix)
    return file_path


def get_dir_path(file):
    return os.path.dirname(file)


def get_up_level_dir_path(file):
    return os.path.dirname(get_dir_path(file))


if __name__ == "__main__":
    print(create_csv_file_path_by_time())

import csv
import os
import matplotlib.pyplot as plt
import numpy as np

from main import FileUtil


def resolve_chinese_problem():
    # 中文乱码处理
    # https://www.zhihu.com/question/25404709
    from matplotlib.font_manager import _rebuild
    _rebuild()  # reload一下
    # 指定默认字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family'] = 'sans-serif'
    # 用来正常显示负号
    plt.rcParams['axes.unicode_minus'] = False


resolve_chinese_problem()


def analyze_csv(file_path, index, value):
    with open(file_path, encoding="utf-8") as file:
        reader = csv.reader(file)
        salary_sum = 0
        count = 0
        for row in reader:
            if row[index] == value:
                salary_sum += float(row[2])
                count += 1
        ave_salary = salary_sum / count
        return ave_salary


def get_ave_salary_and_count(file_path, index, value):
    with open(file_path, encoding="utf-8") as file:
        reader = csv.reader(file)
        salary_sum = 0
        count = 0
        for row in reader:
            if row[index] == value:
                salary_sum += float(row[2])
                count += 1
        if count == 0:
            ave_salary = 0
        else:
            ave_salary = salary_sum / count
        return ave_salary, count


def show_average_salary_by_custom_dimension(file_path, dimension_desc):
    title = dimension_desc[0]
    index = dimension_desc[1]
    labels = dimension_desc[2]
    ave_salary_list = []
    count_list = []
    for option in labels:
        ave_salary_and_count = get_ave_salary_and_count(file_path, index, option)
        ave_salary_list.append(ave_salary_and_count[0])
        count_list.append(ave_salary_and_count[1])

    # draw_pie(title, labels, count_list)
    # draw_bar(title, 'Average salary (k)', labels, ave_salary_list)
    # draw_line(title, 'Average salary (k)', labels, count_list)

    draw_bar_and_line(title, labels, ave_salary_list, count_list)


def draw_bar_and_line(title, labels, bar_values, line_values):
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle(title)
    axs[0].bar(labels, bar_values)
    axs[1].plot(labels, line_values)
    plt.show()


def draw_bar(title, y_label, labels, values):
    plt.ylabel(y_label)
    plt.title(title)
    x_position = np.arange(len(labels))
    plt.bar(x_position, values)
    plt.xticks(x_position, labels)
    draw_value_label(values)
    plt.show()


# 为每个条形图添加数值标签
def draw_value_label(values):
    for i in np.arange(len(values)):
        salary = values[i]
        plt.text(i, salary, '%s' % round(salary, 1), ha='center')


def draw_pie(title, labels, values):
    plt.title(title)
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.show()


def draw_line(title, y_label, labels, values):
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot(labels, values)
    draw_value_label(values)
    plt.show()


def get_file_path():
    global last_file_path
    data_dir_path = FileUtil.get_up_level_dir_path(__file__) + "/data"
    listdir = os.listdir(data_dir_path)
    last_file_name = listdir[-1]
    last_file_path = data_dir_path + "/" + last_file_name
    print(last_file_path)
    return last_file_path


# 北京,Android,22.5,3-5年,本科,互联网,B轮,100-499人,北京雷石
dimension_city = ["城市", 0, ["北京", "上海", "广州", "深圳", "杭州"]]
dimension_experience = ["工作经验", 3, ["不限", "应届生", "1年以内", "1-3年", "3-5年", "5-10年", "10年以上"]]

if __name__ == '__main__':
    show_average_salary_by_custom_dimension(get_file_path(), dimension_experience)

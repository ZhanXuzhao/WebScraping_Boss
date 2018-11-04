import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import re

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


def get_ave_salary_and_count(file_path, index, value, fuzzy=True):
    with open(file_path, encoding="utf-8") as file:
        reader = csv.reader(file)
        salary_sum = 0
        count = 0
        for row in reader:
            if fuzzy_match(value, row[index], fuzzy):
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
    print(ave_salary_list, count_list)
    draw_bar(title, 'Average salary (k)', labels, ave_salary_list)
    # draw_line(title, 'Job counts', labels, count_list)
    # draw_bar_and_line(title, labels, ave_salary_list, count_list)


def draw_bar_and_line(title, labels, bar_values, line_values):
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))
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


def get_file_path(file_index):
    global file_path
    data_dir_path = FileUtil.get_up_level_dir_path(__file__) + "/data"
    listdir = sorted(os.listdir(data_dir_path))
    print(listdir)
    file_name = listdir[file_index]
    file_path = data_dir_path + "/" + file_name
    print(file_path)
    return file_path


def fuzzy_match(pattern, string, fuzzy):
    print(pattern, string)
    pattern = pattern.replace("+","\+")
    if pattern == "H5":
        pattern = "H.*5"
    if fuzzy:
        if re.search(pattern, string, re.IGNORECASE):
            value = True
        else:
            value = False
    else:
        value = pattern == string
    return value


# 北京,Android,22.5,3-5年,本科,互联网,B轮,100-499人,北京雷石
dimension_city = ["Android平均月薪 vs 地区", 0, ["北京", "上海", "广州", "深圳", "杭州"]]
dimension_work_experience = ["Android平均月薪 vs 工作年限（北京）", 3, ["应届生", "1年以内", "1-3年", "3-5年", "5-10年", "10年以上"]]
dimension_education_experience = ["Android平均月薪 vs 学历", 4, ["大专", "本科", "硕士", "博士"]]
dimension_financing_state = ["Android平均月薪 vs 融资阶段", 6, ["未融资", "天使轮", "A轮", "B轮", "C轮", "D轮及以上", "已上市", "不需要融资"]]
dimension_company_size = ["Android平均月薪 vs 公司规模", 7,
                          ["0-20人", "20-99人", "100-499人", "500-999人", "1000-9999人", "10000人以上"]]
dimension_job = ["不同技术岗位 平均月薪", 1, ["Java", "PHP", "C++", "C#", "Python", "H5", "Android", "iOS", "Web前端"]]

if __name__ == '__main__':
    # show_average_salary_by_custom_dimension(get_file_path(0), dimension_city)
    # show_average_salary_by_custom_dimension(get_file_path(1), dimension_work_experience)
    # show_average_salary_by_custom_dimension(get_file_path(2), dimension_education_experience)
    # show_average_salary_by_custom_dimension(get_file_path(3), dimension_financing_state)
    # show_average_salary_by_custom_dimension(get_file_path(4), dimension_company_size)
    show_average_salary_by_custom_dimension(get_file_path(5), dimension_job)

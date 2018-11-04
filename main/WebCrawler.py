import csv
import time
from urllib import request
from bs4 import BeautifulSoup
from main import FileUtil

# constants
encoding = "utf-8"
headers = {
    # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}  # windows
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}  # mac
_page_interval = 1  # crawl page interval

# static data
host = "https://www.zhipin.com"
bj = "/c101010100-p100202/?ka=sel-city-101010100"
sh = "/c101020100-p100202/?ka=sel-city-101020100"
gz = "/c101280100-p100202/?ka=sel-city-101280100"
sz = "/c101280600-p100202/?ka=sel-city-101280600"
hz = "/c101210100-p100202/?ka=sel-city-101210100"
# city_url_array = [bj, sh, gz, sz, hz]
city_url_array = [bj]


def crawl_job_info_from_url_list(file_path, url_array, auto_crawl_next=True):
    with open(file_path, 'w+', encoding=encoding, newline="") as csv_file:
        writer = csv.writer(csv_file)
        for city in url_array:
            crawl_job_info_from_url(city, writer, auto_crawl_next)
    print("crawl_job_info_from_url_list finish")


def crawl_job_info_from_url(url_path, writer, auto_crawl_next=True):
    while True:
        url_path = write_job_info_and_get_next_url_path(url_path, writer)
        time.sleep(_page_interval)
        if (not auto_crawl_next) or (url_path is None):
            break


def write_job_info_and_get_next_url_path(url, writer):
    complete_url = host + url
    print("crawl page:%s" % complete_url)
    soup = get_soup(complete_url)
    write_job_info(writer, soup)
    next_url_path = get_next_url_path(soup)
    return next_url_path


def get_next_url_path(soup):
    a_next = soup.find("a", {"class", "next"})
    if a_next is None:
        return None
    else:
        href = a_next.attrs['href']
        if href == "javascript:;":
            return None
        else:
            return href


def get_soup(path):
    req = request.Request(url=path, headers=headers)
    html = request.urlopen(req)
    # mac 上面一行代码报错 请在terminal中执行下面一行命令（注意替换对应的Python版本号）reference -> https://github.com/tensorflow/tensorflow/issues/10779
    # /Applications/Python\ 3.7/Install\ Certificates.command
    soup = BeautifulSoup(html.read(), features="html.parser")
    return soup


def write_job_info(writer, soup):
    job_primary_divs = soup.findAll("div", {"class", "job-primary"})
    for job_primary in job_primary_divs:

        # title and salary
        job_title_and_salary = job_primary.div.h3.a
        salary = job_title_and_salary.span.get_text()
        ave_salary = get_ave_salary(salary)

        # primary info
        primary_div = job_primary.find("div", {"class", "info-primary"})
        primary_p = primary_div.p
        title = primary_div.h3.a.div.get_text()
        info_primary_arr = primary_p.get_text("|").split("|")
        locations = info_primary_arr[0].split(" ")
        location = locations[0]
        work_exp = info_primary_arr[1]
        education = info_primary_arr[2]

        # company info
        company_text_div = job_primary.find("div", {"class", "info-company"}).div
        company_name = company_text_div.h3.a.get_text()
        company_info_arr = company_text_div.p.get_text("|").split("|")
        if len(company_info_arr) == 3:
            company_info_arr2 = [company_info_arr[0], company_info_arr[1], company_info_arr[2], company_name]
        else:
            company_info_arr2 = [company_info_arr[0], "", company_info_arr[1], company_name]

        # combine to one row
        row = [location, title, ave_salary, work_exp, education] + company_info_arr2
        print(row)
        writer.writerow(row)


def get_ave_salary(s):
    s = s.replace("k", "")
    split = s.split("-")
    ave_salary = (int(split[0]) + int(split[1])) / 2
    return ave_salary


if __name__ == '__main__':
    crawl_job_info_from_url_list(city_url_array, False)

from main import WebCrawler, FileUtil

bj = "/c101010100-p100202/?ka=sel-city-101010100"
sh = "/c101020100-p100202/?ka=sel-city-101020100"
gz = "/c101280100-p100202/?ka=sel-city-101280100"
sz = "/c101280600-p100202/?ka=sel-city-101280600"
hz = "/c101210100-p100202/?ka=sel-city-101210100"
city_url_array = [bj, sh, gz, sz, hz]

file_path = FileUtil.create_csv_file_path_by_time("in_different_cities")
WebCrawler.crawl_job_info_from_url_list(file_path, city_url_array, False)

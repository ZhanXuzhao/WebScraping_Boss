from main import WebCrawler

bj = "/c101010100-p100202/?ka=sel-city-101010100"
sh = "/c101020100-p100202/?ka=sel-city-101020100"
gz = "/c101280100-p100202/?ka=sel-city-101280100"
sz = "/c101280600-p100202/?ka=sel-city-101280600"
hz = "/c101210100-p100202/?ka=sel-city-101210100"
city_url_array = [bj, sh, gz, sz, hz]

WebCrawler.crawl_job_info_from_url_list(city_url_array)

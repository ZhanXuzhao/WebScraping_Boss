from main import WebCrawler, FileUtil

bj = "/c101010100-p100202/?ka=sel-city-101010100"
sh = "/c101020100-p100202/?ka=sel-city-101020100"
gz = "/c101280100-p100202/?ka=sel-city-101280100"
sz = "/c101280600-p100202/?ka=sel-city-101280600"
hz = "/c101210100-p100202/?ka=sel-city-101210100"
city_url_array = [bj, sh, gz, sz, hz]

bj_yingjiesheng = "/c101010100-p100202/e_102/?ka=sel-exp-102"
bj_0_1year = "/c101010100-p100202/e_103/?ka=sel-exp-103"
bj_1_3_year = "/c101010100-p100202/e_104/?ka=sel-exp-104"
bj_3_5_year = "/c101010100-p100202/e_105/?ka=sel-exp-105"
bj_5_10_year = "/c101010100-p100202/e_106/?ka=sel-exp-106"
bj_10_n_year = "/c101010100-p100202/e_107/?ka=sel-exp-107"
bj_work_exp_array = [bj_yingjiesheng, bj_0_1year, bj_1_3_year, bj_3_5_year, bj_5_10_year, bj_10_n_year]

bj_edu_exp_dazhuan = "/c101010100-p100202/d_202/?ka=sel-degree-202"
bj_edu_exp_benke = "/c101010100-p100202/d_203/?ka=sel-degree-203"
bj_edu_exp_shuoshi = "/c101010100-p100202/d_204/?ka=sel-degree-204"
bj_edu_exp_boshi = "/c101010100-p100202/d_205/?ka=sel-degree-205"
bj_edu_exp_array = [bj_edu_exp_dazhuan, bj_edu_exp_benke, bj_edu_exp_shuoshi, bj_edu_exp_boshi]

bj_financing_weirongzi = "/c101010100-p100202/t_801/?ka=sel-stage-801"
bj_financing_tianshi = "/c101010100-p100202/t_802/?ka=sel-stage-802"
bj_financing_a = "/c101010100-p100202/t_803/?ka=sel-stage-803"
bj_financing_b = "/c101010100-p100202/t_804/?ka=sel-stage-804"
bj_financing_c = "/c101010100-p100202/t_805/?ka=sel-stage-805"
bj_financing_d = "/c101010100-p100202/t_806/?ka=sel-stage-806"
bj_financing_shangshi = "/c101010100-p100202/t_807/?ka=sel-stage-807"
bj_financing_buxuyao = "/c101010100-p100202/t_808/?ka=sel-stage-808"
bj_financing_array = [bj_financing_weirongzi, bj_financing_tianshi, bj_financing_a, bj_financing_b, bj_financing_c,
                      bj_financing_d, bj_financing_shangshi, bj_financing_buxuyao]

bj_company_size_20 = "/c101010100-p100202/s_301/?ka=sel-scale-301"
bj_company_size_99 = "/c101010100-p100202/s_302/?ka=sel-scale-302"
bj_company_size_499 = "/c101010100-p100202/s_303/?ka=sel-scale-303"
bj_company_size_999 = "/c101010100-p100202/s_304/?ka=sel-scale-304"
bj_company_size_9999 = "/c101010100-p100202/s_305/?ka=sel-scale-305"
bj_company_size_10000_plus = "/c101010100-p100202/s_306/?ka=sel-scale-306"
bj_company_size_array = [bj_company_size_20, bj_company_size_99, bj_company_size_499, bj_company_size_999,
                         bj_company_size_9999, bj_company_size_10000_plus]

bj_job_backend_java = "/job_detail/?query=&scity=101010100&industry=&position=100101"
bj_job_backend_cpp = "/job_detail/?query=&scity=101010100&industry=&position=100102"
bj_job_backend_php = "/job_detail/?query=&scity=101010100&industry=&position=100103"
bj_job_backend_cshap = "/job_detail/?query=&scity=101010100&industry=&position=100106"
bj_job_backend_python = "/job_detail/?query=&scity=101010100&industry=&position=100109"
bj_job_front_end_h5 = "/job_detail/?query=&scity=101010100&industry=&position=100201"
bj_job_front_end_android = "/job_detail/?query=&scity=101010100&industry=&position=100202"
bj_job_front_end_ios = "/job_detail/?query=&scity=101010100&industry=&position=100203"
bj_job_front_end_web_front = "/job_detail/?query=&scity=101010100&industry=&position=100205"
bj_job_array = [bj_job_backend_java, bj_job_backend_cpp, bj_job_backend_php,
                       bj_job_backend_cshap, bj_job_backend_python, bj_job_front_end_h5,
                       bj_job_front_end_android, bj_job_front_end_ios, bj_job_front_end_web_front]

# WebCrawler.crawl_job_info_from_url_list("different_city", city_url_array)
# WebCrawler.crawl_job_info_from_url_list("different_work_experience_in_beijing",bj_work_exp_array)
# WebCrawler.crawl_job_info_from_url_list("different_education_experience_in_beijing", bj_edu_exp_array)
# WebCrawler.crawl_job_info_from_url_list("different_finance_state_in_beijing", bj_financing_array)
# WebCrawler.crawl_job_info_from_url_list("different_company_size_in_beijing", bj_company_size_array)
WebCrawler.crawl_job_info_from_url_list("different_job_in_beijing", bj_job_array, True)

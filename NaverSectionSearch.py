__author__ = "Foleevora"
__version__ = "1.0.0"
__email__ = "foleevora@gmail.com"

import sys
from selenium import webdriver

def help():
    print("USAGE: naverPopularSearches.py [KeyWord] or [Help]")
    print("KeyWord : ")
    print("[Entertainment] == TV오락")
    print("[Shopping]      == 쇼핑")
    print("[Movie]         == 영화")
    print("[Car]           == 자동차")
    print("[Game]          == 게임")
    print("[Singleman]     == 싱글남")
    print("[Singlewoman]   == 싱글녀")
    print("[Housewife]     == 주부")
    print("[Collegian]     == 대학생")
    print("[Teenager]      == 청소년")

def parsing(options):

    options_map = {
        "Entertainment":0,
        "Shopping":1,
        "Movie":2,
        "Car":3,
        "Game":4,
        "Singleman":5,
        "Singlewoman":6,
        "Housewife":7,
        "Collegian":8,
        "Teenager":9
    }

    driver = webdriver.PhantomJS()
    driver.set_window_size(1120, 550)
    driver.get("http://datalab.naver.com/keyword/sectionSearch.naver")

    elem_list = driver.find_element_by_class_name("keyword_tab_list")
    elems = elem_list.find_elements_by_tag_name("li")
    elem = elems[options_map[options]]

    a_tag = elem.find_element_by_tag_name("a")
    a_tag.click()

    elems = driver.find_elements_by_class_name("sub_title")

    for index, elem in enumerate(elems):
        a_tag = elem.find_element_by_tag_name("a")
        title = a_tag.find_element_by_class_name("title")
        title_index = index + 1
        print(("%2d위 : " + title.text) % title_index)

if __name__ == "__main__":

    if len(sys.argv) is not 2:
        print("UASGE: NaverSectionSearch.py [KeyWord] or [Help]")
    elif sys.argv[1] == "Help":
        help()
    else:
        parsing(sys.argv[1])

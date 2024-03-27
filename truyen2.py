from function.spliceString import cut_string
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from function.get_audio import get_audio
from function.make_video import make_video
from function.dele_mp3 import dele_mp3

# bien arr dem so file mp3 cua 10 chap
arr_count_file_mp3 = []
def initWebTruyen(driver):
    # Sử dụng trình duyệt
    driver.get(
        "https://chromewebstore.google.com/detail/b%E1%BA%ADt-sao-ch%C3%A9p-m%E1%BB%8Di-n%C6%A1i/nahkcohcfljjjkhdcbfdphegdoiflbjd?hl=vi&utm_source=ext_sidebar")

    # Chờ đợi cho đến khi phần tử xuất hiện
    wait = WebDriverWait(driver, 10)
    btn_add_to_chrome = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.UywwFc-LgbsSe.UywwFc-LgbsSe-OWXEXe-dgl2Hf')))
    btn_add_to_chrome.click()
    time.sleep(5)
    # Lấy danh sách các cửa sổ mà trình duyệt đang mở
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[0])
    time.sleep(2)


def get_content_chap(driver):
    time.sleep(3)
    wait = WebDriverWait(driver, 10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Lấy nội dung chương
    name_chap = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'book-title')))[1].text
    content = wait.until(EC.presence_of_element_located((By.ID, 'bookContentBody'))).text

    return name_chap+". "+content


def all_action_text(url, end_chater, number_in_chap):
    driver = webdriver.Chrome()
    initWebTruyen(driver)
    wait = WebDriverWait(driver, 10)

    driver.get(url)
    time.sleep(4)
    chapter_texts = []

    for i in range(1,end_chater):
        chapter_text = get_content_chap(driver)
        # arr_text = cut_string(chapter_text)
        chapter_texts.append(chapter_text)

        btn_next_chap = wait.until(
            EC.presence_of_element_located((By.ID, "btnNextChapter")))
        # print(btn_next_chap)
        btn_next_chap.click()
        print('next chap')
        # Tạo thư mục "text" nếu nó chưa tồn tại
    text_directory = "text"
    if not os.path.exists(text_directory):
        os.makedirs(text_directory)


    count_file_text = 0
    # Lặp qua danh sách các đoạn văn và lưu vào các tệp văn bản
    for i, chapter_text in enumerate(chapter_texts, start=1):
        arr = cut_string(chapter_text)
        count_file_text += len(arr)
        if i % number_in_chap == 0:
            arr_count_file_mp3.append(count_file_text)
            count_file_text = 0

        for index, item in enumerate(arr, start=1):
            filename = os.path.join(text_directory, f"chapter_{i}_{index}.txt")
            with open(filename, "w", encoding="utf-8") as file:
                file.write(item)
                print(f"Dữ liệu của chương đã được lưu vào tệp {filename}")

    if count_file_text != 0:
        arr_count_file_mp3.append(count_file_text)
    driver.quit()
    print(arr_count_file_mp3)
    with open('arr_count_file_mp3.txt', 'w') as file:
        for value in arr_count_file_mp3:
            file.write(f"{value}\n")

name = 'dai_su_huynh'
all_action_text(r'https://truyenwikidich.net/truyen/cau-o-ma-tong-nam-vung-tu-tien/chuong-101-nam-kha-1-mong-van-0-thi-hai-ZJZv3cQsRGREqn0L',23,10)

download_folder = r"C:\Users\Admin\Downloads"
path_to_save_mp3 = rf"C:\Users\Admin\Downloads\audio_{name}"
output_video_folder = rf'D:\truyen\{name}'
# get_audio(path_to_save_mp3,download_folder)

# make_video(101,arr_count_file_mp3, './dai_su_huynh.png', path_to_save_mp3 , output_video_folder,10)
# dele_mp3(path_to_save_mp3)
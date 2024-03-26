from function.spliceString import cut_string
from function.getText import initWebTruyen, get_content_chap
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
import os

def all_action_text(start_chapter,end_chapter, base_url,number_chapter_in_video):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    chapter_texts = []
    initWebTruyen(driver)

    for i in range(start_chapter, end_chapter):
        url = f'{base_url}-{i}'
        text = get_content_chap(driver, url)
        chapter_texts.append(text)

    # Tạo thư mục "text" nếu nó chưa tồn tại
    text_directory = "text"
    if not os.path.exists(text_directory):
        os.makedirs(text_directory)

    # bien arr dem so file mp3 cua 10 chap
    arr_count_file_mp3 = []
    count_file_text = 0
    # Lặp qua danh sách các đoạn văn và lưu vào các tệp văn bản
    for i, chapter_text in enumerate(chapter_texts, start=1):
        arr = cut_string(chapter_text)
        count_file_text += len(arr)
        if i % number_chapter_in_video == 0:
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
    with open('arr_count_file_mp3.txt','w') as file:
        for value in arr_count_file_mp3:
            file.write(f"{value}\n")
    return arr_count_file_mp3
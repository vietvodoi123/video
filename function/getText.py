
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def initWebTruyen(driver):
    # Sử dụng trình duyệt
    driver.get(
        "https://chromewebstore.google.com/detail/b%E1%BA%ADt-sao-ch%C3%A9p-m%E1%BB%8Di-n%C6%A1i/mmpljcghnbpkokhbkmfdmoagllopfmlm?hl=vi&utm_source=ext_sidebar")

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


def get_content_chap(driver, url):
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    # Kiểm tra xem phần tử có nội dung là "Loading..." có xuất hiện không
    print('loading',url)

    # Lấy nội dung chương
    name_chap = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.nh-read__title'))).text
    chap_content = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.c-c'))).text
    time.sleep(2)

    return name_chap + '. ' + chap_content

# driver = webdriver.Chrome()
#
# chapter_texts =[]
# initWebTruyen(driver)
# for i in range(120,130):
#     url = f'https://metruyencv.com/truyen/thinh-cong-tu-tram-yeu/chuong-{i}'
#     text = get_content_chap(driver,url)
#     chapter_texts.append(text)
#
#
# for i,chapter_text in enumerate(chapter_texts,start=1):
#     arr = cut_string(chapter_text)
#     for index, item in enumerate(arr, start=1):
#         filename = f"chapter_{i}_{index}.txt"
#         with open(filename, "w", encoding="utf-8") as file:
#             file.write(item)
#             print(f"Dữ liệu của chương {index} đã được lưu vào tệp {filename}")
#
# driver.quit()
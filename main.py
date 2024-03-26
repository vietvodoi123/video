from function.all_action_text import all_action_text
from function.get_audio import get_audio
from function.make_video import make_video
from function.dele_mp3 import dele_mp3
import os

def all_action_in_here(truyen, start_chapter, end_chapter, number_chapter_in_video ):
    name = truyen['name']
    if not name:
        print("main,lỗi tên truyên")
        return
    download_folder = r"C:\Users\Admin\Downloads"
    path_to_save_mp3 = rf"C:\Users\Admin\Downloads\audio_{name}"
    output_video_folder = rf'D:\truyen\{name}'
    # Kiểm tra xem thư mục "audio" đã tồn tại chưa
    if not os.path.exists(path_to_save_mp3):
        os.makedirs(path_to_save_mp3)  # Tạo thư mục "audio" nếu chưa tồn tại
    # Kiểm tra xem thư mục đã tồn tại hay chưa
    if not os.path.exists(output_video_folder):
        os.makedirs(output_video_folder)  # Tạo thư mục nếu chưa tồn tại
    path_to_image = truyen['image_path']

    arr_count_file_mp3 = all_action_text(start_chapter, end_chapter, truyen['url'],number_chapter_in_video)
    # arr_count_file_mp3 = [10, 10]
    get_audio(path_to_save_mp3,download_folder)

    make_video(start_chapter,arr_count_file_mp3, path_to_image, path_to_save_mp3 , output_video_folder,number_chapter_in_video)
    dele_mp3(path_to_save_mp3)

def audio_err(truyen):
    print("loi lay audio")
    name = truyen['name']
    if not name:
        print("main,lỗi tên truyên")
        return
    download_folder = r"C:\Users\Admin\Downloads"
    path_to_save_mp3 = rf"C:\Users\Admin\Downloads\audio_{name}"
    get_audio(path_to_save_mp3, download_folder)

# 567
truyen_than_thoai_ki_nguyen = {
    'name': 'than_thoai_ky_nguyen',
    'url': 'https://metruyencv.com/truyen/than-thoai-ky-nguyen-ta-tien-hoa-thanh-hang-tinh-cap-cu-thu/chuong',
    'image_path': './undefined_image.png'
}
#
thinh_cong_tu_tram_yeu = {
    'name': 'thinh_cong_tu_tram_yeu',
    'url': 'https://metruyencv.com/truyen/thinh-cong-tu-tram-yeu/chuong',
    'image_path': './tram_yeu_1.png'
}

toan_dan_linh_chu = {
    'name': 'toan_dan_linh_chu',
    'url': 'https://metruyencv.com/truyen/toan-dan-linh-chu-bat-dau-che-tao-bat-hu-tien-vuc/chuong',
    'image_path': './toan_dan_lanh_chu.png'
}

do_de_xuong_nui = {
    'name': 'do_de_xuong_nui',
    'url': 'https://metruyencv.com/truyen/tong-vo-ta-de-tu-sau-khi-xuong-nui-giang-ho-dai-loan/chuong',
    'image_path': './de_tu_xuong_nui.png'
}
muc_long_su = {
    'name': 'muc_long_su',
    'url': 'https://metruyencv.com/truyen/muc-long-su/chuong',
    'image_path': './muc_long_su.png'
}
ta_ve_bua = {
    'name':"ta_ve_bua",
    'url':'https://metruyencv.com/truyen/ta-ve-ra-phu-luc-tat-bi-cam-dung/chuong',
    'image_path': './ta_ve_bua.png'
}
goc_chet_bi_an = {
    'name':'goc_chet_bi_an',
    'url':'https://metruyencv.com/truyen/goc-chet-bi-an/chuong',
    'image_path':'./goc_chet_bi_an.png'
}
mot_quyen = {
    'name':'mot_quyen',
    'url':'https://metruyencv.com/truyen/han-mot-quyen-oanh-sat-ma-than-nguoi-noi-han-la-muc-su/chuong',
    'image_path':'./mot_quyen_1.png'
}
try:
    all_action_in_here(mot_quyen, 91, 111, 10)
except Exception as e:
    # Xử lý lỗi và lấy nội dung lỗi
    error_message = str(e)
    print("Nội dung lỗi:", error_message)
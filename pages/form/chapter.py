from pages import *


def add_new_chapter(name, manga_id, cookies):
    st.title(f"Thêm chương mới cho Manga: {name}")
    total_chapter = get_total_chapter(manga_id)
    with st.form("new_chapter_form"):
        st.write(f"Hiện tại có tổng {total_chapter} chương đã đăng")
        number = st.text_input("Nhập số chương: ", None)
        title = st.text_input("Nhập tiêu đề: ", None)
        images_zip = st.file_uploader("Upload Zip", type=["zip"])

        if st.form_submit_button(label="Add Chapter"):
            add_chapter_api(manga_id, number, title, images_zip, cookies)

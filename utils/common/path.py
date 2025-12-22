import os
import datetime

def upload_path_media(base_folder: str):
    def _upload_path(instance, filename):
        today = datetime.date.today()
        path = os.path.join(base_folder, str(today.year), str(today.month), str(today.day))
        os.makedirs(path, exist_ok=True)
        return os.path.join(path, filename)
    return _upload_path


posted_upload_path = upload_path_media("Document/SaytgaJoylash")
word_order_upload_path = upload_path_media("Document/BuyurtmaWord")
signed_word_order_upload_path = upload_path_media("Document/Tasdiklangan/Word")
signed_pdf_order_upload_path = upload_path_media("Document/Tasdiklangan/Pdf")
template_upload_path = upload_path_media("Andoza/")
attachment_upload_path = upload_path_media("Document/QoshimchaFayllar/")

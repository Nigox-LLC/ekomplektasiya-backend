import os
import datetime


def _build_path(base_folder: str, filename: str) -> str:
    today = datetime.date.today()
    return os.path.join(
        base_folder,
        str(today.year),
        str(today.month),
        str(today.day),
        filename,
    )


def template_upload_path(instance, filename):
    return _build_path("Andoza", filename)


def posted_upload_path(instance, filename):
    return _build_path("Document/SaytgaJoylash", filename)


def word_order_upload_path(instance, filename):
    return _build_path("Document/BuyurtmaWord", filename)


def signed_word_order_upload_path(instance, filename):
    return _build_path("Document/Tasdiklangan/Word", filename)


def signed_pdf_order_upload_path(instance, filename):
    return _build_path("Document/Tasdiklangan/Pdf", filename)


def attachment_upload_path(instance, filename):
    return _build_path("Document/QoshimchaFayllar", filename)


def price_analysis_upload_path(instance, filename):
    return _build_path("Document/NarxTahlili", filename)


def org_info_upload_path(instance, filename):
    return _build_path("Document/TijoriyTaklif/ORG/", filename)


def stat_upload_path(instance, filename):
    return _build_path("Document/TijoriyTaklif/Stat/", filename)


def tk_file_upload_path(instance, filename):
    return _build_path("Document/TijoriyTaklif/TK/", filename)



def appeal_letter_doc_upload_path(instance, filename):
    return _build_path("Document/MurojaatXati/Doc/", filename)

def appeal_letter_pdf_upload_path(instance, filename):
    return _build_path("Document/MurojaatXati/Pdf/", filename)
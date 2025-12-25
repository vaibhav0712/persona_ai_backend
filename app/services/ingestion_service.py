from pathlib import Path
from helper import ingestion_helper


# WARNING : ONLY SUPPORTS CERTAIN HTML FILES
# WARNING : IP IS BLOCKED SO DDWNLOAD IS DISABLE
# THOUGHTS : SHOULD I SWITCH TO ONLY TEXT FILE? I WILL LOSS METADATA FEATURE THEN

# ONLY TEXT SUPPORT BRANCH


LOCAL_ZIP_FILE_PATH = (
    "/home/vaibhav/Documents/project_akira/temp/book_2680/pg2680-h.zip"
)
URL = "https://www.gutenberg.org/cache/epub/2680/pg2680-h.zip"

if __name__ == "__main__":
    url = URL
    book_id = ingestion_helper.extract_book_id_from_url(url)

    # zipfile_path = ingestion_helper.download_zip(url, book_id)
    zipfile_path = Path(LOCAL_ZIP_FILE_PATH)

    extracted_dir = ingestion_helper.extract_zip(zipfile_path)

    html_file_path = ingestion_helper.create_html_file_path(extracted_dir, book_id)

    json_file_path = ingestion_helper.html_to_json(html_file_path, book_id)

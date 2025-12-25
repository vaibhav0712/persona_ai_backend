import httpx
from pathlib import Path
import zipfile
from bs4 import BeautifulSoup
import json


# TODO : Update function more robust method
def extract_book_id_from_url(url):
    return url.split("/")[-2]


def download_zip(url, book_id):
    print(f"Downloading book {book_id} ...")
    res = httpx.get(url)

    zipfile_dir = Path.cwd().parent.parent / "temp" / f"book_{book_id}"
    zipfile_path = zipfile_dir / f"{book_id}.zip"
    Path(zipfile_dir).mkdir(parents=True, exist_ok=True)

    if res.status_code == httpx.codes.OK:
        with open(zipfile_path, "wb") as fp:
            fp.write(res.content)

    return zipfile_path


def extract_zip(zipfile_path):
    print(f"Extracting book...")
    extracted_dir = zipfile_path.parent
    with zipfile.ZipFile(zipfile_path, "r") as fp:
        fp.extractall(extracted_dir)

    return extracted_dir


def create_html_file_path(extracted_dir, book_id):
    return extracted_dir / f"pg{book_id}-images.html"


def extract_book_title(soup):
    book_title = soup.h1.text.strip()
    return book_title


def extract_book_chapters(soup):

    chapters = []

    for chapter in soup.find_all("div", class_="chapter"):
        if chapter.find("h2"):
            chapter_title = chapter.find("h2").text.strip()
            paragraphs = []
            for inx, para in enumerate(chapter.find_all("p")):
                para = para.text.strip()
                paragraphs.append({"id": inx, "length": len(para), "text": para})

            chapter_dict = {"chapter_title": chapter_title, "paragraphs": paragraphs}

            chapters.append(chapter_dict)

    return chapters


def html_to_json(html_file_path, book_id):
    print("Converting book from HTML to JSON ...")
    json_file_path = html_file_path.parent / f"{book_id}.json"
    with open(html_file_path) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    book_title = extract_book_title(soup=soup)
    book_chapters = extract_book_chapters(soup=soup)

    structured_book = {"book_tite": book_title, "chapters": book_chapters}

    with open(json_file_path, "w") as fp:
        json.dump(structured_book, fp)

    return json_file_path

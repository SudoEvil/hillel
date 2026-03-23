import os
import mimetypes
import requests
from urllib.parse import urlparse, unquote, quote

BASE_URL = "http://127.0.0.1:8080"

# POST
def upload_image(image_path: str) -> str:
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Файл не знайдено: {image_path}")

    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type:
        mime_type = "application/octet-stream"

    with open(image_path, "rb") as f:
        files = {"image": (os.path.basename(image_path), f, mime_type)}
        r = requests.post(f"{BASE_URL}/upload", files=files, timeout=15)

    if r.status_code != 201:
        raise RuntimeError(f"Upload failed: {r.status_code} {r.text}")

    data = r.json()
    image_url = data.get("image_url")
    if not image_url:
        raise RuntimeError(f"No image_url in response: {data}")

    return image_url


def extract_filename(image_url: str) -> str:
    parsed = urlparse(image_url)
    filename = parsed.path.split("/")[-1]
    return unquote(filename)


def get_image_url(filename: str) -> str:
    safe_filename = quote(filename)

    headers = {"Content-Type": "text"}

    r = requests.get(f"{BASE_URL}/image/{safe_filename}", headers=headers, timeout=15)

    if r.status_code != 200:
        raise RuntimeError(f"GET failed: {r.status_code} {r.text}")

    data = r.json()
    image_url = data.get("image_url")
    if not image_url:
        raise RuntimeError(f"No image_url in response: {data}")

    return image_url


def delete_image(filename: str) -> dict:
    safe_filename = quote(filename)
    r = requests.delete(f"{BASE_URL}/delete/{safe_filename}", timeout=15)

    if r.status_code != 200:
        raise RuntimeError(f"DELETE failed: {r.status_code} {r.text}")

    return r.json()


if __name__ == "__main__":
    IMAGE_PATH = "/Users/kseniaparshyna/Downloads/doll.png"

    print("1) POST /upload")
    uploaded_url = upload_image(IMAGE_PATH)
    print("   uploaded_url:", uploaded_url)

    filename = extract_filename(uploaded_url)
    print("   filename:", filename)

    print("2) GET /image/<filename> (Content-Type: text)")
    fetched_url = get_image_url(filename)
    print("   fetched_url:", fetched_url)

    print("3) DELETE /delete/<filename>")
    delete_resp = delete_image(filename)
    print("   delete_resp:", delete_resp)

    print("Done ✅")
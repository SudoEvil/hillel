import requests

BASE_URL = "https://images-api.nasa.gov"

#search images
search_url = f"{BASE_URL}/search"

search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

search_response = requests.get(search_url, params=search_params)
search_response.raise_for_status()

search_data = search_response.json()

# get nasa_id
items = search_data["collection"]["items"]

nasa_ids = []

for item in items:
    data_block = item.get("data", [])
    if data_block:
        nasa_id = data_block[0].get("nasa_id")
        if nasa_id:
            nasa_ids.append(nasa_id)


nasa_ids = nasa_ids[:2]

print("NASA IDs:", nasa_ids)


#get url

def get_jpg_url(nasa_id):
    asset_url = f"{BASE_URL}/asset/{nasa_id}"

    response = requests.get(asset_url)
    response.raise_for_status()

    asset_data = response.json()

    items = asset_data["collection"]["items"]

    # choose jpg
    for item in items:
        href = item.get("href")
        if href and href.lower().endswith(".jpg"):
            return href

    return None


#Download
for index, nasa_id in enumerate(nasa_ids, start=1):
    jpg_url = get_jpg_url(nasa_id)

    if jpg_url:
        print(f"Downloading: {jpg_url}")

        img_response = requests.get(jpg_url)
        img_response.raise_for_status()

        file_name = f"mars_photo{index}.jpg"

        with open(file_name, "wb") as f:
            f.write(img_response.content)

        print(f"Saved as {file_name}")
    else:
        print(f"No JPG found for {nasa_id}")
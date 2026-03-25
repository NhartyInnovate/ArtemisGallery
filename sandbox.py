import requests


def fetch_artworks():
    # 1. The API Endpoint (We are asking for 5 items, and only specific fields)
    url = "https://api.artic.edu/api/v1/artworks?limit=5&fields=id,title,artist_display,image_id,date_display,medium_display"

    # 2. Make the request
    print("Fetching data from the Art Institute of Chicago...")
    response = requests.get(url)

    # 3. Parse the JSON
    data = response.json()

    # The AIC API wraps the actual list of artworks inside a "data" key
    artworks = data.get("data", [])

    # 4. Loop through the artworks and clean the data
    print("\n--- ARTEMIS: ARCHIVE FETCH SUCCESSFUL ---\n")

    for art in artworks:
        title = art.get("title", "Unknown Title")
        artist = art.get("artist_display", "Unknown Artist")
        date = art.get("date_display", "Unknown Date")
        medium = art.get("medium_display", "Unknown Medium")
        image_id = art.get("image_id")

        # 5. The Data Mutator: Constructing the actual image URL
        # We only build the URL if an image_id actually exists
        if image_id:
            image_url = f"https://www.artic.edu/iiif/2/{image_id}/full/843,/0/default.jpg"
        else:
            image_url = "No image available for this piece."

        # 6. Print the formatted data to the terminal
        print(f"🎨 Title:  {title}")
        print(f"👤 Artist: {artist}")
        print(f"📅 Date:   {date}")
        print(f"🖌️ Medium: {medium}")
        print(f"🔗 Image:  {image_url}")
        print("-" * 40)


if __name__ == "__main__":
    fetch_artworks()
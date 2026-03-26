from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder="../templates")


@app.route("/")
def gallery():
    # 1. Capture user inputs, defaulting the page number to 1
    search_query = request.args.get("q", "").strip()
    art_type = request.args.get("type", "").strip()

    # Safely convert the page URL parameter to an integer
    try:
        current_page = int(request.args.get("page", 1))
    except ValueError:
        current_page = 1

    # 2. Inject the '&page=' parameter into the API URL
    limit = 25
    if search_query:
        url = f"https://api.artic.edu/api/v1/artworks/search?q={search_query}&limit={limit}&page={current_page}&fields=id,title,artist_display,image_id,date_display,medium_display,artwork_type_title"
    else:
        url = f"https://api.artic.edu/api/v1/artworks?limit={limit}&page={current_page}&fields=id,title,artist_display,image_id,date_display,medium_display,artwork_type_title"

    # 3. Fetch Data & Extract Pagination Metadata
    try:
        response = requests.get(url)
        data = response.json()
        raw_artworks = data.get("data", [])

        # The API gives us a dictionary telling us how many pages exist!
        pagination_info = data.get("pagination", {})
        total_pages = pagination_info.get("total_pages", 1)
    except:
        raw_artworks = []
        total_pages = 1

    # 4. Clean and Filter
    artworks = []
    for art in raw_artworks:
        image_id = art.get("image_id")
        current_type = art.get("artwork_type_title", "")

        if art_type and current_type != art_type:
            continue

        if image_id:
            artworks.append({
                "id": art.get("id"),
                "title": art.get("title", "Unknown Title"),
                "artist": art.get("artist_display", "Unknown Artist"),
                "date": art.get("date_display", "Unknown Date"),
                "type": current_type,
                "image_url": f"https://www.artic.edu/iiif/2/{image_id}/full/843,/0/default.jpg"
            })

    # 5. Pass the page variables back to Jinja
    return render_template("index.html",
                           artworks=artworks,
                           search_query=search_query,
                           selected_type=art_type,
                           current_page=current_page,
                           total_pages=total_pages)


if __name__ == "__main__":
    app.run(debug=True)
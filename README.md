# 🏛️ Artemis | Digital Fine Art Archive


**Artemis** is a luxury, high-performance digital gallery that fetches and displays real historical artifacts, paintings, and sculptures. 

Powered by the **Art Institute of Chicago (AIC) API**, this data-driven web application demonstrates advanced API integration techniques, including server-side pagination, compound search filtering, and on-the-fly IIIF image URL construction. Built with a focus on premium UI/UX, it features a responsive masonry grid and a custom-built sliding detail drawer without the use of heavy frontend frameworks.

## Core Engineering Features

* **Server-Side Pagination:** Intercepts URL parameters (`?page=X`) in the Flask backend to request specific data chunks from the AIC API, dramatically reducing payload size and improving load times.
* **Compound Search & Filter:** Combines native API search endpoints with Python-level data filtering, allowing users to query text (e.g., "Monet") while simultaneously filtering by physical medium (e.g., "Painting").
* **IIIF Image Construction:** Parses raw API data to extract `image_id`s and manually constructs valid International Image Interoperability Framework (IIIF) URLs to serve high-resolution, dynamically cropped images.
* **Responsive Masonry Grid:** Utilizes advanced CSS (`column-count` and `break-inside: avoid`) to create an interlocking, Pinterest-style layout that beautifully accommodates both portrait and landscape artwork without awkward cropping.
* **Custom Vanilla JS Drawer:** Bypasses basic Bootstrap modals for a custom, frosted-glass sliding drawer. It reads HTML5 `data-*` attributes via Vanilla JavaScript to instantly display rich metadata without triggering a page reload.

##  Tech Stack

**Backend:**
* Python 3.x
* Flask (Routing & Controller Logic)
* Requests (API fetching & JSON parsing)
* Jinja2 (Dynamic HTML Templating & State Preservation)

**Frontend:**
* HTML5 / CSS3
* Vanilla JavaScript (DOM manipulation & Drawer state)
* CSS Glassmorphism & Custom Animations

##  Project Structure

```text
Artemis_Gallery/
│
├── app.py                  # Core Flask server, API routing, and data mutation
├── requirements.txt        # Python dependencies
│
├── static/
│   └── style.css           # Premium dark-theme and masonry styling
│
└── templates/
    └── gallery.html        # Main Jinja template (Grid, Forms, Pagination, Drawer)
```


## Local Installation & Setup
To run this project locally on your machine:

## Clone the repository:

Bash
git clone [https://github.com/YOUR-USERNAME/artemis-gallery.git](https://github.com/NhartyInnovate/artemis-gallery.git)
cd artemis-gallery
## Create a virtual environment (Recommended):

Bash
python -m venv venv

# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate
Install the required dependencies:

Bash
pip install Flask requests
Run the Flask server:

Bash
python app.py
Explore the Archive:
Open your web browser and navigate to http://127.0.0.1:5000

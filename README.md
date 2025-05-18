# Spotifind

Spotifind is a Python application that recommends related artists on Spotify based on a given artist's name. It uses the Spotify API to fetch artist information and suggest similar artists.

---

## 📦 Project Structure

```
Spotifind/
├── .cache
├── .env
├── README.md
├── inspiration.py
├── spotify_artist_recommender.py
├── test_spotify.py
└── venv/
```

---

## 🚀 Getting Started

Follow these steps to set up and run Spotifind:

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kirankumarvel/Spotifind.git
   cd Spotifind
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the root directory with your Spotify API credentials:

   ```
   SPOTIPY_CLIENT_ID=<your_client_id>
   SPOTIPY_CLIENT_SECRET=<your_client_secret>
   ```

5. **Run the application**
   ```bash
   python spotify_artist_recommender.py
   ```

---

## 🛠️ File Overview

- `inspiration.py` &mdash; Initial prototype for fetching related artists.
- `spotify_artist_recommender.py` &mdash; Main script for artist recommendations.
- `test_spotify.py` &mdash; Test suite to verify API responses.

---

## 🧑‍💻 Author

- **Kiran**

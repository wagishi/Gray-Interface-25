
# 🎧 Spotify 2023 - Exploratory Data Analysis (EDA)

Welcome to the Exploratory Data Analysis of the **Spotify 2023 dataset** — a deep dive into the world of music analytics using Python! This project unveils powerful insights behind the most streamed artists and songs, genre patterns, popularity trends, and data-driven revelations.

---

## 📁 Dataset Overview

- **Source:** `spotify-2023.csv`
- **Features:** Contains detailed metadata of songs including:
  - Song title, Artist, Streams
  - BPM, Key, Mode, Danceability, Valence, Energy
  - Appearances in playlists and charts (Shazam, Deezer)
- **Timespan:** Songs range from the 1930s to 2023.

---

## 🧰 Tools & Libraries Used

- `Pandas` for data manipulation
- `NumPy` for numerical operations
- `Matplotlib` & `Seaborn` for data visualization
- `Warnings` filter for clean output

---

## 📊 EDA Highlights

### 🔍 1. Data Cleaning & Type Fixes
- Identified misclassified columns (e.g., streams as object due to formatting).
- Corrected issues in columns like `in_deezer_playlists` (commas caused type mismatch).
- Replaced null values in columns such as `in_shazam_charts` and `key`.

### 📈 2. Statistical Summary
- Songs span over **9 decades** (1930–2023).
- Maximum playlist inclusion: **~52,898 playlists**.
- Highest number of streams: **~3.7 billion**.

### 📦 3. Visual Insights
- **Boxplots** were used to detect outliers and understand distribution for features like:
  - Number of artists
  - Release year
  - Playlist appearances
  - Stream count
- **Top Songs and Artists:**
  - Most Streamed Song: *"Blinding Lights"*
  - Top Artists: *The Weeknd*, *Taylor Swift*, *Ed Sheeran*

### 💡 4. Interesting Discoveries
- A song's number of playlist appearances doesn't always correlate with stream count.
- The popularity isn't solely defined by playlist counts.

---

## 📌 Key Takeaways

- Effective data cleaning is crucial when working with inconsistent formats.
- Visualizations help uncover hidden patterns that raw numbers may not reveal.
- Even in music, not all popularity metrics are interrelated — a reminder that data always tells a story.

---

## 🧠 Author's Note

This project was built to enhance EDA skills and show how music data can be transformed into beautiful and insightful visuals. Feedback, suggestions are always welcome!

---

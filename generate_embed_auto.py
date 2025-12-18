import sys, os, requests

API_KEY = os.environ["YOUTUBE_API_KEY"]

def get_video_id(song_title, artist_name):
    query = f"{song_title} {artist_name}"
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=1&q={query}&key={API_KEY}"
    resp = requests.get(url)
    data = resp.json()
    if "items" in data and len(data["items"]) > 0:
        return data["items"][0]["id"]["videoId"]
    else:
        raise ValueError("No video found for query")

def make_embed(song_title, artist_name, video_id):
    return f"""
<div style="max-width:960px;margin:0 auto;">
  <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:16px;">
    <iframe
      src="https://www.youtube-nocookie.com/embed/{video_id}?rel=0&modestbranding=1&color=white"
      title="{artist_name} — {song_title}"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen
      style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;border-radius:16px;">
    </iframe>
  </div>
</div>
""".strip()

if __name__ == "__main__":
    song_title = sys.argv[1]
    artist_name = sys.argv[2]
    video_id = get_video_id(song_title, artist_name)
    print(make_embed(song_title, artist_name, video_id))

from pathlib import Path

base_dir = Path(__file__).resolve().parent
song_path = base_dir / "music"
def _getSongTitles():
        song_list = []
        for song_item in song_path.iterdir():
            if song_item.is_file():
                if song_item.suffix == ".mp3":
                    song_list.append(song_item.stem)
        return song_list

beng = _getSongTitles()

print(beng)

        
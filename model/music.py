from model.lyrics import FLY_MY_WINGS_LYRICS, VIOLET_LYRICS, SAIKAI_LYRICS


class Music:
    def __init__(self, title="unknown", genre="unknown", artist="unknown"):
        self.title = title.strip() or "unknown"
        self.genre = genre.strip() or "unknown"
        self.artist = artist.strip() or "unknown"

    def __str__(self):
        return f"제목: {self.title} | 장르: {self.genre} |  아티스트: {self.artist}"

    def __repr__(self):
        return f"제목: {self.title} | 장르: {self.genre} |  아티스트: {self.artist}"


class LyricsMusic(Music):
    def __init__(self, title="unknown", genre="unknown", artist="unknown",lyrics="unknown"):
        super().__init__(title, genre, artist)
        self.lyrics = lyrics.strip() or "unknown"

    def __str__(self):
        return f"{super().__str__()}\n\n가사: {self.lyrics}"

class DefaultMusic:

    @staticmethod
    def create_playlist():
        return [
            LyricsMusic(
                "Fly, My Wings",
                "OST",
                "Mili",
                FLY_MY_WINGS_LYRICS
            ),
            LyricsMusic(
                "Through Patches of Violet",
                "OST",
                "Mili",
                VIOLET_LYRICS
            ),
            LyricsMusic(
                "Saikai",
                "OST",
                "Mili",
                SAIKAI_LYRICS
            )
        ]
class AudioFileMixin:
    def play_audio(self):
        if not hasattr(self, "audio_file"):
            raise AttributeError(f"{self.__class__.__name__} не найден audio_file")
        print(f"Воспроизведение аудио для {self.__class__.__name__}")

        for track in self.audio_file:
            print(track)

class VideoFileMixin:
    def play_video(self):
        if not hasattr(self, "video_file"):
            raise AttributeError(f"{self.__class__.__name__} не найден video_file")

        print(f"Воспроизведение видео для {self.__class__.__name__}")

        for video in self.video_file:
            print(video)

class MediaPlayer(AudioFileMixin):
    def __init__(self, track: list[str]):
        self.audio_file = track

class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, track: list[str], movie: list[str]):
        self.audio_file = track
        self.video_file = movie

tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]

MediaPlayer(tracks).play_audio()

Laptop(tracks, movies).play_video()
Laptop(tracks, movies).play_audio()
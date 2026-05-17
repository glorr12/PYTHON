class AudioFileMixin:
    def play_audio(self):
        if not hasattr(self, "audio_file"):
            raise AttributeError(f"{self.__class__.__name__} не найден audio_file")
        return f"Воспроизведение аудио для {self.__class__.__name__}:\n{'\n'.join(self.audio_file)}"

class VideoFileMixin:
    def play_video(self):
        if not hasattr(self, "video_file"):
            raise AttributeError(f"{self.__class__.__name__} не найден video_file")

        return f"Воспроизведение видео для {self.__class__.__name__}:\n{'\n'.join(self.video_file)}"

class MediaPlayer(AudioFileMixin):
    def __init__(self, track: list[str]):
        self.audio_file = track

class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, track: list[str], movie: list[str]):
        self.audio_file = track
        self.video_file = movie

tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]

print(MediaPlayer(tracks).play_audio())
print(Laptop(tracks,movies).play_audio())
print(Laptop(tracks,movies).play_video())
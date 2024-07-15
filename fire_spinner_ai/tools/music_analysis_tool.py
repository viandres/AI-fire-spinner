from crewai_tools import BaseTool
import librosa

class MusicAnalysisTool(BaseTool):
    def analyze_music(self, music_path):
        y, sr = librosa.load(music_path)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(beat_frames, sr=sr)
        return beat_times

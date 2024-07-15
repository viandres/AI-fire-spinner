from crewai_tools import BaseTool
import mediapipe as mp
import cv2

class MediaPipePoseTool(BaseTool):
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()

    def process_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        pose_data = []
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = self.pose.process(frame)
            if results.pose_landmarks:
                pose_data.append(self.extract_landmarks(results.pose_landmarks))
        cap.release()
        return pose_data

    @staticmethod
    def extract_landmarks(landmarks):
        return [(lm.x, lm.y, lm.z) for lm in landmarks.landmark]

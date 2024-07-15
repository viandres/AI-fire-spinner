import unittest
from unittest.mock import patch
from agents.video_scraper import video_scraper
from agents.pose_estimator import pose_estimator
from agents.music_analysis import music_analysis_agent
from agents.choreography import choreography_agent
from agents.pose_mapping_agent import pose_mapping_agent

class TestAgents(unittest.TestCase):

    def test_video_scraper_initialization(self):
        self.assertEqual(video_scraper.role, "Video Scraper")
        self.assertTrue(video_scraper.tools)

    def test_pose_estimator_initialization(self):
        self.assertEqual(pose_estimator.role, "Pose Estimator")
        self.assertTrue(pose_estimator.tools)

    def test_music_analysis_agent_initialization(self):
        self.assertEqual(music_analysis_agent.role, "Music Analysis Agent")
        self.assertTrue(music_analysis_agent.tools)

    def test_choreography_agent_initialization(self):
        self.assertEqual(choreography_agent.role, "Choreography Agent")
        self.assertIsNone(choreography_agent.tools)

    def test_pose_mapping_agent_initialization(self):
        self.assertEqual(pose_mapping_agent.role, "Pose Mapping Agent")
        self.assertTrue(pose_mapping_agent.tools)

if __name__ == '__main__':
    unittest.main()

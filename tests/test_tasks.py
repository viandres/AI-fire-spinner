import unittest
from unittest.mock import patch
from tasks.scraping_task import scraping_task
from tasks.pose_estimation_task import pose_estimation_task
from tasks.music_analysis_task import music_analysis_task
from tasks.choreography_task import choreography_task
from tasks.pose_mapping_task import pose_mapping_task

class TestTasks(unittest.TestCase):

    def test_scraping_task_initialization(self):
        self.assertIn("search the web", scraping_task.description)
        self.assertTrue(scraping_task.agent)

    def test_pose_estimation_task_initialization(self):
        self.assertIn("extract detailed position", pose_estimation_task.description)
        self.assertTrue(pose_estimation_task.agent)

    def test_music_analysis_task_initialization(self):
        self.assertIn("detect beats and rhythms", music_analysis_task.description)
        self.assertTrue(music_analysis_task.agent)

    def test_choreography_task_initialization(self):
        self.assertIn("create a detailed choreography script", choreography_task.description)
        self.assertTrue(choreography_task.agent)

    def test_pose_mapping_task_initialization(self):
        self.assertIn("structured format suitable for 3D animation", pose_mapping_task.description)
        self.assertTrue(pose_mapping_task.agent)

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch, mock_open
from utils.data_processing import load_json, save_json, normalize_pose_data
from utils.logging import setup_logger, log_message
import json
import os

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.test_json_path = 'test.json'
        self.test_data = {'key': 'value'}
        self.logger = setup_logger('test_logger', 'test.log')

    def tearDown(self):
        if os.path.exists(self.test_json_path):
            os.remove(self.test_json_path)
        if os.path.exists('test.log'):
            os.remove('test.log')

    def test_load_json(self):
        with patch('builtins.open', mock_open(read_data=json.dumps(self.test_data))):
            data = load_json(self.test_json_path)
            self.assertEqual(data, self.test_data)

    def test_save_json(self):
        with patch('builtins.open', mock_open()) as mock_file:
            path = save_json(self.test_data, self.test_json_path)
            self.assertTrue(mock_file.called)
            self.assertTrue(os.path.exists(path))

    def test_normalize_pose_data(self):
        pose_data = [{'frame': 0, 'position': {'x': 1, 'y': 2, 'z': 3}, 'rotation': {}}]
        normalized_data = normalize_pose_data(pose_data)
        self.assertEqual(normalized_data[0]['position']['x'], 1)

    def test_setup_logger(self):
        self.assertTrue(os.path.exists('test.log'))

    def test_log_message(self):
        log_message(self.logger, 'Test message', level=logging.INFO)
        with open('test.log', 'r') as log_file:
            logs = log_file.read()
            self.assertIn('Test message', logs)

if __name__ == '__main__':
    unittest.main()

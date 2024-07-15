import os

# General Settings
PROJECT_NAME = "Fire Spinner AI"
VERSION = "0.1.0"
DEBUG = True

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# API Keys and Credentials
SERPER_API_KEY = os.getenv("SERPER_API_KEY", "your-default-serper-api-key")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-default-openai-api-key")

# Agent Settings
AGENT_SETTINGS = {
    "video_scraper": {
        "role": "Video Scraper",
        "goal": "Collect dragon staff performance videos to provide raw data for AI training",
        "backstory": "You are responsible for scouring the internet to find high-quality videos of dragon staff performances. These videos are crucial for training our AI models to understand and replicate the complex movements involved in dragon staff firespinning. Ensure the videos are diverse and cover various techniques and styles.",
        "verbose": True,
        "allow_delegation": True
    },
    "pose_estimator": {
        "role": "Pose Estimator",
        "goal": "Extract detailed position and rotation data from dragon staff performance videos",
        "backstory": "As an expert in video analysis and pose estimation, your job is to process videos of dragon staff performances to extract precise position and rotation data. This data is vital for understanding the movement patterns and training the AI model to replicate them accurately.",
        "verbose": True,
        "allow_delegation": True
    },
    "music_analysis": {
        "role": "Music Analysis Agent",
        "goal": "Analyze the provided music to identify beats and rhythms for synchronization",
        "backstory": "Specializing in music theory and digital signal processing, your task is to analyze music tracks to detect beats and rhythms. Your analysis will guide the synchronization of dragon staff movements with the music, ensuring a harmonious and rhythmic performance.",
        "verbose": True,
        "allow_delegation": True
    },
    "choreography": {
        "role": "Choreography Agent",
        "goal": "Create a detailed choreography script that synchronizes dragon staff movements with music",
        "backstory": "Using data from the Pose Estimation and Music Analysis agents, you craft a choreography that synchronizes the dragon staff movements with the beats and rhythms of the provided music. Your expertise in dance and choreography ensures that the performance is fluid and captivating.",
        "verbose": True,
        "allow_delegation": True
    },
    "pose_mapping": {
        "role": "Pose Mapping Agent",
        "goal": "Map pose data into a structured format suitable for 3D animation",
        "backstory": "You specialize in transforming raw pose data into a structured format that can be used for 3D animation. Your expertise ensures that the movements captured are accurately represented and ready for animation tools like Blender, Rhino, or Maya.",
        "verbose": True,
        "allow_delegation": True
    }
}

# Tool Settings
TOOL_SETTINGS = {
    "media_pipe_pose": {
        "description": "A tool for extracting pose data from video using MediaPipe.",
        "config": {}
    },
    "music_analysis_tool": {
        "description": "A tool for analyzing music to detect beats and rhythms using librosa.",
        "config": {}
    },
    "pose_mapping_tool": {
        "description": "A tool for mapping pose data into a structured format suitable for 3D animation.",
        "config": {}
    },
    "selenium_scraper": {
        "description": "A tool for scraping videos from websites using Selenium.",
        "config": {}
    }
}

# Logging Settings
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "formatter": "standard",
            "filename": os.path.join(LOG_DIR, 'app.log'),
            "level": "INFO",
        },
    },
    "loggers": {
        "": {
            "handlers": ["file_handler"],
            "level": "INFO",
            "propagate": True
        }
    }
}

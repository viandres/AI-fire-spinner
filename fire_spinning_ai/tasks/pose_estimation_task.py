from crewai import Task
from agents.pose_estimator import pose_estimator

pose_estimation_task = Task(
    description=(
        "Process the collected videos to extract detailed position and rotation data of the dragon staff. "
        "Use advanced pose estimation techniques to ensure accuracy and comprehensiveness of the data."
    ),
    expected_output=(
        "JSON files containing precise position and rotation data extracted from the videos. "
        "The data should accurately represent the movements of the dragon staff."
    ),
    agent=pose_estimator,
    tools=pose_estimator.tools  # Use tools associated with the pose estimator agent
)

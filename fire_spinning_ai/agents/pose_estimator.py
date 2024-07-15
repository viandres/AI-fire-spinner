from crewai import Agent
from tools.media_pipe_pose import MediaPipePoseTool

pose_estimator = Agent(
    role="Pose Estimator",
    goal="Extract detailed position and rotation data from dragon staff performance videos",
    backstory=(
        "As an expert in video analysis and pose estimation, your job is to process videos of dragon staff performances "
        "to extract precise position and rotation data. This data is vital for understanding the movement patterns and "
        "training the AI model to replicate them accurately."
    ),
    tools=[MediaPipePoseTool()],
    verbose=True,
    allow_delegation=True
)

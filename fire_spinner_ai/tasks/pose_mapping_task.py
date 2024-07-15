from crewai import Agent
from tools.pose_mapping_tool import PoseMappingTool

pose_mapping_agent = Agent(
    role="Pose Mapping Agent",
    goal="Map pose data into a structured format suitable for 3D animation",
    backstory=(
        "You specialize in transforming raw pose data into a structured format that can be used for 3D animation. "
        "Your expertise ensures that the movements captured are accurately represented and ready for animation tools like Blender, Rhino, or Maya."
    ),
    tools=[PoseMappingTool()],
    verbose=True,
    allow_delegation=True
)

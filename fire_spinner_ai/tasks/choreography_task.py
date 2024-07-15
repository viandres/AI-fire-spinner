from crewai import Task
from agents.choreography import choreography_agent

choreography_task = Task(
    description=(
        "Using the pose data and beat information, create a detailed choreography script that synchronizes the dragon staff movements with the music. "
        "Ensure that the movements are fluid and aligned with the music's rhythm and tempo."
    ),
    expected_output=(
        "A comprehensive choreography script that maps out the dragon staff movements in sync with the music beats. "
        "The script should detail each movement and its timing relative to the music."
    ),
    agent=choreography_agent,
    tools=choreography_agent.tools  # Use tools associated with the choreography agent
)

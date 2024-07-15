from crewai import Task
from agents.music_analysis import music_analysis_agent

music_analysis_task = Task(
    description=(
        "Analyze the provided music tracks to detect beats and rhythms. "
        "Your analysis will be used to synchronize the dragon staff movements with the music, ensuring a cohesive performance."
    ),
    expected_output=(
        "A detailed list of time-stamped beats and rhythms detected in the music tracks. "
        "This data will guide the choreography and synchronization process."
    ),
    agent=music_analysis_agent,
    tools=music_analysis_agent.tools  # Use tools associated with the music analysis agent
)

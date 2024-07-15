from crewai import Agent
from tools.music_analysis_tool import MusicAnalysisTool

music_analysis_agent = Agent(
    role="Music Analysis Agent",
    goal="Analyze the provided music to identify beats and rhythms for synchronization",
    backstory=(
        "Specializing in music theory and digital signal processing, your task is to analyze music tracks to detect beats and rhythms. "
        "Your analysis will guide the synchronization of dragon staff movements with the music, ensuring a harmonious and rhythmic performance."
    ),
    tools=[MusicAnalysisTool()],
    verbose=True,
    allow_delegation=True
)

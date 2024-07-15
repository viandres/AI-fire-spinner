from crewai import Agent

choreography_agent = Agent(
    role="Choreography Agent",
    goal="Create a detailed choreography script that synchronizes dragon staff movements with music",
    backstory=(
        "Using data from the Pose Estimation and Music Analysis agents, you craft a choreography that synchronizes the dragon staff movements "
        "with the beats and rhythms of the provided music. Your expertise in dance and choreography ensures that the performance is fluid and captivating."
    ),
    verbose=True,
    allow_delegation=True
)

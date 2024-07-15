# AI Fire Spinner

Welcome to the AI Fire Spinner project! This ambitious and exciting initiative aims to merge the art of fire spinning with the power of artificial intelligence to create a mesmerizing and dynamic performance experience.

## Project Overview

The AI Fire Spinner project focuses on developing an AI model capable of learning and replicating the intricate movements of fire spinners dancing to music. By analyzing videos and accompanying music, the AI will learn the specific movements of a dragon staff, enabling it to perform autonomously when given a piece of music.

## Key Objectives

- Data Collection: Gather and preprocess video data of fire spinners performing with a dragon staff, along with the corresponding music.
- AI Model Development: Train an AI model to recognize and learn the movements of the dragon staff in sync with the music.
- 3D Animation: Illustrate the AI-generated movements using a 3D animation program to visualize the performance.
- Kinetic AI Sculpture: Build a kinetic sculpture that embodies the AI's learned choreography, capable of dancing and performing live with other real fire spinners at events, shows, and festivals.

## Future Vision

The ultimate goal of the AI Fire Spinner project is to create an AI-driven kinetic sculpture that not only performs solo but also collaborates with human performers. This will bring a unique fusion of technology and artistry to live performances, captivating audiences with a blend of innovation and tradition.

## Usage

Before usage please set your SERPER_API_KEY and OPENAI_API_KEY in the fire_spinning_ai/config/settings.py file.

# Precondition

## Development Setup

Open the [integrated terminal](https://code.visualstudio.com/docs/editor/integrated-terminal) and run the setup script for your OS (see below). This will install a [Python virtual environment](https://docs.python.org/3/library/venv.html) with all packages specified in `requirements.txt`.

### Linux and Mac Users

1. run the setup script: `./setup.sh` or `sh setup.sh`
2. activate the python environment: `source .venv/bin/activate`
3. run example code: `python src/hello.py`
4. install new dependency: `pip install sklearn`
5. save current installed dependencies back to requirements.txt: `pip freeze > requirements.txt`

### Windows Users

1. run the setup script `.\setup.ps1`
2. activate the python environment: `.\.venv\Scripts\Activate.ps1`
3. run example code: `python src/hello.py`
4. install new dependency: `pip install sklearn`
5. save current installed dependencies back to requirements.txt: `pip freeze > requirements.txt`

Troubleshooting:

- If your system does not allow to run powershell scripts, try to set the execution policy: `Set-ExecutionPolicy RemoteSigned`, see https://www.stanleyulili.com/powershell/solution-to-running-scripts-is-disabled-on-this-system-error-on-powershell/
- If you still cannot run the setup.ps1 script, open it and copy all the commands step by step in your terminal and execute each step

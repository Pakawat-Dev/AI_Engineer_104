# Meeting Management AI Agent System

Python application that uses AI agents to help manage meetings, create agendas, and handle task assignments.

## Overview
This project uses AI agents to help manage meetings, create agendas, and handle assignments using OpenAI's GPT models.

## Prerequisites
- Python 3.8 or higher installed
- OpenAI API key
- Basic command line knowledge

## Step-by-Step Setup

### Step 1: Install Python Dependencies
Open your terminal/command prompt in the project folder and run:
```bash
pip install -r requirements.txt
```

### Step 2: Set Up Your OpenAI API Key
1. Open the `.env` file in this folder
2. Replace the existing API key with your own OpenAI API key:
   ```
   OPENAI_API_KEY="your-api-key-here"
   ```
3. Save the file

### Step 3: Run the Program
In your terminal, run:
```bash
python team_openai.py
```

### Step 4: Use the Interactive Mode
Once the program starts, you'll see:
```
Assignment Mode (type 'exit' to quit)

Assignment:
```

Now you can type any task or question, for example:
- "Schedule a team meeting for next week"
- "Create an agenda for a project kickoff"
- "Summarize our last meeting notes"
- "Plan a 30-minute standup meeting"

### Step 5: Exit the Program
Type `exit`, `quit`, or `q` to stop the program.

## Features
- **Meeting Coordinator**: Schedules meetings efficiently
- **Agenda Planner**: Creates structured meeting agendas
- **Note Taker**: Summarizes meetings and creates action items
- **Assignment Handler**: Processes your task requests

## Configuration
The agents are configured with:
- Model: `gpt-5-nano-2025-08-07`
- Max iterations: 2 (to control response length)
- Verbose mode: Off (cleaner output)

## Troubleshooting

### SSL Certificate Error
If you see SSL/telemetry errors, the code already disables telemetry with:
```python
os.environ["OTEL_SDK_DISABLED"] = "true"
```

### API Key Issues
- Make sure your OpenAI API key is valid
- Check that you have credits in your OpenAI account
- Verify the `.env` file is in the same folder as `team_openai.py`

### Model Not Found
If the model is not available, change the model in `team_openai.py`:
```python
def create_llm():
    return ChatOpenAI(model="gpt-4o-mini")  # or another available model
```

## Example Usage
```
Assignment: Schedule a team meeting for tomorrow at 2 PM

[AI will generate meeting details, invite template, and checklist]

Assignment: exit
```

## Need Help?
- Check your Python version: `python --version`
- Verify dependencies: `pip list`
- Review error messages carefully - they usually indicate what's wrong

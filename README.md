# Meeting Management AI Agent System

Python application that uses AI agents to help manage meetings, create agendas, and handle task assignments.

## What This Does

This program creates AI-powered assistants that can:
- Schedule meetings and suggest time slots
- Create meeting agendas
- Summarize meeting notes
- Handle custom task assignments

## Prerequisites

Before you start, you need:
1. Python 3.8 or higher installed
2. An OpenAI API key
3. Basic knowledge of command line/terminal

## Step-by-Step Setup

### Step 1: Install Required Packages

Open your terminal/command prompt and run:

```bash
pip install crewai langchain-openai python-dotenv
```

### Step 2: Create Environment File

1. In the same folder as `team.py`, create a file named `.env`
2. Add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.

### Step 3: Run the Program

In your terminal, navigate to the project folder and run:

```bash
python team.py
```

## How to Use

### Interactive Mode

When you run the program, it starts in "Assignment Mode":

```
Assignment Mode (type 'exit' to quit)

Assignment: 
```

You can type any task or question, for example:
- "Create a meeting agenda for tomorrow's standup"
- "Schedule a team meeting for next week"
- "Summarize the key points from our last discussion"

Type `exit`, `quit`, or `q` to stop the program.

## Understanding the Code

### Main Components

1. **LLM (Language Model)**: The AI brain that powers the agents
   - Uses OpenAI's GPT model
   - Temperature set to 0.1 for consistent responses

2. **Agents**: Four specialized AI assistants
   - **Coordinator**: Schedules meetings
   - **Summarizer**: Takes notes and creates summaries
   - **Planner**: Creates meeting agendas
   - **Assistant**: Handles general task assignments

3. **Tasks**: Specific jobs given to agents
   - Each task has a description and expected output
   - Tasks are executed by assigned agents

4. **Crew**: A team of agents working together
   - Agents collaborate to complete tasks
   - Tasks run sequentially (one after another)

### Key Functions

- `create_llm()`: Sets up the AI model
- `create_agents()`: Creates the four AI assistants
- `create_schedule_task()`: Makes a meeting scheduling task
- `create_agenda_task()`: Makes an agenda creation task
- `create_summary_task()`: Makes a note summarization task
- `handle_user_assignment()`: Processes your input
- `interactive_mode()`: Runs the chat interface

## Example Usage

```
Assignment: Schedule a team meeting for next Monday

[AI will suggest meeting times, create an invite template, and provide a checklist]

Assignment: Create an agenda for a 1-hour project review

[AI will create a structured agenda with time allocations and topics]

Assignment: exit
```

## Troubleshooting

**Problem**: "Module not found" error
- **Solution**: Make sure you installed all packages (Step 1)

**Problem**: "API key not found" error
- **Solution**: Check your `.env` file has the correct API key

**Problem**: Program runs but no response
- **Solution**: Verify your OpenAI API key is valid and has credits

## Customization

### Change the AI Model

In `create_llm()` function, modify:
```python
return ChatOpenAI(model="gpt-4", temperature=0.1)
```

### Add More Agents

In `create_agents()` function, add a new agent:
```python
'new_agent': Agent(
    role='Your Role',
    goal='Your Goal',
    backstory='Your Backstory',
    verbose=True,
    allow_delegation=False,
    llm=llm
)
```

## Project Structure

```
AI_Engineer_104/
├── team.py          # Main program file
├── .env             # API keys (create this)
└── README.md        # This file
```

## Important Notes

- Keep your `.env` file private (never share your API key)
- Each API call costs money (check OpenAI pricing)
- The program needs internet connection to work
- Responses may take a few seconds to generate

## Next Steps

Once comfortable with the basics:
1. Try modifying agent roles and goals
2. Create custom tasks for specific needs
3. Experiment with different meeting scenarios
4. Add error handling for your use cases

## Support

If you encounter issues:
1. Check that all packages are installed
2. Verify your API key is correct
3. Ensure you have internet connection
4. Review error messages carefully

---

from crewai import Agent, Task, Crew, Process
from langchain_ollama import ChatOllama
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Disable CrewAI telemetry
os.environ["OTEL_SDK_DISABLED"] = "true"

def create_llm():
    return ChatOllama(
        model="ministral-3:3b",
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        temperature=0.1,
        num_predict=2500
    )

def create_agents(llm):
    return {
        'coordinator': Agent(
            role='Meeting Coordinator',
            goal='Schedule meetings efficiently',
            backstory='Executive assistant specializing in meeting coordination. Keep responses concise.',
            verbose=False,
            allow_delegation=False,
            llm=llm,
            max_iter=2
        ),
        'summarizer': Agent(
            role='Meeting Note Taker',
            goal='Create meeting summaries and action items',
            backstory='Skilled note-taker capturing key decisions and action items. Keep responses brief.',
            verbose=False,
            allow_delegation=False,
            llm=llm,
            max_iter=2
        ),
        'planner': Agent(
            role='Agenda Planner',
            goal='Create structured meeting agendas',
            backstory='Expert at creating productive meeting agendas. Keep responses concise.',
            verbose=False,
            allow_delegation=False,
            llm=llm,
            max_iter=2
        ),
        'assistant': Agent(
            role='Assignment Handler',
            goal='Process user assignments',
            backstory='Assistant handling user task assignments. Keep responses brief and to the point.',
            verbose=False,
            allow_delegation=False,
            llm=llm,
            max_iter=2
        )
    }

def create_schedule_task(agent):
    return Task(
        description="""Schedule project kickoff meeting for next week (1 hour, product/engineering/stakeholders, EST/PST timezones).
Provide: 3 time options, invite template, preparation checklist.""",
        expected_output="Meeting plan with times, invite, checklist",
        agent=agent
    )

def create_agenda_task(agent):
    return Task(
        description="""Create agenda for project kickoff: time allocations, topics (intros, overview, scope, timeline, Q&A), owners, materials.""",
        expected_output="Structured agenda with times and owners",
        agent=agent
    )

def create_summary_task(agent, notes):
    return Task(
        description=f"""Summarize meeting notes: {notes}
Provide: executive summary, key decisions, action items with owners/deadlines, follow-ups.""",
        expected_output="Meeting summary with action items",
        agent=agent
    )

def create_custom_task(agent, meeting_type, participants, duration, topics):
    return Task(
        description=f"""Organize {meeting_type}: {participants}, {duration}, topics: {topics}.
Provide: agenda, time slots, objectives.""",
        expected_output=f"{meeting_type} plan",
        agent=agent
    )

def create_assignment_task(agent, user_input):
    return Task(
        description=f"Process: {user_input}",
        expected_output="Task result",
        agent=agent
    )

def execute_crew(crew):
    try:
        return crew.kickoff()
    except Exception as e:
        print(f"Error executing crew: {e}")
        raise

def run_meeting_agent(agents):
    tasks = [
        create_schedule_task(agents['coordinator']),
        create_agenda_task(agents['planner']),
        create_summary_task(agents['summarizer'], 
            "Product roadmap, resource concerns, hire 2 devs, budget approval Friday, designs end of month, weekly Tues 2PM")
    ]
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    return execute_crew(crew)

def handle_meeting_request(agents, meeting_type, details):
    if not isinstance(details, dict):
        raise TypeError("details must be a dictionary")
    
    task = create_custom_task(
        agents['coordinator'],
        meeting_type,
        details.get('participants', 'Team members'),
        details.get('duration', '30 minutes'),
        details.get('topics', 'General discussion')
    )
    crew = Crew(
        agents=[agents['coordinator'], agents['planner']],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )
    return execute_crew(crew)

def handle_user_assignment(agents, user_input):
    task = create_assignment_task(agents['assistant'], user_input)
    crew = Crew(
        agents=[agents['assistant']],
        tasks=[task],
        process=Process.sequential,
        verbose=False
    )
    return execute_crew(crew)

def interactive_mode(agents):
    print("Assignment Mode (type 'exit' to quit)")
    while True:
        user_input = input("\nAssignment: ").strip()
        if user_input.lower() in ['exit', 'quit', 'q']:
            break
        if not user_input:
            continue
        try:
            result = handle_user_assignment(agents, user_input)
            print(f"\n{result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    llm = create_llm()
    agents = create_agents(llm)
    
    interactive_mode(agents)

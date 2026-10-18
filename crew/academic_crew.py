# crew/academic_crew.py

from crewai import Crew, Process

from agents.discovery import discovery_agent
from agents.governance import governance_agent
from agents.architect import architect
from agents.flow_analyst import flow_agent
from agents.standards import standards_agent
from agents.sharepoint import sharepoint_agent
from agents.python_dev import python_agent
from agents.reviewer import reviewer

from tasks.discovery_platform import discovery_task
from tasks.gap_analysis import gap_analysis_task
from tasks.analyse_flows import flow_analysis_task
from tasks.build_model import build_model_task
from tasks.build_sharepoint import sharepoint_task
from tasks.build_parser import build_parser_task

crew = Crew(
    agents=[
        discovery_agent,
        flow_agent,
        standards_agent,
        governance_agent,
        architect,
        sharepoint_agent,
        python_agent,
        reviewer
    ],

    tasks=[
        discovery_task,
        gap_analysis_task,
        flow_analysis_task,
        build_model_task,
        sharepoint_task,
        build_parser_task
    ],

    process=Process.sequential,

    verbose=True
)
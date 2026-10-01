# crew/academic_crew.py

from crewai import Crew

from agents.architect import architect
from agents.flow_analyst import flow_agent
from agents.standards import standards_agent
from agents.sharepoint import sharepoint_agent
from agents.python_dev import python_agent
from agents.reviewer import reviewer

from tasks import discovery_platform
from tasks.build_model import build_model_task
from tasks.build_sharepoint import sharepoint_task
from tasks.build_parser import build_parser_task
from tasks.analyse_flows import flow_analysis_task
from tasks.discovery_platform import discovery_task

crew = Crew(
    agents=[
        architect,
        flow_agent,
        standards_agent,
        sharepoint_agent,
        python_agent,
        reviewer
    ],

    tasks=[
        discovery_task,
        build_model_task,
        sharepoint_task,
        build_parser_task,
        flow_analysis_task
    ],

    verbose=True
)
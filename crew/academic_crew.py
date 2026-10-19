# crew/academic_crew.py

from crewai import Crew, Process

from agents.discovery import discovery_agent
from agents.governance import governance_agent
from agents.flow_analyst import flow_agent
from agents.architect import architect
from agents.sharepoint import sharepoint_agent

from tasks.discovery_platform import discovery_task
from tasks.compliance import compliance_task
from tasks.analyse_flows import flow_analysis_task
from tasks.build_model import build_model_task
from tasks.build_sharepoint import sharepoint_task


crew = Crew(
    agents=[
        discovery_agent,
        governance_agent,
        flow_agent,
        architect,
        sharepoint_agent
    ],

    tasks=[
        # Extract schema from repository artefacts
        discovery_task,

        # Convert governance requirements into schema requirements
        compliance_task,

        # Extract integration relationships
        flow_analysis_task,

        # Merge into canonical schema
        build_model_task,

        # Generate SharePoint deployment schema
        sharepoint_task
    ],

    process=Process.sequential,

    verbose=True
)
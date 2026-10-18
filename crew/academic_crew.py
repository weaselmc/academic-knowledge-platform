# crew/academic_crew.py

from crewai import Crew, Process

from agents.discovery import discovery_agent
from agents.governance import governance_agent
from agents.flow_analyst import flow_agent
from agents.architect import architect
from agents.sharepoint import sharepoint_agent
from agents.python_dev import python_agent

from tasks.discovery_platform import discovery_task
from tasks.compliance import compliance_task
from tasks.analyse_flows import flow_analysis_task
from tasks.build_model import build_model_task
from tasks.build_sharepoint import sharepoint_task
from tasks.parser_mapping import parser_mapping_task
from tasks.parser_code import parser_code_task

crew = Crew(
    agents=[
        discovery_agent,
        governance_agent,
        flow_agent,
        architect,
        sharepoint_agent,
        python_agent
    ],

    tasks=[
        discovery_task,        # discovered_schema.json

        compliance_task,       # compliance_schema.json

        flow_analysis_task,    # integration_schema.json        

        build_model_task,      # canonical_schema.json

        sharepoint_task,       # sharepoint_schema.json

        parser_mapping_task,   # parser_mapping_spec.json

        parser_code_task       # parser_generation_spec.json
    ],

    process=Process.sequential,

    verbose=True
)
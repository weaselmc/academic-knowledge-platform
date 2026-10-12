# tasks/build_model.py

from crewai import Knowledge, Task
from agents.architect import architect
from tasks.discovery_platform import discovery_task
from tasks.gap_analysis import gap_analysis_task

build_model_task = Task(
    description="""
    Design a canonical academic governance and delivery data model for an RTO.

    The model must support:

    - Qualifications
    - Courses
    - Clusters
    - Units
    - TASs
    - LAPs
    - Assessment Mapping Matrices

    - Industry Advisory Meetings
    - Student Feedback
    - Validation Findings
    - Recommendations
    - Continuous Improvements

    - Change Requests
    - Approval Workflows

    - Versioned TASs
    - Versioned LAPs
    - Historical Reconstruction

    - SharePoint storage
    - Power Automate workflows
    - Canvas publishing

    - Auditor evidence chains

    Data must be normalised so that information
    is stored once and reused across all views.

    No data may be physically deleted.
    All changes must be versioned and auditable.
    """,

    agent=architect
)
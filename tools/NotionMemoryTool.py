import os
import hashlib
from typing import Dict
from notion_client import Client

# ENV: Please make sure these are set
NOTION_API_TOKEN = os.getenv("NOTION_API_TOKEN")
NOTION_DB_ID = os.getenv("NOTION_JOBS_DB_ID")

# Initialize Notion client
notion = Client(auth=NOTION_API_TOKEN)


def store_job(job: Dict) -> bool:
    """
    Stores a job in Notion if not a duplicate.
    Returns True if inserted, False if skipped.
    """
   
    try:
        notion.pages.create(
            parent={"database_id": NOTION_DB_ID},
            properties={
                "Job Title": {"title": [{"text": {"content": job["title"]}}]},
                "Company": {"rich_text": [{"text": {"content": job["company"]}}]},
                "Location": {"rich_text": [{"text": {"content": job.get("location", "")}}]},
                "Apply Link": {"url": job["apply_link"]},
                "Posted Date": {"date": {"start": job.get("posted_date")}},
                "Tags": {"multi_select": [{"name": tag} for tag in job.get("tags", [])]},
                "Source": {"rich_text": [{"text": {"content": job.get("source", "")}}]},
                "Description": {"rich_text": [{"text": {"content": job.get("description", "")}}]},
                "UID": {"rich_text": [{"text": {"content": job.get("uid", "")}}]},
            }
        )
        return True
    except Exception as e:
        raise RuntimeError(f"Failed to insert job to Notion: {e}")
from notion_client import Client
import os

notion = Client(auth=os.getenv("NOTION_API_TOKEN"))
QUERY_DB_ID = os.getenv("QUERY_DB_ID")

def get_active_queries():
    rows = notion.databases.query(
        database_id=QUERY_DB_ID,
        filter={"property": "Active", "checkbox": {"equals": True}}
    )
    queries = []
    for row in rows["results"]:
        props = row["properties"]
        queries.append({
            "query": props["Search Query"]["title"][0]["text"]["content"],
            "source": props["Source"]["select"]["name"],
            "category": props.get("Category", {}).get("select", {}).get("name", "")
        })
    return queries
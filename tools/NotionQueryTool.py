from notion_client import Client

class NotionQueryTool:

def __init__(self):
	self.notion = Client(auth="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")
	self.database_id = "1e069e833b44805e869fc4b5167f74bc"

def run(self, input=None):
"""
Returns active search queries from the specified Notion database.
"""

try:
try:
	rows = self.notion.databases.query(
		database_id=self.database_id,
		filter={"property": "Active", "checkbox": {"equals": True}},
	)

	queries = []
	for row in rows["results"]:
		props = row["properties"]

		query_val = ""
		if props.get("Search Query", {}).get("title"):
			title = props["Search Query"]["title"]
			if title and title[0]["type"] == "text":
				query_val = title[0]["text"]["content"]

		source_val = props.get("Source", {}).get("select", {}).get("name", "")
		category_val = props.get("Category", {}).get("select", {}).get("name", "")

		queries.append({
			"query": query_val,
			"source": source_val,
			"category": category_val
		})

	return {"results": queries}

except Exception as e:
	return {"error": str(e)}
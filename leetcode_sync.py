# leetcode_sync.py

import requests, json, os

USERNAME = os.environ["LEETCODE_USERNAME"]
SESSION = os.environ["LEETCODE_SESSION"]

headers = {
    "cookie": f"LEETCODE_SESSION={SESSION}",
    "referer": "https://leetcode.com",
    "Content-Type": "application/json",
}

def fetch_submissions():
    query = {
        "operationName": "mySubmissions",
        "variables": {"offset": 0, "limit": 20},
        "query": """
        query mySubmissions($offset: Int!, $limit: Int!) {
            submissionList(offset: $offset, limit: $limit) {
                submissions {
                    title
                    statusDisplay
                    lang
                    timestamp
                    code
                }
            }
        }
        """
    }

    res = requests.post("https://leetcode.com/graphql", headers=headers, data=json.dumps(query))
    submissions = res.json()["data"]["submissionList"]["submissions"]

    os.makedirs("solutions", exist_ok=True)

    for sub in submissions:
        if sub["statusDisplay"] == "Accepted":
            lang = {"python3": "py", "cpp": "cpp", "java": "java"}.get(sub["lang"], "txt")
            name = sub["title"].replace(" ", "_") + "." + lang
            with open(f"solutions/{name}", "w", encoding="utf-8") as f:
                f.write(sub["code"])

if __name__ == "__main__":
    fetch_submissions()

import requests
import json
import os
import time

USERNAME = os.environ.get("LEETCODE_USERNAME")
SESSION = os.environ.get("LEETCODE_SESSION")

headers = {
    "cookie": f"LEETCODE_SESSION={SESSION}",
    "referer": "https://leetcode.com",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

# Maps LeetCode language to file extension
LANG_MAP = {
    "python3": "py",
    "cpp": "cpp",
    "java": "java",
    "c": "c",
    "csharp": "cs",
    "javascript": "js",
    "typescript": "ts",
    "go": "go",
    "ruby": "rb",
    "swift": "swift"
}

def fetch_submissions(limit=20):
    print("🔄 Fetching recent submissions...")

    query = {
        "operationName": "mySubmissions",
        "variables": {"offset": 0, "limit": limit},
        "query": """
        query mySubmissions($offset: Int!, $limit: Int!) {
            submissionList(offset: $offset, limit: $limit) {
                submissions {
                    id
                    title
                    statusDisplay
                    lang
                    timestamp
                }
            }
        }
        """
    }

    res = requests.post("https://leetcode.com/graphql", headers=headers, data=json.dumps(query))
    data = res.json()

    if "data" not in data:
        print("❌ Failed to fetch submissions. Response:")
        print(json.dumps(data, indent=2))
        return []

    return data["data"]["submissionList"]["submissions"]

def fetch_code(submission_id):
    url = f"https://leetcode.com/submissions/detail/{submission_id}/check/"
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        try:
            return res.json().get("code", "")
        except:
            return ""
    return ""

def save_solution(title, lang, code):
    ext = LANG_MAP.get(lang, "txt")
    filename = f"solutions/{title.replace(' ', '_').replace('/', '_')}.{ext}"
    os.makedirs("solutions", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"✅ Saved: {filename}")

def main():
    submissions = fetch_submissions()
    for sub in submissions:
        if sub["statusDisplay"] == "Accepted":
            code = fetch_code(sub["id"])
            if code:
                save_solution(sub["title"], sub["lang"], code)
                time.sleep(1)  # polite delay
            else:
                print(f"⚠️ Could not fetch code for {sub['title']}")

if __name__ == "__main__":
    main()

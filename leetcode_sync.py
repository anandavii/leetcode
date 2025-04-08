import requests
import json
import os

# Load credentials from environment variables
USERNAME = os.environ.get("LEETCODE_USERNAME")
SESSION = os.environ.get("LEETCODE_SESSION")

# LeetCode headers for authentication
headers = {
    "cookie": f"LEETCODE_SESSION={SESSION}",
    "referer": "https://leetcode.com",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"  # helps avoid bot detection
}

def fetch_submissions():
    # GraphQL query to fetch recent submissions
    query = {
        "operationName": "mySubmissions",
        "variables": {
            "offset": 0,
            "limit": 20
        },
        "query": """
        query mySubmissions($offset: Int!, $limit: Int!) {
            submissionList(offset: $offset, limit: $limit) {
                submissions {
                    id
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

    # Send POST request to LeetCode's internal GraphQL API
    response = requests.post("https://leetcode.com/graphql", headers=headers, data=json.dumps(query))

    try:
        data = response.json()
    except Exception as e:
        print("❌ Failed to parse JSON:", e)
        print("Raw response:\n", response.text)
        return

    # Check if the response contains submission data
    if "data" not in data or not data["data"].get("submissionList"):
        print("❌ Invalid or expired session. API response:")
        print(json.dumps(data, indent=2))
        return

    submissions = data["data"]["submissionList"]["submissions"]

    # Ensure output directory exists
    os.makedirs("solutions", exist_ok=True)

    # Save each accepted solution
    for sub in submissions:
        if sub["statusDisplay"] == "Accepted":
            # Get file extension based on language
            lang = sub["lang"]
            ext = {
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
            }.get(lang, "txt")

            # Clean filename and save code
            title = sub["title"].replace(" ", "_").replace("/", "_")
            filename = f"solutions/{title}.{ext}"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(sub["code"])
            print(f"✅ Saved: {filename}")

if __name__ == "__main__":
    fetch_submissions()

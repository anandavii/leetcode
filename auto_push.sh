#!/bin/bash

# 👉 Set this to the full path of your local Git repo
REPO_PATH="/Users/abhishek/Projects/leetcode-java"
cd "$REPO_PATH" || { echo "Repo path not found"; exit 1; }

echo "🔄 Watching for changes in Java files in: $REPO_PATH"
echo "⏳ Script will auto-stop after 6 hours."

# 🕒 Track script start time
START_TIME=$(date +%s)
MAX_DURATION=21600  # 6 hours in seconds

while true
do
    # ⏱ Check elapsed time
    CURRENT_TIME=$(date +%s)
    ELAPSED_TIME=$((CURRENT_TIME - START_TIME))

    if [ "$ELAPSED_TIME" -ge "$MAX_DURATION" ]; then
        echo "✅ 6 hours reached. Stopping script."
        break
    fi

    # 👀 Wait for change in .java file only
    CHANGED_FILE=$(fswatch -1 --event Created --event Updated --event Renamed --event Removed -e ".*" -i "\\.java$" .)

    if [ ! -z "$CHANGED_FILE" ]; then
        echo "📄 Detected change in: $CHANGED_FILE"

        git add *.java

        COMMIT_MSG="Auto-commit $(basename "$CHANGED_FILE") on $(date '+%Y-%m-%d %H:%M:%S')"
        git commit -m "$COMMIT_MSG"
        git push origin main

        echo "🚀 Pushed to GitHub with message: $COMMIT_MSG"
    fi
done

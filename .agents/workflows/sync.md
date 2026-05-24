---
description: A two-way sync that pulls remote changes first, then commits and pushes local changes to GitHub.
---

# Sync Workflow

---

## Workflow Instructions

When the user triggers this command, execute these steps:

### Step 1: Commit Local Changes (if any)
1. Run `git status` to check for any uncommitted changes.
2. If there are changes:
   - Run `git add .` to stage all modifications, deletions, and new files.
   - If the user provided a commit message with the slash command (e.g., `/sync "my changes"`), use that.
   - If no message is provided, generate a brief, descriptive commit message based on the staged changes using `git diff --staged`.
   - Run `git commit -m "<commit_message>"`.

### Step 2: Pull Remote Changes
1. Run `git pull` to fetch and merge any updates from the remote GitHub repository. This ensures local is up-to-date with GitHub before pushing.
2. If there are merge conflicts, inform the user and halt the workflow so they can resolve them manually.

### Step 3: Push to Remote
1. Run `git status` to check if there are commits to push (your local branch is ahead of the remote).
2. If there are commits to push, run `git push` to upload them to the remote repository.

### Step 4: Report
1. Inform the user that the sync is complete.
2. Summarize what was pulled from the remote (if anything) and what was pushed from local (if anything).

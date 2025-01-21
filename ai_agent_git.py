from github import Github
import os
import datetime

# Authenticate safely using an environment variable
TOKEN = os.getenv("GITHUB_TOKEN")  # Set this environment variable in your runtime environment
g = Github(TOKEN)

# Get the repository
repo_name = "prafulk9155/daily-publish"

try:
    # Get the repository
    repo = g.get_repo(repo_name)
    print(f"Successfully accessed repository: {repo.full_name}")

    # Create a new file or update an existing one
    file_path = "daily_update.txt"
    commit_message = f"Daily update {datetime.date.today().isoformat()}" # YYYY-MM-DD format
    content = f"Updated on {datetime.datetime.now().isoformat()}"  # ISO format for timestamp

    try:
        # Try to get the file contents
        file = repo.get_contents(file_path)
        print(f"File {file_path} exists, attempting to update")
        repo.update_file(file.path, commit_message, content, file.sha)
        print("File updated successfully")
    except Exception as e:
        # If the file does not exist, create a new one.
        print(f"Error updating file: {str(e)}")
        print("Attempting to create a new file")
        repo.create_file(file_path, commit_message, content)
        print("New file created successfully")

except Exception as e:
    print(f"Error accessing repository: {str(e)}")

# Print information about the authenticated user
user = g.get_user()
print(f"Authenticated as: {user.login}")

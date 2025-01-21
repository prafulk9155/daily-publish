from github import Github
import datetime

# Authenticate
g = Github("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")

# Get the repository
repo = g.get_repo("prafulk9155/daily-publish")


try:
    # Get the repository
    repo = g.get_repo("prafulk9155/daily-publish")
    print(f"Successfully accessed repository: {repo.full_name}")

    # Create a new file or update an existing one
    file_path = "daily_update.txt"
    commit_message = f"Daily update {datetime.date.today()}"
    content = f"Updated on {datetime.datetime.now()}"

    try:
        # Try to get the file contents
        file = repo.get_contents(file_path)
        print(f"File {file_path} exists, attempting to update")
        repo.update_file(file_path, commit_message, content, file.sha)
        print("File updated successfully")
    except Exception as e:
        print(f"Error updating file: {str(e)}")
        print("Attempting to create new file")
        repo.create_file(file_path, commit_message, content)
        print("New file created successfully")

except Exception as e:
    print(f"Error accessing repository: {str(e)}")

# Print information about the authenticated user
user = g.get_user()
print(f"Authenticated as: {user.login}")
# print("Accessible repositories:")
# for repo in user.get_repos():
#     print(f"- {repo.full_name}")

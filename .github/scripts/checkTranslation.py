import sys
import os
from crowdin_api import CrowdinClient

# -----------------------------
# CROWDIN API SCORE
# -----------------------------

def get_score_from_api(lang_id: str, crowdin_file_name: str) -> float:
	"""
	Fetches the translation progress percentage directly from Crowdin API.
	Returns a float between 0.0 and 1.0.
	"""
	token = os.environ.get("crowdinAuthToken")
	project_id = os.environ.get("CROWDIN_PROJECT_ID")

	# Ensure credentials are present
	if not token or not project_id:
		return 0.0

	client = CrowdinClient(token=token)
	try:
		# Normalize the file name (e.g., askOpenRouter.md or askOpenRouter.xliff)
		norm_name = crowdin_file_name.replace('\\', '/').strip('/')
		
		# Fetch all files from the project to find the matching ID
		files = client.source_files.with_full_data().list_files(projectId=project_id)
		file_id = next((f['data']['id'] for f in files['data'] 
					   if f['data']['path'].strip('/') == norm_name), None)
		
		if file_id is None:
			return 0.0

		# Fetch progress for the specific language
		progress = client.translation_status.get_project_progress(project_id, languageId=lang_id)
		for item in progress['data']:
			if item['data']['fileId'] == file_id:
				# Return ratio (0.0 to 1.0)
				return item['data']['translationProgress'] / 100
	except Exception:
		# Fallback to 0.0 in case of API or network error
		return 0.0
	
	return 0.0

# -----------------------------
# MAIN ENGINE
# -----------------------------

def main():
	"""
	Main entry point. 
	Expects two arguments: <file_name> <language_id>
	"""
	if len(sys.argv) < 3:
		sys.exit(2)

	file_name = sys.argv[1]
	lang = sys.argv[2]

	# All evaluations now go through the Crowdin API
	score = get_score_from_api(lang, file_name)
	
	# Output formatting for PowerShell capture (CamelCase)
	if file_name.lower().endswith('.md'):
		print(f"mdScore={score}")
	else:
		print(f"translationRatio={score}")

	# Exit with code 0 if score > 5%, otherwise 1
	sys.exit(0 if score > 0.05 else 1)

if __name__ == "__main__":
	main()
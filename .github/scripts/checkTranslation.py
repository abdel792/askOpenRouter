import sys
import os
import xml.etree.ElementTree as ET
import polib
from crowdin_api import CrowdinClient

def normalize(s: str | None) -> str:
    """Standardizes text for comparison by removing extra whitespace and lowering case."""
    return " ".join((s or "").strip().lower().split())

# -----------------------------
# CROWDIN API SCORE (for MD)
# -----------------------------

def scoreMd(lang_id: str, crowdin_path: str) -> float:
    """
    Fetches the translation percentage of a specific file path from Crowdin.
    Used for Markdown files since local scoring is unreliable.
    """
    token = os.environ.get("crowdinAuthToken")
    project_id = os.environ.get("CROWDIN_PROJECT_ID")

    if not token or not project_id:
        return 0.0

    client = CrowdinClient(token=token)
    try:
        norm_path = crowdin_path.replace('\\', '/').strip('/')
        # Get all files to find the ID corresponding to the path
        files = client.source_files.with_full_data().list_files(projectId=project_id)
        file_id = next((f['data']['id'] for f in files['data'] 
                       if f['data']['path'].strip('/') == norm_path), None)
        
        if file_id is None:
            return 0.0

        # Get translation progress for the language
        progress = client.translation_status.get_project_progress(project_id, languageId=lang_id)
        for item in progress['data']:
            if item['data']['fileId'] == file_id:
                return item['data']['translationProgress'] / 100
    except Exception as e:
        print(f"API Error: {e}", file=sys.stderr)
    
    return 0.0

# -----------------------------
# MULTI-FILE COMPARISON
# -----------------------------

def compareMd(file_list, lang_id):
    """
    Evaluates multiple files (by API path) and prints the winner.
    """
    results = []
    for f in file_list:
        score = scoreMd(lang_id, f)
        results.append((f, score))

    # Sort by score descending
    results.sort(key=lambda x: x[1], reverse=True)
    winner_path, winner_score = results[0]

    print(f"winner_path={winner_path}")
    print(f"winner_score={winner_score}")

# -----------------------------
# LOCAL FILE CHECKERS
# -----------------------------

def checkPo(path: str) -> float:
    """Checks translation ratio for Gettext PO files."""
    po = polib.pofile(path)
    translated = sum(1 for e in po if e.msgid.strip() and e.msgstr and normalize(e.msgstr) != normalize(e.msgid))
    total = sum(1 for e in po if e.msgid.strip())
    return translated / total if total else 0.0

def checkXliff(path: str) -> float:
    """Checks translation ratio for XLIFF files by comparing source and target nodes."""
    tree = ET.parse(path)
    root = tree.getroot()
    translated, total = 0, 0
    
    # Simple XLIFF parser for source/target pairs
    for unit in root.iter():
        if unit.tag.endswith("unit") or unit.tag.endswith("trans-unit"):
            source_node = next((n for n in unit if n.tag.endswith("source")), None)
            target_node = next((n for n in unit if n.tag.endswith("target")), None)
            
            if source_node is not None and source_node.text:
                total += 1
                s_text = normalize(source_node.text)
                t_text = normalize(target_node.text) if target_node is not None else ""
                if t_text and t_text != s_text:
                    translated += 1
                    
    return translated / total if total else 0.0

# -----------------------------
# MAIN ENGINE
# -----------------------------

def main():
    if len(sys.argv) < 2:
        sys.exit(2)

    args = sys.argv[1:]

    # MULTI-FILE MODE (e.g. checkTranslation.py path1 path2 fr)
    if len(args) >= 3:
        *files, lang = args
        compareMd(files, lang)
        sys.exit(0)

    path = args[0]

    # API MODE for Markdown (if file doesn't exist locally or explicitly requested with lang)
    if not os.path.exists(path) and len(args) == 2:
        lang = args[1]
        score = scoreMd(lang, path)
        print(f"api_score={score}")
        sys.exit(0 if score > 0.05 else 1)

    # LOCAL FILE MODE
    ext = os.path.splitext(path)[1].lower()
    if ext == ".po":
        ratio = checkPo(path)
        print(f"translation_ratio={ratio}")
        sys.exit(0 if ratio > 0.05 else 1)
    elif ext in [".xliff", ".xlf"]:
        ratio = checkXliff(path)
        print(f"translation_ratio={ratio}")
        sys.exit(0 if ratio > 0.05 else 1)
    else:
        # For a single local MD file, we check its path against the API
        if len(args) == 2:
            lang = args[1]
            score = scoreMd(lang, path) # We assume the local path matches Crowdin structure
            print(f"api_score={score}")
            sys.exit(0 if score > 0.05 else 1)
        sys.exit(2)

if __name__ == "__main__":
    main()
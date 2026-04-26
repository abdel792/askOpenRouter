import sys
import os
from crowdin_api import CrowdinClient

def get_score_from_api(file_name_to_search: str, lang_id: str) -> float:
    token = os.environ.get("crowdinAuthToken")
    p_id_env = os.environ.get("CROWDIN_PROJECT_ID")

    if not token or not p_id_env:
        print("ERREUR : Variables d'environnement manquantes.")
        return 0.0

    client = CrowdinClient(token=token)
    p_id = int(p_id_env)

    try:
        # Nettoyage du nom recherché (ex: askOpenRouter.po -> askopenrouter)
        base_target = file_name_to_search.replace('\\', '/').split('/')[-1].rsplit('.', 1)[0].lower()
        ext_target = file_name_to_search.split('.')[-1].lower()
        
        # Ce qu'on cherche sur Crowdin
        search_ext = ".pot" if ext_target == "po" else f".{ext_target}"
        
        print(f"-- RECHERCHE : {base_target}{search_ext} --")

        files = client.source_files.list_files(projectId=p_id, limit=500)
        file_id = None
        
        for f in files['data']:
            path_crowdin = f['data']['path'].lower() # ex: /askopenrouter.pot
            
            # TEST DE CORRESPONDANCE
            if path_crowdin.endswith(f"{base_target}{search_ext}"):
                file_id = f['data']['id']
                print(f"MATCH TROUVÉ : {path_crowdin} (ID: {file_id})")
                break
        
        if file_id is None:
            print(f"ECHEC : Aucun fichier dans Crowdin ne finit par '{base_target}{search_ext}'")
            # Petit scan de secours : on affiche les 3 premiers fichiers pour voir le format
            print("Exemples de fichiers vus sur ton Crowdin :")
            for f in files['data'][:3]:
                print(f" - {f['data']['path']}")
            return 0.0

        # Récupération du score
        progress = client.translation_status.get_file_progress(projectId=p_id, fileId=file_id)
        for item in progress['data']:
            if item['data']['languageId'].lower() == lang_id.lower():
                score = float(item['data']['translationProgress']) / 100
                return score
                
    except Exception as e:
        print(f"ERREUR API : {e}")
        return 0.0
    
    return 0.0

def main():
    if len(sys.argv) < 3:
        sys.exit(2)

    input_file = sys.argv[1]
    lang = sys.argv[2]
    score = get_score_from_api(input_file, lang)
    
    print(f"translationRatio={score}")
    if input_file.lower().endswith('.md'):
        print(f"mdScore={score}")
    else:
        print(f"poScore={score}")

    sys.exit(0 if score > 0.05 else 1)

if __name__ == "__main__":
    main()
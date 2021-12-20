import json
import os
import sys

manifest = "installed_content.txt"

# Relevant source folders
mod_folders = {
    'modules': 'data/mod',
    'hak': 'data/hk',
    'tlk': 'data/tlk',
    'localvault': 'data/lcv',
    'movies': 'data/mov',
    'music': 'data/mus',
    'ambient': 'data/amb',
    'erf': 'data/txpk',
    'portraits': 'data/prt',
    'override': 'ovr',
    'docs': 'data/mod_docs'
}

class ContentTracker:
    def __init__(self):
        self.content_map = {}
        if os.path.exists(manifest):
            with open(manifest) as f:
                self.content_map = json.loads(f.read())

    def install_content(self, mod_path):
        content_name = os.path.basename(mod_path)
        if content_name in self.content_map:
            print(f"You've already installed {content_name}")
            sys.exit(0)
        mod_dirs = os.listdir(mod_path)
        self.content_map[content_name] = {}
        for mod_dir in mod_dirs:
            if not mod_dir in mod_folders:
                print(f"{mod_dir} isn't in one of the known mod folders. Not sure what to do with it.") 
                continue

            self.content_map[content_name][mod_dir] = []

            dest_folder = mod_folders[mod_dir]
            for mod_file in os.listdir(os.path.join(mod_path, mod_dir)):
                self.content_map[content_name][mod_dir].append(mod_file)
                # TODO: Actually move files


    def uninstall_content(self, mod_path):
        content_name = os.path.basename(mod_path)
        if not content_name in self.content_map:
            print(f"You don't have {content_name} intalled, or it wasn't installed using this program.")
            sys.exit(0)
        
        remove_content = self.content_map.pop(content_name)
        # TODO: implement removal of a piece of content
        pass

    def list_content(self):
        # TODO: list the mods currently installed
        pass

    def __del__(self):
        with open(manifest, "w") as f:
            f.write(json.dumps(self.content_map))
        pass

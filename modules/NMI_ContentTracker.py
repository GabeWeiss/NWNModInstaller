import json
import os
import shutil
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
    def __init__(self, nwn_dir):
        self.content_map = {}
        self.install_dir = nwn_dir
        if os.path.exists(manifest):
            with open(manifest) as f:
                self.content_map = json.loads(f.read())

    def install_content(self, mod_path):
        content_name = os.path.basename(mod_path)
        if content_name in self.content_map:
            print(f"You've already installed {content_name}")
            sys.exit(0)
        if not os.path.exists(mod_path):
            print("Couldn't find a mod at the specified path, please specify a valid mod.")
            sys.exit(1)
        mod_dirs = os.listdir(mod_path)
        self.content_map[content_name] = {}
        for mod_dir in mod_dirs:
            if not mod_dir in mod_folders:
                print(f"{mod_dir} isn't in one of the known mod folders. Not sure what to do with it.") 
                continue

            dest_folder = mod_folders[mod_dir]
            self.content_map[content_name][dest_folder] = []

            for mod_file in os.listdir(os.path.join(mod_path, mod_dir)):
                source_path = os.path.join(mod_path, mod_dir, mod_file)
                destination_path = os.path.join(self.install_dir, dest_folder, mod_file)
                try:
                    shutil.copy(source_path, destination_path)
                except Exception as ex:
                    print(f"Wasn't able to copy over {mod_file}")
                    sys.exit(1)
                self.content_map[content_name][dest_folder].append(mod_file)


    def uninstall_content(self, mod_path):
        content_name = os.path.basename(mod_path)
        if not content_name in self.content_map:
            print(f"You don't have {content_name} intalled, or it wasn't installed using this program.")
            sys.exit(0)
        
        remove_content = self.content_map.pop(content_name)
        for mod_folder in remove_content:
            for mod_file in remove_content[mod_folder]:
                del_file = os.path.join(self.install_dir, mod_folder, mod_file)
                os.remove(del_file)

    def list_content(self):
        # TODO: list the mods currently installed
        pass

    def __del__(self):
        with open(manifest, "w") as f:
            f.write(json.dumps(self.content_map))
        pass

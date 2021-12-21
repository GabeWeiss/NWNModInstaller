import os
import sys

ini_filename = "NWNModInstaller.ini"

settings_nwn_folder = "nwn_install_dir"


class Settings:
    def __init__(self):
        self.vars = {}

    def initialize_settings(self):
        try:
            ini_file = open(ini_filename, "r")
        except:
            print("Couldn't find or open our ini file. Please reinstall tool.")
            sys.exit(1)
        else:
            for line in ini_file:
                if not line.strip():
                    continue
                key, value = line.split("=")
                self.vars[key] = value
            ini_file.close()

            # prompt to set NWN install dir if it's not yet set
            if not settings_nwn_folder in self.vars:
                print("Install directory for NWN not yet set, please enter path to NWN install directory:")
                path = input('--> ').strip()
                if not path:
                    print("You have not entered a path, exiting.")
                    sys.exit(1)
                else:
                    path_to_check = os.path.join(path.strip(), "bin/win32/nwmain.exe")
                    if not os.path.exists(path_to_check):
                        print("Could not find the NWN install directory specified, please edit your NWNModInstaller.ini and correct the path to the install directory.")
                        sys.exit(1)
                    self.vars[settings_nwn_folder] = path

    def __del__(self):
        with open(ini_filename, "w") as f:
            for k in self.vars:
                f.write(f"{k}={self.vars[k]}\n")
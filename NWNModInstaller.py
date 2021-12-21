import argparse
import os
import sys

sys.path.append('modules')

import NMI_ContentTracker
import NMI_Settings

parser = argparse.ArgumentParser()
# path to the parent folder of the mod we're operating on
parser.add_argument("-m",
                    "--mod",
                     help="Path to the module folder we're operating on.")
parser.add_argument("-r",
                    "--remove",
                    help="-r flag causes module specified to be removed",
                    action="store_true")
parser.add_argument("-l",
                    "--list",
                    help="Lists the installed content.",
                    action="store_true")
args = parser.parse_args()

ini = NMI_Settings.Settings()
ini.initialize_settings()

mods = NMI_ContentTracker.ContentTracker(ini.nwn_install_dir())

if args.remove:
    mods.uninstall_content(args.mod)
elif args.list:
    mods.list_content()
elif args.mod:
    mods.install_content(args.mod)
else:
    parser.print_help()

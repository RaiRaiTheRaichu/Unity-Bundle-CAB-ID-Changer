# Unity Bundle CAB-ID Changer #

This is a modding tool for Unity bundles. The CAB-ID is an MD5 hash of the bundle, stored in the header.

If you use a program like UABE, you can replace textures, swap models, and so on within Unity bundles. If you are modding a Unity game that can load these new bundles, the CAB-ID needs to be unique as well or else Unity will crash. The CAB-ID will not automatically change when you replace the contents of a Unity bundle, therefore changing the ID manually is required. This tool automates that process.

This script supports drag-and-drop file support as well as batch file support.

Currently, changing bundle dependencies is not supported. This may change in the future.

### Requirements ###

* Python 3.12.0

You only need Python if you are not downloading the compiled binary. The binary is created using pyinstaller.

### How To Use ###

- Extract 'CAB_ID_Changer.exe' to an unprotected folder (NOT within Program Files, etc)
- Copy your Unity bundle(s) to the folder containing the 'CAB_ID_Changer.exe'.
- Drag and drop your bundle(s) onto the executable file and it will process all of them.

Alternatively, you can run the script through the command line interface with the following format:
- `CAB_ID_Changer.exe 'someunitybundle.bundle' 'someotherunitybundle' ... 

### Contact ###

* RaiRaiTheRaichu on Discord.

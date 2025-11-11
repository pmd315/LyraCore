This repository contains workspace settings and editor configs to ensure files are saved with UTF-8 encoding.

Files added:
- .vscode/settings.json — sets Visual Studio Code workspace encoding to UTF-8
- .editorconfig — recommends charset = utf-8 for editors that support EditorConfig
- .gitattributes — helps Git treat files as text and normalize line endings

How to change/override:
- To use UTF-8 with BOM in VS Code, set `"files.encoding": "utf8bom"` in the settings.json above.
- You can set User settings instead of workspace settings via VS Code Settings UI.

Verification & conversion examples are in the main instructions provided by the workspace maintainer.

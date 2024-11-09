# Description

## faf_krita_blender.py
Replace the Ctrl+S by this script
When editing a .kra / .krz, running this script will save the document and generate a .png file with the same name as the document.
It also disables hides any node (layer / group) named "UV" when it exports the .png, then reenables it back if it was enabled initially.

I made this script so I could work faster on textures with Blender, without having to say "Export > Overwrite > Confirm settings" every time.

## hide_uv_node.py
Hides / unhides the UV layer or layer group if there's any, by pressing ²
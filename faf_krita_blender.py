from krita import *

activeDocument = Krita.instance().activeDocument()
info = InfoObject()

# Saves the current document so that I can replace the usual Ctrl + S by this script
activeDocument.save()
exportImageFileName = activeDocument.fileName()


does_name_contain_version_number = False
# Only affects .kra files
if exportImageFileName[len(exportImageFileName)-4:] == ".kra" or exportImageFileName[len(exportImageFileName)-4:] == ".krz":
    activeDocument.setBatchmode(True)   # Prevents pop-ups
    if "_" in exportImageFileName:
        for i in range(0, len(exportImageFileName), -1):
            if exportImageFileName[i] == "_":
                if i+1 < len(exportImageFileName):  # Doesn't do it for the first iteration because it would crash
                    if exportImageFileName[i+1] in "0123456789":
                        # Only keeps the name, and not the _01.kra, _02.kra, etc
                        exportImageFileName = exportImageFileName[:i]
                    else:
                        does_name_contain_version_number = False


    if not does_name_contain_version_number:
        # Removes the .kra at the end
        exportImageFileName = exportImageFileName[:len(exportImageFileName)-4]

    # Hides the UV Group / Layer temporarily for export
    uv_node = activeDocument.nodeByName("UV")
    is_uv_node_visible = uv_node.visible()  # Initial state
    if is_uv_node_visible:
        uv_node.setVisible(False)
        activeDocument.refreshProjection()  # If you don't call that method, it basically doesn't update the image, so it doesn't work


    activeDocument.exportImage(f"{exportImageFileName}.png", info)

    # Shows the UV Group / Layer if it was initially visible
    if is_uv_node_visible:
        uv_node.setVisible(True)
        activeDocument.refreshProjection()

    activeDocument.setBatchmode(False)
from krita import *

activeDocument = Krita.instance().activeDocument()

# Hides the UV Group / Layer temporarily for export
uv_node = activeDocument.nodeByName("UV")

if uv_node != None:    # If a node is found
    uv_node.setVisible(not uv_node.visible())
    activeDocument.refreshProjection()
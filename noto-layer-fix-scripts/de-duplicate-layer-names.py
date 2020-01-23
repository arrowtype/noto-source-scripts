#MenuTitle: De-duplicate layer names
# -*- coding: utf-8 -*-
__doc__="""
	Find duplicate layer names and add a serial number to them to keep them unique for FontMake.
"""

font = Glyphs.font

for glyph in font.glyphs:
	print("\n------------------------")
	print(glyph)
	
	layersList = []

	for layer in glyph.layers:
		
		layerName = str(layer.name)
		
		if layerName not in layersList:
			layersList.append(layerName)
			i = 0
			print "\t" + layerName
		
		else:
			newName = layerName + "_" + str(i+1).rjust(3, "0")
			print "\t" + newName
			
			layer.name = newName
			i += 1
			
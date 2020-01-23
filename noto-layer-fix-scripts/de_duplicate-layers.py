#MenuTitle: De-duplicate layers
# -*- coding: utf-8 -*-
__doc__="""
	Check if layers are exact duplicates of others; delete duplicates if so.

	**Work in progress**

	Potential TODO:
	- if layer name matches existing layer name
		- check if layer paths are equal to existing layer paths
		- leave only one layer of the same paths under each master (e.g. allow same layer under each master layer, for drawing help)
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

			print glyph.layers[layerName].paths.nodes
			print layer.paths.nodes

			if layer.paths.keys() == glyph.layers[layerName].paths.keys():
				print "paths equal existing layer"
			
			# layer.name = newName
			i += 1
			
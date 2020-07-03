# CalcMeanStd
# Language: Python
# Input: NOA (nodes and values)
# Output: none (mean and standard deviation printed to the screen)
# Tested with: PluMA 1.1, Python 3.6

PluMA plugin that calculates mean and standard deviation.

The plugin takes input in NOA (Cytoscape NOde Attribute) file format and produces textual output
that shows the mean and the values that are one and two standard deviations away from the mean.

This output can be particularly useful when visualizing a network; with an NOA file each node
has an attribute, so you can assign a color scheme to values depending on their number of deviations
(i.e. red = 2 left, orange = 1 left, yellow = mean, green = 1 right, blue = 2 right).

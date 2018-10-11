class Node:
    def __init__(self, label):
        self.label = label
        self.children = {}
    def addBranch(self, attribute, sub_child):
        self.children.append([attribute, sub_child])
	# you may want to add additional fields here...

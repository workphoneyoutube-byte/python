class Tree:
    def __init__(self,name,type,color):
        self.treeTypeName = name
        self.treeType = type
        self.treeColor = color
        
    def display_info(self):
        print("Tree type name: " + self.treeTypeName)
        print("Tree type: " + self.treeType)
        print("Tree color: " + self.treeColor)

oak = Tree("Oak","Perrenial","Ochre")

oak.display_info()
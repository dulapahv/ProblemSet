# Lossless Compression using Huffman Coding Algorithm - www.101computing.net/lossless-compression-huffman-coding-algorihtm/

# A class used to implement a Binary Tree consisting of Nodes!
class Node(object):
    left = None
    right = None
    item = None
    weight = 0

    def __init__(self, symbol, weight, l=None, r=None):
        self.symbol = symbol
        self.weight = weight
        self.left = l
        self.right = r

  # Called when outputting/printing the node
    def __repr__(self):
        return '("%s", %s, %s, %s)' % (self.symbol, self.weight, self.left, self.right)


def sortByWeight(node):
    # Sort by weight and alphabetical order if same weight
    return (node.weight * 1000000 + ord(node.symbol[0]))

# A Class used to apply the Huffman Coding algorithm to encode / compress a message


class HuffmanEncoder:
    def __init__(self):
        self.symbols = {}
        self.codes = {}
        self.tree = []
        self.message = ""

    def frequencyAnalysis(self):
        self.symbols = {}
        for symbol in self.message:
            self.symbols[symbol] = self.symbols.get(symbol, 0) + 1

    def preorder_traverse(self, node, path=""):
        if node.left == None:
            self.codes[node.symbol] = path
        else:
            self.preorder_traverse(node.left, path+"0")
            self.preorder_traverse(node.right, path+"1")

    def encode(self, message):
        self.message = message
        # Identify the lsit of symbols and their weights / frequency in the message
        self.frequencyAnalysis()

        # Convert list of symbols into a binary Tree structure
        # Step 1: Generate list of Nodes...
        self.tree = []
        for symbol in self.symbols.keys():
            self.tree.append((Node(symbol, self.symbols[symbol], None, None)))

        # Step 2: Sort list of nodes per weight
        self.tree.sort(key=sortByWeight)

        # Step 3: Organise all nodes into a Binary Tree.
        while len(self.tree) > 1:  # Carry on till the tree has only one root node!
            leftNode = self.tree.pop(0)
            rightNode = self.tree.pop(0)
            newNode = Node(leftNode.symbol + rightNode.symbol,
                           leftNode.weight + rightNode.weight, leftNode, rightNode)
            self.tree.append(newNode)
            self.tree.sort(key=sortByWeight)

        # Generate List of Huffman Code for each symbols used...
        self.codes = {}
        self.preorder_traverse(self.tree[0])

        # Encode Message:
        encodedMessage = ""
        for symbol in message:
            encodedMessage = encodedMessage + self.codes[symbol]

        return encodedMessage

    def viewCodes(self):
        print("Huffman Codes:")
        list = []
        for symbol in self.codes.keys():
            code = self.codes[symbol]
            list.append([len(code), symbol, code])
        list.sort()
        for code in list:
            print(code[1] + " : " + code[2])


#####  Start Code Here  ####
message = "lossless_compression"

print(message)
print("")
print("Huffman Coding...")
encoder = HuffmanEncoder()
compressedMessage = encoder.encode(message)
# print(compressedMessage)
# Add spaces between each digit to allow text wrapping
print("".join(compressedMessage))
print("")
encoder.viewCodes()

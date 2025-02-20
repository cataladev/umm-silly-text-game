class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.locations = set()
        self.action = None
        self.description = ""  # Add description field

class CommandTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, command_words, locations, action, description=""):
        node = self.root
        for word in command_words:
            if word not in node.children:
                node.children[word] = TrieNode()
            node = node.children[word]
        node.is_end = True
        node.locations.update(locations)
        node.action = action
        node.description = description  # Store description

    def search(self, command_words, current_location):
        node = self.root
        for word in command_words:
            if word not in node.children:
                return None
            node = node.children[word]
        if node.is_end and current_location in node.locations:
            return node.action
        return None

    def get_all_commands(self, current_location):
        commands = []
        self._collect_commands(self.root, [], current_location, commands)
        return commands

    def _collect_commands(self, node, prefix, current_location, commands):
        if node.is_end and current_location in node.locations:
            commands.append((" ".join(prefix), node.description))
        for word, child in node.children.items():
            self._collect_commands(child, prefix + [word], current_location, commands)
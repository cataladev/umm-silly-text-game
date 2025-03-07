class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.locations = set()
        self.action = None
        self.description = ""

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
        node.description = description

    def search(self, command_words, current_location):
        node = self.root
        depth = 0
        last_valid_action = None
        
        # Find the deepest matching command
        for word in command_words:
            if word not in node.children:
                break
            node = node.children[word]
            depth += 1
            if node.is_end and (current_location in node.locations or "*" in node.locations):
                last_valid_action = node.action
        
        return last_valid_action

    def get_all_commands(self, current_location):
        commands = []
        self._collect_commands(self.root, [], current_location, commands)
        return commands

    def _collect_commands(self, node, prefix, current_location, commands):
        if node.is_end and (current_location in node.locations or "*" in node.locations):
            commands.append((" ".join(prefix), node.description))
        for word, child in node.children.items():
            self._collect_commands(child, prefix + [word], current_location, commands)
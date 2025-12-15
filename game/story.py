from typing import Dict, List

class StoryNode:
    def __init__(self, id: str, content: str, choices: Dict[str, str], requirements: Dict[str, any] = None):
        self.id = id
        self.content = content
        self.choices = choices
        self.requirements = requirements or {}  # Add this line

class Story:
    def __init__(self, title: str, starting_node: str):
        self.title = title
        self.nodes: Dict[str, StoryNode] = {}
        self.current_node_id = starting_node

    def add_node(self, node: StoryNode):
        self.nodes[node.id] = node

    def get_current_node(self) -> StoryNode:
        return self.nodes.get(self.current_node_id)

def create_basic_story() -> Story:
    story = Story("Basic Adventure", "start")
    
    # Create a simple branching story
    story.add_node(StoryNode(
        "start",
        "You stand at a crossroads. To the north is a dark forest, to the east is a mountain path.",
        {
            "go north": "forest",
            "go east": "mountain",
            "check inventory": "check_items"
        }
    ))

    story.add_node(StoryNode(
        "forest",
        "The forest is dense and dark. You hear rustling in the bushes.",
        {
            "investigate noise": "forest_encounter",
            "return to crossroads": "start",
            "check inventory": "check_items"
        }
    ))

    story.add_node(StoryNode(
        "mountain",
        "The mountain path is steep but clear. You see a cave entrance nearby.",
        {
            "enter cave": "cave",
            "return to crossroads": "start",
            "check inventory": "check_items"
        }
    ))

    story.add_node(StoryNode(
        "check_items",
        "You check your belongings.",
        {
            "continue": "start"  # Changed from "return_to_previous"
        }
    ))

    # Add missing nodes to prevent dead ends
    story.add_node(StoryNode(
        "forest_encounter",
        "You investigate the noise and find a small clearing.",
        {
            "return to forest": "forest"
        }
    ))

    story.add_node(StoryNode(
        "cave",
        "The cave is dark and mysterious.",
        {
            "return to mountain": "mountain"
        }
    ))

    return story

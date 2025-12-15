from .story import Story, StoryNode
from .player import Player

class AIDM:
    def __init__(self, story: Story):
        self.story = story
        self.current_node = story.get_current_node()

    def process_action(self, action: str, player: Player) -> dict:
        # Get current story node
        current_node = self.story.get_current_node()
        
        # Handle 'start' command
        if action == 'start':
            return {
                "success": True,
                "message": current_node.content,
                "choices": list(current_node.choices.keys())
            }
        
        # Check if action matches any available choices
        for choice_text, next_node_id in current_node.choices.items():
            if action.lower() in choice_text.lower():
                # Check requirements if any
                if self._check_requirements(current_node, player):
                    self.story.current_node_id = next_node_id
                    new_node = self.story.get_current_node()
                    return {
                        "success": True,
                        "message": new_node.content,
                        "choices": list(new_node.choices.keys())
                    }
                else:
                    return {
                        "success": False,
                        "message": "You don't meet the requirements for this action.",
                        "choices": list(current_node.choices.keys())
                    }
        
        return {
            "success": False,
            "message": "I don't understand that action. Available choices are: " + 
                      ", ".join(current_node.choices.keys()),
            "choices": list(current_node.choices.keys())
        }

    def _check_requirements(self, node: StoryNode, player: Player) -> bool:
        if not hasattr(node, 'requirements') or not node.requirements:
            return True
            
        # Add requirement checking logic here
        return True

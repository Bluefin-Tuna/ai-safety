from general import TOGETHER_API_KEY
from cai.util import load_constitution
from together import Together

critique_model = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"

class Critique:
    def __init__(self) -> None:
        self.client = Together(TOGETHER_API_KEY)
    
    def critique(self, response: str, constitution: list[str] = load_constitution()):
        self.client.chat.completions.create(response)
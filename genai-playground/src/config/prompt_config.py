from dataclasses import dataclass

@dataclass
class GenerationConfig:

    temperature: float = 0.3

    top_k: int = 50
     
    top_p: float = 0.9

    frequency_penalty: float = 0

    presence_penalty: float = 0

    max_tokens: int = 1024

    system_prompt: str = (
        "You are a helpful AI assistant."
    )

    stream: bool = True
from  providers.base import BaseProvider
from providers.gemini_provider import GeminiProvider
from providers.ollama_provider import OllamaProvider
from providers.groq_provider import GroqProvider
from providers.openai_provider import OpenAIProvider


class ProviderFactory:

    providers: dict[str, BaseProvider] = {
        "ollama": OllamaProvider,
        "gemini": GeminiProvider,
        "groq": GroqProvider,
        "openai": OpenAIProvider,
    }

    @classmethod
    def get_provider(cls, provider:str) -> BaseProvider:

        return cls.providers[provider]()
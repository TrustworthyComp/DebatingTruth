"""
Debate participant classes
"""

from .agent import Agent
from ..utils.openai_client import OpenAIClient


class DebatePlayer(Agent):
    """Debate participant class"""
    
    def __init__(self, 
                 model_name: str,
                 name: str,
                 temperature: float,
                 openai_client: OpenAIClient,
                 sleep_time: float = 0):
        super().__init__(model_name, name, temperature, openai_client, sleep_time)


class AffirmativePlayer(DebatePlayer):
    """Affirmative debater"""
    
    def __init__(self, 
                 model_name: str,
                 temperature: float,
                 openai_client: OpenAIClient,
                 sleep_time: float = 0):
        super().__init__(model_name, "Affirmative side", temperature, openai_client, sleep_time)


class NegativePlayer(DebatePlayer):
    """Negative debater"""
    
    def __init__(self,
                 model_name: str, 
                 temperature: float,
                 openai_client: OpenAIClient,
                 sleep_time: float = 0):
        super().__init__(model_name, "Negative side", temperature, openai_client, sleep_time)


class ModeratorPlayer(DebatePlayer):
    """Moderator"""
    
    def __init__(self,
                 model_name: str,
                 temperature: float, 
                 openai_client: OpenAIClient,
                 sleep_time: float = 0):
        super().__init__(model_name, "Moderator", temperature, openai_client, sleep_time)


class JudgePlayer(DebatePlayer):
    """Judge/Judicator"""
    
    def __init__(self,
                 model_name: str,
                 temperature: float,
                 openai_client: OpenAIClient, 
                 sleep_time: float = 0):
        super().__init__(model_name, "Judge", temperature, openai_client, sleep_time)

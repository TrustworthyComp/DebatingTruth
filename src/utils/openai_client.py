"""
OpenAI client wrapper
"""

import backoff
import time
import tiktoken
from typing import List, Dict
from openai import OpenAI, RateLimitError, APIError, APIConnectionError


MODEL_MAX_CONTEXT = {
    "gpt-4o-mini": 7900,
    "gpt-4o": 7900,
}

DEFAULT_MAX_CONTEXT = 7900


class OpenAIClient:
    """OpenAI client wrapper class"""
    
    def __init__(self, 
                 api_key: str,
                 base_url: str,
                 sleep_time: float = 0):
        """
        Initialize OpenAI client
        
        Args:
            api_key: OpenAI API key
            base_url: API base URL
            sleep_time: Request interval time
        """
        self.api_key = api_key
        self.sleep_time = sleep_time
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.encoding = tiktoken.get_encoding("cl100k_base")
    
    def num_tokens_from_string(self, text: str) -> int:
        return len(self.encoding.encode(text))
    
    @backoff.on_exception(backoff.expo, (RateLimitError, APIError, APIConnectionError), max_tries=3)
    def chat_completion(self, 
                       model_name: str,
                       messages: List[Dict[str, str]],
                       temperature: float = 0.7,
                       max_tokens: int = 512,
                       top_p: float = 1.0) -> str:
        """
        Send chat completion request
        
        Args:
            model_name: Model name
            messages: Message list
            temperature: Temperature parameter
            max_tokens: Maximum token count
            top_p: Top-p parameter
            
        Returns:
            Generated text
        """
        time.sleep(self.sleep_time)
        
        response = self.client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=False,
            top_p=top_p,
        )
        
        try:
            return response['choices'][0]['message']['content']
        except (KeyError, TypeError):
            return response.choices[0].message.content



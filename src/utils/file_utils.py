"""
File operation utilities
"""

import json
import os
from typing import List, Dict, Any, Union


class FileUtils:
    """File operation utility class"""
    
    @staticmethod
    def load_json(file_path: str) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Load JSON file
        
        Args:
            file_path: JSON file path
            
        Returns:
            JSON data
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    return [json.loads(line.strip()) for line in f if line.strip()]
            except Exception:
                raise ValueError(f"Cannot parse JSON file: {file_path}")
        except Exception as e:
            raise ValueError(f"Cannot read file {file_path}: {e}")
    
    @staticmethod
    def save_json(data: Union[List[Dict[str, Any]], Dict[str, Any]], 
                  file_path: str, 
                  indent: int = 4,
                  ensure_ascii: bool = False) -> None:
        """
        Save JSON file
        
        Args:
            data: Data to save
            file_path: File path
            indent: Indentation spaces
            ensure_ascii: Whether to ensure ASCII encoding
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=ensure_ascii, indent=indent)
    
    @staticmethod
    def create_output_dir(base_dir: str, 
                         debate_model: str,
                         judge_model: str,
                         config_name: str,
                         is_train: bool = False,
                         evidence_type: str = "hero",
                         ) -> str:
        """
        Create output directory
        
        Args:
            base_dir: Base directory
            debate_model: Debate model name
            judge_model: Judge model name
            config_name: Configuration name
            is_train: Whether it is training data
            evidence_type: Evidence type
            
        Returns:
            Output directory path
        """
        dir_name = f"{'train' if is_train else 'dev'}_D{debate_model}_J{judge_model}_{config_name}_{evidence_type}"
        
        output_dir = os.path.join(base_dir, dir_name)
        os.makedirs(output_dir, exist_ok=True)
        
        return output_dir
    
    @staticmethod
    def get_processed_claims(output_dir: str) -> set:
        """
        Get list of processed claim IDs
        
        Args:
            output_dir: Output directory
            
        Returns:
            Set of processed claim IDs
        """
        if not os.path.exists(output_dir):
            return set()
        
        processed_claims = set()
        for filename in os.listdir(output_dir):
            if filename.endswith('.json') and not filename.endswith('-config.json'):
                try:
                    claim_id = int(filename.split('.json')[0])
                    processed_claims.add(claim_id)
                except ValueError:
                    continue
        
        return processed_claims

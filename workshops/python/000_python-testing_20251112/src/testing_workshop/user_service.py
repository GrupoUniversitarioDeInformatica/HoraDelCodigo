"""User service for testing external dependencies."""

from typing import Dict, Optional

import requests


class UserService:
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url

    def get_user(self, user_id: int) -> Optional[Dict]:
        response = requests.get(f"{self.base_url}/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        return None

    def create_user(self, name: str, email: str) -> Dict:
        data = {"name": name, "email": email}
        response = requests.post(f"{self.base_url}/users", json=data)
        return response.json()

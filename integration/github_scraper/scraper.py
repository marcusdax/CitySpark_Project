# 🔗 CitySpark GitHub Integration
# GitHub repository scraping and asset management

from typing import Dict, List, Any, Optional
from datetime import datetime
import requests
import json


class GitHubScraper:
    """Handles GitHub repository scraping and asset management"""

    def __init__(self, api_token: Optional[str] = None):
        self.api_token = api_token
        self.base_url = "https://api.github.com"
        self.repositories = {}
        self.assets = {}

    def scrape_repository(self, repo_url: str) -> Dict[str, Any]:
        """Scrape a GitHub repository for educational content"""
        # Extract owner and repo from URL
        parts = repo_url.strip("/").split("/")
        if len(parts) < 2:
            raise ValueError("Invalid repository URL")

        owner, repo = parts[-2], parts[-1]

        repo_data = self._fetch_repository_data(owner, repo)
        contents = self._fetch_repository_contents(owner, repo)

        scraped_repo = {
            "id": f"{owner}_{repo}",
            "name": repo_data.get("name", repo),
            "full_name": repo_data.get("full_name", f"{owner}/{repo}"),
            "description": repo_data.get("description", ""),
            "language": repo_data.get("language", ""),
            "stars": repo_data.get("stargazers_count", 0),
            "forks": repo_data.get("forks_count", 0),
            "updated_at": repo_data.get("updated_at", ""),
            "contents": contents,
            "educational_files": self._filter_educational_files(contents),
            "scraped_at": datetime.now().isoformat(),
        }

        self.repositories[scraped_repo["id"]] = scraped_repo
        return scraped_repo

    def _fetch_repository_data(self, owner: str, repo: str) -> Dict[str, Any]:
        """Fetch basic repository data from GitHub API"""
        url = f"{self.base_url}/repos/{owner}/{repo}"
        headers = {}

        if self.api_token:
            headers["Authorization"] = f"token {self.api_token}"

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def _fetch_repository_contents(
        self, owner: str, repo: str, path: str = ""
    ) -> List[Dict[str, Any]]:
        """Fetch repository contents recursively"""
        url = f"{self.base_url}/repos/{owner}/{repo}/contents/{path}"
        headers = {}

        if self.api_token:
            headers["Authorization"] = f"token {self.api_token}"

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        contents = response.json()
        all_contents = []

        if isinstance(contents, list):
            for item in contents:
                if item["type"] == "file":
                    all_contents.append(item)
                elif item["type"] == "dir":
                    # Recursively fetch directory contents
                    sub_contents = self._fetch_repository_contents(
                        owner, repo, item["path"]
                    )
                    all_contents.extend(sub_contents)

        return all_contents

    def _filter_educational_files(
        self, contents: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Filter contents for educational files"""
        educational_extensions = [
            ".md",
            ".txt",
            ".py",
            ".js",
            ".html",
            ".css",
            ".ipynb",
            ".pdf",
            ".doc",
            ".docx",
        ]
        educational_keywords = [
            "tutorial",
            "guide",
            "learn",
            "education",
            "course",
            "example",
            "demo",
            "documentation",
            "readme",
        ]

        educational_files = []

        for file in contents:
            if file["type"] != "file":
                continue

            file_name = file["name"].lower()
            file_path = file["path"].lower()

            # Check extension
            has_educational_extension = any(
                file_name.endswith(ext) for ext in educational_extensions
            )

            # Check keywords in path or name
            has_educational_keyword = any(
                keyword in file_path for keyword in educational_keywords
            )

            if has_educational_extension or has_educational_keyword:
                educational_files.append(
                    {
                        **file,
                        "educational_relevance": self._calculate_educational_relevance(
                            file
                        ),
                        "categorized_as": self._categorize_educational_file(file),
                    }
                )

        return educational_files

    def _calculate_educational_relevance(self, file: Dict[str, Any]) -> float:
        """Calculate how educationally relevant a file is"""
        relevance_score = 0.5  # Base score

        file_name = file["name"].lower()
        file_path = file["path"].lower()

        # Bonus for educational keywords
        if any(word in file_path for word in ["tutorial", "guide", "learn"]):
            relevance_score += 0.3
        if any(word in file_path for word in ["example", "demo"]):
            relevance_score += 0.2
        if file_name.startswith("readme"):
            relevance_score += 0.2

        return min(relevance_score, 1.0)

    def _categorize_educational_file(self, file: Dict[str, Any]) -> str:
        """Categorize an educational file"""
        file_name = file["name"].lower()
        file_path = file["path"].lower()

        if file_name.startswith("readme"):
            return "documentation"
        elif "tutorial" in file_path:
            return "tutorial"
        elif "example" in file_path or "demo" in file_path:
            return "example"
        elif file_name.endswith((".py", ".js", ".html", ".css")):
            return "code"
        elif file_name.endswith((".md", ".txt")):
            return "documentation"
        else:
            return "resource"

    def get_educational_assets(self, repo_id: str) -> List[Dict[str, Any]]:
        """Get educational assets from a scraped repository"""
        if repo_id not in self.repositories:
            raise ValueError(f"Repository {repo_id} not found")

        repo = self.repositories[repo_id]
        return repo.get("educational_files", [])

    def search_repositories(
        self, query: str, educational: bool = True
    ) -> List[Dict[str, Any]]:
        """Search GitHub for repositories"""
        search_query = query
        if educational:
            search_query += " educational tutorial"

        url = f"{self.base_url}/search/repositories"
        params = {"q": search_query, "sort": "stars", "order": "desc", "per_page": 20}
        headers = {}

        if self.api_token:
            headers["Authorization"] = f"token {self.api_token}"

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        search_results = response.json()
        return search_results.get("items", [])

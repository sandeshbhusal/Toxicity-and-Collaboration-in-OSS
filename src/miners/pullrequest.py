"""
Mines the pull request of a particular repository
"""

from typing import *
from requests import get as Get, Response
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')  # Add this line


def minePullRequest(owner: str, repo: str) -> Optional[List[dict]]:
    TOKEN = "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"
    
    log = logging.getLogger("minePullRequest") 

    response: Response = Get(
        f"https://api.github.com/repos/{owner}/{repo}/pulls",
        headers={
            "accept": "application/vnd.github+json",
            "user-agent": "bsu-msr-mr-sb",
            "X-Github-Api-Version": "2022-11-28",
            "Authorization": f"Bearer {TOKEN}",
        },
        
        params={"state": "closed", "per-page": 1},
    )

    if response.status_code != 200:
        log.error(f"Got a non-200 status code: {response.status_code}")
        try:
            log.error(f"Body is: {response.json()}")
            
        except Exception as e:
            log.error(f"Error getting body of response: {e}")
            
        return None

    try:
        return response.json()
    except Exception as e:
        return None

def minePullRequestComment(owner: str, repo: str, pull_id: int) -> Optional[List[dict]]:
    TOKEN = "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"
    
    log = logging.getLogger("minePullRequestComment")

    response: Response = Get(
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_id}/comments",
        headers={
            "accept": "application/vnd.github+json",
            "user-agent": "bsu-msr-mr-sb",
            "X-Github-Api-Version": "2022-11-28",
            "Authorization": f"Bearer {TOKEN}",
        },
        
        params={"state": "closed", "per-page": 1},
    )

    if response.status_code != 200:
        log.error(f"Got a non-200 status code: {response.status_code}")
        try:
            log.error(f"Body is: {response.json()}")
            
        except Exception as e:
            log.error(f"Error getting body of response: {e}")
            
        return None

    try:
        return response.json()
    except Exception as e:
        return None

if __name__ == "__main__":
    prs: Optional[List[dict]] = minePullRequest("sirupsen", "logrus")
     
    if prs is not None:
        for pull_request in prs:
            # Get the pull request id.
            identifier = pull_request["number"]
            
            # Get review comments.
            comments: Optional[List[dict]] = minePullRequestComment("sirupsen", "logrus", identifier)
            if comments is not None:
                for comment in comments:
                    print(comment["user"]["login"] + " said " + comment["body"]) 
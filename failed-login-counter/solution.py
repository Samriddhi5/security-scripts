"""
Failed Login Counter - Brute Force Detection
Problem: Given a list of login attempts, return users who failed more than once.
Time complexity: O(n) - single pass through the list
"""

def failed_logins(attempts):
    result = {}
    for attempt in attempts:
        if attempt["status"] == "failed":
            result[attempt["user"]] = result.get(attempt["user"], 0) + 1
    return {
        user: {"count": count, "risk": "high" if count > 3 else "normal"}
        for user, count in result.items()
        if count > 1
    }

# Test
login_attempts = [
    {"user": "alice", "status": "failed"},
    {"user": "bob", "status": "success"},
    {"user": "alice", "status": "failed"},
    {"user": "charlie", "status": "failed"},
    {"user": "alice", "status": "failed"},
    {"user": "bob", "status": "failed"},
    {"user": "charlie", "status": "failed"},
]

print(failed_logins(login_attempts))
# Expected: {"alice": {"count": 3, "risk": "normal"}, "charlie": {"count": 2, "risk": "normal"}}

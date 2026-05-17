"""
Permission Baseline Checker - Least Privilege Enforcement
Problem: Return users with permissions beyond their role baseline.
Time complexity: O(n) - single pass, set difference per user
"""

def check_permissions(users, baselines):
    result = {}
    for user, info in users.items():
        role = info["role"]
        user_perms = info["permissions"]
        baseline = baselines.get(role, [])
        extra = list(set(user_perms) - set(baseline))
        if extra:
            result[user] = extra
    return result

# Test
users = {
    "alice": {"role": "developer", "permissions": ["read", "write", "deploy"]},
    "bob": {"role": "analyst", "permissions": ["read", "write", "admin"]},
    "charlie": {"role": "developer", "permissions": ["read", "write"]},
}

baselines = {
    "developer": ["read", "write", "deploy"],
    "analyst": ["read", "write"],
}

print(check_permissions(users, baselines))
# Expected: {"bob": ["admin"]}

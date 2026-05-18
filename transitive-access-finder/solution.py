"""
Transitive Access Finder - IAM Privilege Escalation Detection
Problem: Find users who have access to sensitive resources through group memberships.
Time complexity: O(u * g * r) - users * groups per user * resources per group
Real-world use: SoD violation detection, privileged access reviews in SailPoint/Saviynt
"""

def check_mappings(user_groups, group_resources, sensitive):
    result = {}
    for user, groups in user_groups.items():
        user_resources = []
        for group in groups:
            for resource in group_resources.get(group, []):
                if resource not in user_resources:
                    user_resources.append(resource)
        flagged = [r for r in user_resources if r in sensitive]
        if flagged:
            result[user] = flagged
    return result

# Test
user_groups = {
    "alice": ["engineering", "analytics"],
    "bob": ["analytics"],
    "charlie": ["engineering", "admin"],
}

group_resources = {
    "engineering": ["code_repo", "dev_database"],
    "analytics": ["reports", "dev_database"],
    "admin": ["prod_database", "user_management"],
}

sensitive = ["prod_database", "user_management"]

print(check_mappings(user_groups, group_resources, sensitive))
# Expected: {"charlie": ["prod_database", "user_management"]}

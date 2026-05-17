"""
Anomalous Login Detector - Lateral Movement Detection
Problem: Flag users who accessed 3+ distinct systems within a 5-minute window.
Time complexity: O(n^3) - three nested loops
Optimization note: sliding window with two pointers would reduce to O(n)
"""

def detect_anomalous(events):
    # Group events by user
    user_events = {}
    for event in events:
        user = event["user"]
        if user not in user_events:
            user_events[user] = []
        user_events[user].append((event["time"], event["system"]))

    flagged = {}
    for user, events in user_events.items():
        for i in range(len(events)):
            window_systems = []
            for j in range(i, len(events)):
                if events[j][0] - events[i][0] <= 5:
                    if events[j][1] not in window_systems:
                        window_systems.append(events[j][1])
                else:
                    break
            if len(window_systems) >= 3:
                flagged[user] = window_systems
                break
    return flagged

# Test
login_events = [
    {"user": "alice", "time": 1, "system": "email"},
    {"user": "alice", "time": 3, "system": "database"},
    {"user": "alice", "time": 4, "system": "payroll"},
    {"user": "bob", "time": 1, "system": "email"},
    {"user": "bob", "time": 10, "system": "database"},
    {"user": "charlie", "time": 1, "system": "email"},
    {"user": "charlie", "time": 2, "system": "database"},
    {"user": "charlie", "time": 3, "system": "payroll"},
    {"user": "charlie", "time": 4, "system": "vpn"},
]

print(detect_anomalous(login_events))
# Expected: {"charlie": ["email", "database", "payroll", "vpn"]}

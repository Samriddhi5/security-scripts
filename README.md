# Security Scripts

Python scripts built for security detection use cases. Each script 
addresses a real security problem with an explanation of the approach, 
time complexity, and potential improvements.

## Scripts

### 1. Failed Login Counter - Brute Force Detection
Detects users with multiple failed login attempts. Returns a dictionary 
of flagged users with fail counts and risk labels.

- Technique: Dictionary filtering, counter pattern
- Time complexity: O(n)
- Real-world use: SIEM correlation rule baseline, Splunk alert logic

[View solution](./failed-login-counter/solution.py)

---

### 2. Anomalous Login Detector - Lateral Movement Detection
Flags users who accessed 3 or more distinct systems within a 5-minute 
window — a common lateral movement indicator.

- Technique: Nested loops with time window, sliding window optimization
- Time complexity: O(n³) current, O(n) with sliding window optimization
- Real-world use: SOC alert for lateral movement, UBA baseline

[View solution](./anomalous-login-detector/solution.py)

---

### 3. Permission Baseline Checker - Least Privilege Enforcement
Compares user permissions against role baselines and flags any user 
with permissions beyond their role definition.

- Technique: Set difference, dictionary iteration
- Time complexity: O(n)
- Real-world use: IAM access review automation, SoD policy enforcement

[View solution](./permission-baseline-checker/solution.py)

---

### 4. Transitive Access Finder - IAM Privilege Escalation Detection
Identifies users who have access to sensitive resources through group 
memberships - the same logic used in IAM access reviews and SoD 
violation detection.

- Technique: Nested iteration, set membership check
- Time complexity: O(u × g × r) - users × groups × resources
- Real-world use: Privileged access reviews, SoD violation detection 
  in SailPoint and Saviynt

[View solution](./transitive-access-finder/solution.py)

---

## Why these problems

These scripts mirror real detection logic used in SOC operations and 
IAM governance:

- Failed login counter → the logic behind Splunk brute force detection rules
- Anomalous login detector → the logic behind lateral movement alerts in SIEM
- Permission baseline checker → the logic behind automated access reviews 
  in SailPoint and Saviynt
- Transitive access finder → the logic behind SoD violation detection 
  and privileged access reviews in enterprise IAM platforms

Built as part of ongoing security engineering practice.

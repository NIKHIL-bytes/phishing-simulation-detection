import re

PHISHING_KEYWORDS = [
    "verify",
    "suspended",
    "urgent",
    "click",
    "login"
]

def detect_phishing(email):
    score = 0

    for word in PHISHING_KEYWORDS:
        if re.search(word, email, re.IGNORECASE):
            score += 1

    if "http://" in email and "https://" not in email:
        score += 1

    return score

if __name__ == "__main__":
    with open("sample_emails.txt", "r") as f:
        emails = f.read().split("---")

    for email in emails:
        score = detect_phishing(email)
        result = "Phishing Suspected" if score >= 2 else "Likely Safe"
        print(result)
        print(email.strip())
        print("=" * 50)

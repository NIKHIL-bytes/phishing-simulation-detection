def load_emails():
    with open("sample_emails.txt", "r") as f:
        return f.read().split("---")

def simulate():
    emails = load_emails()
    print("Loaded email samples:\n")
    for i, email in enumerate(emails, 1):
        print(f"Email {i}")
        print(email.strip())
        print("-" * 40)

if __name__ == "__main__":
    simulate()

# ai_agents/ai_reviewer_feedback.py

def ai_reviewer_feedback(revised_text):
    print("\n[4] Human-in-the-loop phase initiated...")
    print("\n>> Human-in-the-loop: Final Review\n")

    print("--- AI Reviewed Chapter Preview ---\n")
    print(revised_text[:1000])  # show first 1000 characters

    while True:
        decision = input("\n[H]uman edits / [A]ccept / [R]eject? ").strip().upper()
        if decision in ['H', 'A', 'R']:
            break
        else:
            print("Invalid input. Please enter H, A, or R.")

    return decision


# === ai_agents/human_loop.py ===

def human_review_interface(reviewed_text):
    print("\n>> Human-in-the-loop: Final Review")
    print("\n--- AI Reviewed Chapter Preview ---\n")
    print(reviewed_text[:1000] + ("..." if len(reviewed_text) > 1000 else ""))

    while True:
        choice = input("\n[H]uman edits / [A]ccept / [R]eject? ").strip().lower()
        if choice == 'a':
            return reviewed_text
        elif choice == 'r':
            print("\nRewriting rejected. Returning original reviewed version.")
            return reviewed_text
        elif choice == 'h':
            print("\nEnter your final edits below (end with a blank line):")
            edited_lines = []
            while True:
                line = input()
                if not line:
                    break
                edited_lines.append(line)
            return "\n".join(edited_lines)
        else:
            print("Invalid input. Try again.")

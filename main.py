# === automated_book_workflow/main.py ===
from dotenv import load_dotenv
load_dotenv()

from scraper.scraper import scrape_chapter
from scraper.screenshot import capture_screenshot
from ai_agents.writer import ai_writer_spin
from ai_agents.ai_reviewer_feedback import ai_reviewer_feedback
from ai_agents.human_loop import human_review_interface
from rl_model.reward_engine import evaluate_output_quality
from storage.chromadb_interface import store_version, search_versions
from storage.voice_module import read_aloud_text


def main():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    print("\n[1] Fetching content from:", url)
    
    original_text = scrape_chapter(url)
    capture_screenshot(url, "screenshots/chapter1.png")

    print("\n[2] Running AI Writer spin...")
    ai_written = ai_writer_spin(original_text)

    print("\n[3] Reviewer evaluating AI-written content...")
    reviewed_output = ai_reviewer_feedback(ai_written)

    print("\n[4] Human-in-the-loop phase initiated...")
    final_output = human_review_interface(reviewed_output)

    print("\n[5] Evaluating with RL reward model...")
    score = evaluate_output_quality(original_text, final_output)
    print(f"\nRL Reward Score: {score:.2f}")

    print("\n[6] Storing versions in ChromaDB...")
    store_version("Chapter_1", final_output, metadata={"reward_score": score})

    print("\n[7] Reading aloud final chapter (voice support)...")
    read_aloud_text(final_output)

    print("\n✅ Workflow Complete. All versions stored and processed.")


if __name__ == "__main__":
    main()

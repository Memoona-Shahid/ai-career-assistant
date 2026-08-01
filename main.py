"""
Entry point for the AI Career Assistant application.
"""

from career_assistant import CareerAssistant
from logger import logger
from utils import welcome


def main() -> None:
    """
    Start the AI Career Assistant application.
    """

    logger.info("Starting AI Career Assistant.")

    welcome()

    assistant = CareerAssistant()

    assistant.start_chat()


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:

        logger.warning("Application interrupted by user.")

        print("\n\nApplication interrupted.")

    except Exception:

        logger.exception("Unexpected application error.")

        print("\nAn unexpected error occurred.")
        print("Please check logs/assistant.log for details.")
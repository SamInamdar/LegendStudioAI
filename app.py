"""
Legend Studio AI

Application Entry Point
"""

from core.bootstrap.bootstrap import Bootstrap


def main() -> None:
    """Application entry point."""
    Bootstrap().run()


if __name__ == "__main__":
    main()
"""Training entry point — placeholder for Day 1, will grow each phase."""

import logging

from ml_engineering.utils import load_config, setup_logging


def main() -> None:
    setup_logging()
    logger = logging.getLogger(__name__)
    config = load_config("configs/base.yaml")
    logger.info("Starting training run with config: %s", config["project"]["name"])
    logger.info("Seed: %s", config["project"]["seed"])
    logger.info("Training entry point ready — model code coming Day 5+")


if __name__ == "__main__":
    main()

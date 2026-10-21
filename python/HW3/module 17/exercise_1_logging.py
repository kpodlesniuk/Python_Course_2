#!/usr/bin/env python3

"""Exercise 1: Temperature Sensor Logging.

Create a function that generates a random temperature every second
for three minutes and logs the generated values using different
logging levels.
"""

import logging
import random
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("sensor.log")
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def run_sensor(duration=180):
    """Generate and log random temperature values.

    Args:
        duration: Number of seconds to run the sensor.
    """
    temperatures = []
    start_time = time.time()

    logger.info("Sensor started.")

    try:
        while time.time() - start_time < duration:
            value = random.randint(-10, 50)
            temperatures.append(value)

            logger.debug(f"Generated temperature: {value}")

            if value > 45:
                logger.critical(f"Critical temperature: {value}")
            elif value > 35:
                logger.warning(f"High temperature: {value}")
            elif value < 0:
                logger.error(f"Temperature below zero: {value}")

            time.sleep(1)

    except KeyboardInterrupt:
        logger.exception("Sensor interrupted by user.")

    finally:
        if temperatures:
            logger.info(
                f"Summary: count={len(temperatures)}, "
                f"min={min(temperatures)}, max={max(temperatures)}"
            )

        logger.info("Sensor stopped.")


run_sensor()

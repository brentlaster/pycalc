import logging
from typing import Optional
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    result = a + b
    logging.info(f"Adding {a} and {b}: {result}")
    return result

def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The result of subtracting b from a.
    """
    result = a - b
    logging.info(f"Subtracting {b} from {a}: {result}")
    return result

def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.
    """
    result = a * b
    logging.info(f"Multiplying {a} and {b}: {result}")
    return result

def divide(a: float, b: float) -> Optional[float]:
    """Divide the first number by the second.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        Optional[float]: The result of division, or None if division by zero occurs.
    """
    if b == 0:
        logging.warning("Attempted to divide by zero.")
        return None
    result = a / b
    logging.info(f"Dividing {a} by {b}: {result}")
    return result

def main():
    """CLI interface for the calculator application."""
    parser = argparse.ArgumentParser(description="A simple calculator application.")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="The operation to perform.")
    parser.add_argument("a", type=float, help="The first number.")
    parser.add_argument("b", type=float, help="The second number.")

    args = parser.parse_args()

    if args.operation == "add":
        print(f"Result: {add(args.a, args.b)}")
    elif args.operation == "subtract":
        print(f"Result: {subtract(args.a, args.b)}")
    elif args.operation == "multiply":
        print(f"Result: {multiply(args.a, args.b)}")
    elif args.operation == "divide":
        result = divide(args.a, args.b)
        if result is None:
            print("Error: Division by zero.")
        else:
            print(f"Result: {result}")

if __name__ == "__main__":
    main()

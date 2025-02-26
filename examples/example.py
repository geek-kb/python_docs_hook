"""Example module to test documentation generation."""

def hello_world(name: str) -> str:
    """Say hello to someone.

    Args:
        name: The name to greet

    Returns:
        A greeting message
    """
    return f"Hello, {name}!"

def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b

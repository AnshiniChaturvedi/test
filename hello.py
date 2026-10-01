def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}! Welcome to the test repository."


def main():
    names = ["Anshini", "World", "GitHub"]
    for name in names:
        print(greet(name))


if __name__ == "__main__":
    main()

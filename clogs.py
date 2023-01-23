from colorama import init, Fore


def logstatus(level: int, message: str, end: str = '\n'):
    """
    Prints colored text.\n
    Return Example: "[Success] You have been logged in"\n
    Arguments:
        level:   int = The message level (0-4).
        message: str = The message to display.
        end:     str = The end of the message (default: '\\n').
    Level system:
        0 - Success\n
        1 - Info\n
        2 - Warning\n
        3 - Error\n
        4 - Critical Error\n

    """
    init()

    level_colors = {
        0: Fore.LIGHTGREEN_EX,   # Success
        1: Fore.LIGHTYELLOW_EX,  # Info
        2: Fore.YELLOW,          # Warning
        3: Fore.LIGHTRED_EX,     # Error
        4: Fore.RED              # Critical Error
    }

    level_types = {
        0: "SUCCESS",
        1: "INFO",
        2: "WARNING",
        3: "ERROR",
        4: "CRITICAL ERROR"
    }

    if level not in level_colors:
        raise ValueError(f"Invalid level {level}. Level must be between 0-4")

    color = level_colors[level]
    type_ = level_types[level]
    reset = Fore.RESET
    print(f"[{color}{type_}{reset}] {message}{reset}", end=end)

    if level == 4:
        exit(message)


if __name__ == '__main__':
    logstatus(0, "This is an success example")
    logstatus(1, "This is an info example")
    logstatus(2, "This is an warning example")
    logstatus(3, "This is a error example")
    logstatus(4, "This is a critical error example, I automatically exit when I get called!")
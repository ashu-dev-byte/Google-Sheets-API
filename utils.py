from format_terminal import Color


def print_formatted_exception(exception):
    """Prints exceptions in a formatted way"""

    status_code = str(exception).partition("<HttpError ")[2].partition(" when")[0]
    error_message = str(exception).partition('Details: "')[2].partition('">')[0]

    # print(
    #     f"{Color.BOLD}Full Error Message:{Color.END} \n{Color.RED}{exception}{Color.END}\n"
    # )

    print(
        f"{Color.BOLD}Error Message:{Color.END} {Color.RED}{error_message}{Color.END}"
    )
    print(f"{Color.BOLD}Status Code:{Color.END} {Color.RED}{status_code}{Color.END}")


def print_formatted_output(output):
    """Prints output in a formatted way"""

    print(f"{Color.BOLD}{Color.DARKCYAN}Output:{Color.END}\n{output}")

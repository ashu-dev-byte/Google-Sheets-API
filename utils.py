import random
from format_terminal import Color


def print_formatted_exception(exception):
    """Prints exceptions in a formatted way"""

    status_code = str(exception).partition("<HttpError ")[2].partition(" when")[0]
    error_message = str(exception).partition('Details: "')[2].partition('">')[0]

    print(
        f"\n{Color.BOLD}Full Error Message:{Color.END} {Color.RED}{exception}{Color.END}\n"
    )

    print(
        f"{Color.BOLD}Error Message:{Color.END} {Color.RED}{error_message}{Color.END}"
    )
    print(f"{Color.BOLD}Status Code:{Color.END} {Color.RED}{status_code}{Color.END}\n")


def print_formatted_output(value, key="Output"):
    """Prints output in a formatted way"""

    print(f"\n{Color.BOLD}{Color.DARKCYAN}{key}:{Color.END}\n{value}\n")


def print_formatted_info(value):
    """Prints info in a formatted way"""

    print(f"\n{Color.UNDERLINE}{Color.BOLD}{Color.YELLOW}{value}{Color.END}\n")


def get_values_list():
    """Returns a random list of list."""

    student_list = [
        ["Alexandra", "Female", "Senior", "English", "Drama Club"],
        ["Andrew", "Male", "Freshman", "Math", "Lacrosse"],
        ["Becky", "Female", "Sophomore", "Art", "Baseball"],
        ["Carrie", "Female", "Junior", "English", "Track & Field"],
        ["Dorothy", "Female", "Senior", "Math", "Lacrosse"],
        ["Dylan", "Male", "Freshman", "Math", "Baseball"],
        ["Edward", "Male", "Junior", "English", "Drama Club"],
        ["Ellen", "Female", "Freshman", "Physics", "Valorant"],
    ]

    output_list = [
        ["Student Name", "Gender", "Class Level", "Major", "Extracurricular"],
    ]
    for i in range(30):
        value = random.randint(0, 30)
        if value > 15:
            output_list.append(student_list[value % 4])

    return output_list

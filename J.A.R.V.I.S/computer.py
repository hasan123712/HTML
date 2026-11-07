import subprocess
import webbrowser
import os

from pathlib import Path


def open_application(name):

    name = name.lower().strip()

    applications = {

        "notepad": "notepad.exe",

        "calculator": "calc.exe",

        "explorer": "explorer.exe"

    }

    if name in applications:

        subprocess.Popen(
            [applications[name]]
        )

        return "Opening " + name

    elif name in ["chrome", "browser"]:

        webbrowser.open(
            "https://www.google.com"
        )

        return "Opening your default browser."

    elif name == "downloads":

        os.startfile(
            str(Path.home() / "Downloads")
        )

        return "Opening downloads."

    elif name == "documents":

        os.startfile(
            str(Path.home() / "Documents")
        )

        return "Opening documents."

    elif name == "desktop":

        os.startfile(
            str(Path.home() / "Desktop")
        )

        return "Opening desktop."

    else:

        return "I don't recognize that application."


def open_website(url):

    webbrowser.open(url)

    return "Opening website."
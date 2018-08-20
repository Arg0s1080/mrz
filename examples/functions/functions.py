import os
import subprocess
import sys

RED = ("\033[31m", "\033[0m")


def open_image(directory, image):
    answer = input("Would you like to open the image of the computed passport file? [y] / n : ").lower()

    if answer in ("y", "yes") or answer == "":
        try:
            # TODO: Test abspath() on Windows
            image_path = os.path.join(os.pardir, os.pardir, "docs", "images", directory, image)
            print(image_path)

            if sys.platform.startswith('darwin'):
                subprocess.call(('open', image_path))
            elif os.name == 'nt':
                os.startfile(image_path)
            elif os.name == 'posix':
                subprocess.call(('xdg-open', image_path))

        except Exception:
            print("%s- An unexpected error occurred. The file could not be opened%s" % RED)
            for msg in sys.exc_info():
                print("\033[31m!", str(msg))
    elif answer in ("n", "no"):
        exit()
    else:
        print("%sInvalid response%s" % RED)
        open_image(directory, image)


def parent_dir():
    return os.path.dirname(__file__).replace("examples/functions", "")

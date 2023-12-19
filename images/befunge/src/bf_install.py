import sys
from pyb93 import Befunge

def on_output(output):
    sys.stdout.write(output)

if __name__ == "__main__":
    b93 = Befunge()
    b93.on_output = on_output

    with open(sys.argv[0], "r") as file:
        code = file.read()

    b93.run(code)

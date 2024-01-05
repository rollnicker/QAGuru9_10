import os.path

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TEST_DIR = os.path.join(CURRENT_DIR, "tests")
PIC_DIR = os.path.join(TEST_DIR, "pictures")

def path(file_name):
    return os.path.join(PIC_DIR, file_name)
import os
import shutil
import sys


def main(input_dir, target_dir):
    os.makedirs(target_dir, exist_ok=True)
    for fname in os.listdir(input_dir):
        if fname.endswith(".gz"):
            print("Copying {} to {}".format(fname, target_dir))
            shutil.copy2(
                os.path.join(input_dir, fname), os.path.join(target_dir, fname)
            )


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise ValueError("Please specify input and target dirs!")
    main(sys.argv[1], sys.argv[2])

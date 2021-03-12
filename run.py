import os
import shutil

from torchvision.datasets.mnist import MNIST
from torchvision.datasets import utils


def patched_download_url(url, root, filename=None, md5=None, max_redirect_hops=3):
    """Patched version of the
    https://github.com/pytorch/vision/blob/01dfa8ea81972bb74b52dc01e6a1b43b26b62020/torchvision/datasets/utils.py#L97
    """
    root = os.path.expanduser(root)
    if not filename:
        filename = os.path.basename(url)
    fpath = os.path.join(root, filename)

    os.makedirs(root, exist_ok=True)

    # check if file is already present locally
    if utils.check_integrity(fpath, md5):
        print("Using downloaded and verified file: " + fpath)
        return

    shutil.copy2(os.path.join(os.environ["GITHUB_ACTION_PATH"], filename), fpath)

    # check integrity of downloaded file
    if not utils.check_integrity(fpath, md5):
        raise RuntimeError("File not found or corrupted.")


def main():
    # Patch download method
    utils.download_url = patched_download_url
    # Download MNIST
    MNIST(os.environ["INPUT_TARGET_DIR"], download=True)


if __name__ == "__main__":
    main()

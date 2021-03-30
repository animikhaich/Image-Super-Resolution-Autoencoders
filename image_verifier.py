import cv2, os
from glob import glob
from tqdm import tqdm
import argparse


parser = argparse.ArgumentParser(description="COCO Image Verifier")
parser.add_argument(
    "--train_dir",
    type=str,
    required=True,
    help="Enter the Dir Path Containing the Training Images",
)
parser.add_argument(
    "--val_dir",
    type=str,
    required=False,
    default=None,
    help="Enter the Dir Path Containing the Val Images",
)

args = parser.parse_args()


def fix_images(dir_path):
    im_paths = glob(os.path.join(dir_path, "*"))
    for im_path in tqdm(im_paths):
        image = cv2.imread(im_path)
        if image is not None:
            cv2.imwrite(im_path, image)


fix_images(args.train_dir)
if args.val_dir is not None:
    fix_images(args.val_dir)
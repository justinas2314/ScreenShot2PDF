import glob
from PIL import Image


def main(output_path: str, glob_path: str = None, images: [Image] = None, func=lambda x: x):
    """
    Assumptions:
        Either `glob_path` or `images` is not None
        if `images` is specified `len(images) > 0` is true
        if `glob_directory` is specified there are more than 0 images inside
        if `glob_directory` is specified all files in the directory are named
            "data\0.png", "data\2.png", "data\3.png" and so on
        `func` accepts and returns an `Image` object
    """
    if images is None:
        images = [
            Image.open(x) for x in sorted(glob.glob(glob_path),
                                          key=lambda x: int(x.split('\\')[-1].replace('.png', '')))
        ]
    base, *rest = map(func, images)
    base.save(output_path, resolution=100., save_all=True, append_images=rest)


if __name__ == '__main__':
    main(r'data\output.pdf', r'data\images\*.png', func=lambda x: x.crop((0, 0, 1600, 1080)))

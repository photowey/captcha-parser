import base64

import cv2
import numpy as np

import ocr


def base64_to_image(image_base64) -> cv2.typing.MatLike:
    try:
        if 'data:' in image_base64 and ';base64,' in image_base64:
            _, image_base64 = image_base64.split(';base64,')

        image_data = base64.b64decode(image_base64)

        np_arr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        return image

    except Exception as e:
        print(f"Failed: {e}")

    return None


# ----------------------------------------------------------------

def recognize_captcha(image_path: str, debug=False):
    image = cv2.imread(image_path)

    return ocr.recognize_captcha(image, debug)


def recognize_captcha_base64(image_base64: str, debug=False):
    image = base64_to_image(image_base64)

    return ocr.recognize_captcha(image, debug)


# ----------------------------------------------------------------

def parse(image_path, debug=False):
    return recognize_captcha(image_path, debug)


def parse_base64(image_base64: str, debug=False):
    return recognize_captcha_base64(image_base64, debug)

import cv2
import numpy as np
import pytesseract
from PIL import Image

base_alphabeta_table = r'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


# Remove: '1', 'h', 'i', 'l', 'o', 's', 'z', 'O', 'S', ...
# base_alphabeta_table = r'023456789abcdefgjkmnpqrtuvwxyABCDEFGHIJKLMNPQRTUVWXYZ'


def preprocess_image(image: cv2.typing.MatLike, debug=False):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if debug:
        cv2.imshow("Step 1: Gray Image", gray_image)
        cv2.waitKey(0)

    adaptive_binary_img = cv2.adaptiveThreshold(
        gray_image,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV,
        15, 2
    )
    if debug:
        cv2.imshow("Step 2: Adaptive Binary Image", adaptive_binary_img)
        cv2.waitKey(0)

    denoised_image = cv2.medianBlur(adaptive_binary_img, 3)
    if debug:
        cv2.imshow("Step 3: Denoised Image", denoised_image)
        cv2.waitKey(0)

    kernel = np.ones((2, 2), np.uint8)
    eroded_image = cv2.erode(denoised_image, kernel, iterations=1)
    if debug:
        cv2.imshow("Step 4: Eroded Image", eroded_image)
        cv2.waitKey(0)

    dilated_image = cv2.dilate(eroded_image, kernel, iterations=1)
    if debug:
        cv2.imshow("Step 5: Dilated Image", dilated_image)
        cv2.waitKey(0)

    return dilated_image


def post_process_recognition(text):
    text = text.strip()
    # ...

    return text


def recognize_captcha(image: cv2.typing.MatLike, debug=False):
    processed_image = preprocess_image(image, debug)

    pil_image = Image.fromarray(processed_image)

    custom_config = r'--psm 6 --oem 3 -c tessedit_char_whitelist={}'.format(base_alphabeta_table)

    text = pytesseract.image_to_string(pil_image, config=custom_config)
    captcha_text = ''.join(char for char in text if char.isalnum())[:4]

    # If necessary
    captcha_text = post_process_recognition(captcha_text)

    return captcha_text

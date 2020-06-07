from argparse import ArgumentParser
import os
import cv2
import pytesseract
from PIL import Image
from langdetect import detect
from gtts import gTTS
from playsound import playsound

if __name__ == "__main__":

    # Argument Parser
    ap = ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to input image to be OCR'd")
    ap.add_argument("-p", "--processing", type=str, default='thresh',
                    help="type of pre-processing to be done(thresh, blur)")

    ap.add_argument("-f", "--format", type=str, default='speak',
                    help="Format for the output(speak)")
    args = vars(ap.parse_args())

    print('Program Running With PID: %s' % os.getpid())

    # Read the Image
    image = cv2.imread(args['image'])

    # Convert image to grayscale image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Process the Image for better output
    if args['processing'] == 'thresh':
        gray_image = cv2.threshold(gray_image, 0, 255,
                                   cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif args['processing'] == 'blur':
        gray_image = cv2.medianBlur(gray_image, 3)

    # Temporary store the image to temp folder

    filename = "temp" + os.path.sep + "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray_image)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    if args['format'] == 'speak':
        # get text from Image
        text = pytesseract.image_to_string(Image.open(filename))
        # remove temp file
        os.remove(filename)

        print("Captured text from Image : %s" % text)

        # store the text to the .txt file in output folder

        text_filepath = "output" + os.path.sep + "{}.txt".format(os.getpid())
        with open(file=text_filepath, mode='w+') as file:
            file.write(text)

        lang = detect(text)
        print("Language: %s" % lang)
        audio = gTTS(text=text, lang=lang, slow=False)
        audio_filepath = "output" + os.path.sep + "{}.mp3".format(os.getpid())
        audio.save(audio_filepath)
        print('Audio file is saved to the path %s' % audio_filepath)
        filename = "output" + os.path.sep + "{}.png".format(os.getpid())
        print('After Processed Image path %s' % audio_filepath)
        cv2.imwrite(filename, gray_image)
        print('Playing Audio...')
        playsound(audio_filepath)

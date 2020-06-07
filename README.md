# PyIm2Speak
Read image and speek the text content using PIL, langdetect, tesseract, gtts and playsound with Python <br/><br/>
[![paypal](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/sameernarkhede/250)

# Before you start
You must have to install [tesseract-ocr](https://github.com/tesseract-ocr/tesseract) on your local pc

## Parameters
- -i --image   - path to input image to be OCR
- -p --processing - For type of pre-processing to be done(thresh, blur)
- -f --format  - Format for the output(speak)

## Coding

Read the Image

    image = cv2.imread(args['image'])
    
Convert image to grayscale image

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
Process the Image for threshold and blur according to user's choice
For Threshold

    gray_image = cv2.threshold(gray_image, 0, 255,
                    cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
                    
For Blurr

    gray_image = cv2.medianBlur(gray_image, 3)
    
Store the image into temp folder with name as process_id of progrma

    filename = "temp" + os.path.sep + "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray_image)

set path for tesseract

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
get text from image
    
    text = pytesseract.image_to_string(Image.open(filename))
 
remove temp file

    os.remove(filename)

Store the processed image into output folder
    
    text_filepath = "output" + os.path.sep + "{}.txt".format(os.getpid())
    with open(file=text_filepath, mode='w+') as file:
        file.write(text)    
        
Detect the language accourding to the text
    
    lang = detect(text)
    print("Language: %s" % lang)
    
Convert Text to Audio using gtts
    
    audio = gTTS(text=text, lang=lang, slow=False)

Store the audio file to output folder

    audio_filepath = "output" + os.path.sep + "{}.mp3".format(os.getpid())
    audio.save(audio_filepath)
    
write Grayimage to output folder

    cv2.imwrite(filename, gray_image)
    
Play the converted audio

    playsound(audio_filepath)
    
# Author
Sameer Narkhede <br/>
Profile : https://github.com/narkhedesam <br/>
Website : https://narkhedesam.github.io/ 

## Donation

If this project help you reduce time to develop, you can give me a cup of coffee :relaxed: 
<br/>

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/sameernarkhede/250)

from PIL import Image
import easyocr
import tempfile

reader=easyocr.Reader(['en'], gpu=False)

def extract_text_from_image(image_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        img=Image.open(image_file)
        img.save(tmp.name)
        result=reader.readtext(tmp.name, detail=0)
    return " ".join(result)
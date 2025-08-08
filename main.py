from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import io

from escpos.printer import Usb

app = FastAPI()

p = Usb(0x04b8, 0x0e28, profile="TM-T20II")

@app.post("/print-image")
async def print_image(file: UploadFile = File(...)):
    try:
        # Read the image file
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))

        # Open the printer connection
        p.open()

        # Print the image
        p.image(image, center=True)

        # Cut the paper
        p.cut()

        # Close the printer connection
        p.close()

        return JSONResponse(content={"message": "Printed successfully!"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


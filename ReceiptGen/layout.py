{\rtf1\ansi\ansicpg1250\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from PIL import Image, ImageDraw, ImageFont\
import os\
\
def generate_receipt_image(product_name, product_price, delivery_address, brand_name):\
    # \uc0\u321 adowanie odpowiedniego szablonu\
    template_path = f'./templates/\{brand_name.lower()\}_template.png'\
    if not os.path.exists(template_path):\
        raise ValueError(f"Brak szablonu dla marki \{brand_name\}")\
\
    image = Image.open(template_path)\
    draw = ImageDraw.Draw(image)\
    \
    # Ustawienie czcionki\
    font = ImageFont.load_default()\
\
    # Rysowanie tekst\'f3w na obrazie\
    draw.text((10, 10), f"Produkt: \{product_name\}", font=font, fill="black")\
    draw.text((10, 40), f"Cena: \{product_price\}", font=font, fill="black")\
    draw.text((10, 70), f"Adres: \{delivery_address\}", font=font, fill="black")\
\
    # Zapisz obrazek\
    output_path = f'./generated_receipts/\{brand_name.lower()\}_receipt.png'\
    image.save(output_path)\
    \
    return output_path\
}
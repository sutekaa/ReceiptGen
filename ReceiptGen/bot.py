{\rtf1\ansi\ansicpg1250\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import discord\
from discord.ext import commands\
from discord.ui import Modal, TextInput\
import smtplib\
from email.mime.text import MIMEText\
from email.mime.multipart import MIMEMultipart\
import os\
from layout_generator import generate_receipt_image\
\
intents = discord.Intents.default()\
bot = commands.Bot(command_prefix='/', intents=intents)\
\
# Wczytywanie zmiennych z .env\
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')\
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')\
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')\
\
@bot.event\
async def on_ready():\
    print(f'Bot \{bot.user\} is ready.')\
\
@bot.command()\
async def receipt(ctx):\
    modal = ReceiptModal()\
    await ctx.send_modal(modal)\
\
class ReceiptModal(Modal):\
    def __init__(self):\
        super().__init__(title="Wygeneruj paragon")\
\
        # Wprowadzenie danych\
        self.product_name = TextInput(label="Nazwa produktu", placeholder="Np. Apple iPhone 14")\
        self.product_price = TextInput(label="Cena produktu", placeholder="Np. 1000 PLN")\
        self.delivery_address = TextInput(label="Adres dostawy", placeholder="Np. Warszawa, ul. X")\
        self.email_address = TextInput(label="Adres e-mail (gdzie wy\uc0\u347 lemy paragon)", placeholder="Tw\'f3j e-mail")\
        self.brand_choice = TextInput(label="Wybierz mark\uc0\u281  (np. Apple, Nike, Gucci)", placeholder="Np. Apple")\
        \
        self.add_item(self.product_name)\
        self.add_item(self.product_price)\
        self.add_item(self.delivery_address)\
        self.add_item(self.email_address)\
        self.add_item(self.brand_choice)\
\
    async def on_submit(self, interaction: discord.Interaction):\
        # Generowanie paragonu\
        image_path = generate_receipt_image(self.product_name.value, self.product_price.value, self.delivery_address.value, self.brand_choice.value)\
        \
        # Wysy\uc0\u322 anie e-maila\
        send_receipt_email(self.email_address.value, image_path)\
\
        # Odpowied\uc0\u378  po wykonaniu\
        await interaction.response.send_message(f"Paragon zosta\uc0\u322  wys\u322 any na e-mail: \{self.email_address.value\}")\
\
def send_receipt_email(recipient_email, image_path):\
    msg = MIMEMultipart()\
    msg['From'] = EMAIL_ADDRESS\
    msg['To'] = recipient_email\
    msg['Subject'] = 'Tw\'f3j paragon zakupu'\
\
    body = 'Za\uc0\u322 \u261 czam paragon w formie PDF.'\
    msg.attach(MIMEText(body, 'plain'))\
\
    with open(image_path, 'rb') as attachment:\
        part = MIMEApplication(attachment.read(), _subtype='octet-stream')\
        part.add_header('Content-Disposition', 'attachment', filename=image_path)\
        msg.attach(part)\
\
    # U\uc0\u380 yj SMTP Gmaila\
    with smtplib.SMTP('smtp.gmail.com', 587) as server:\
        server.starttls()\
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)\
        text = msg.as_string()\
        server.sendmail(EMAIL_ADDRESS, recipient_email, text)\
\
bot.run(DISCORD_TOKEN)\
}
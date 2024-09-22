# pip install pyTelegramBotAPI requests
# pip install openai

import telebot
import requests
from PIL import Image
import io
import openai


bot_token = 'enter the token' #my token is hidden for security purpose
bot = telebot.TeleBot(bot_token)

openai.api_key = 'enter api_key' #my key is hidden for security purpose

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Retrieve the message text
    text = message.text

    # Use the DALL·E API to generate an image based on the text
    response = openai.Image.create(prompt=text, n=1, size="1024x1024")
    image_url = response['data'][0]['url']

    # Download the image
    image_data = requests.get(image_url).content
    image = Image.open(io.BytesIO(image_data))

    # Convert the image to bytes
    image_byte_array = io.BytesIO()
    image.save(image_byte_array, format='PNG')
    image_byte_array.seek(0)

    # Send the image as a reply
    bot.send_photo(message.chat.id, image_byte_array)
bot.polling()

import subprocess
import sys
import  telegram 
bot = telegram.Bot(token='529449700:AAG6dcqs0NaI2Od1pefXfpJEFG1eoEbBzqM')
bot.deleteWebhook()
p=subprocess.Popen(r'ngrok.exe http -bind-tls=true 5000')



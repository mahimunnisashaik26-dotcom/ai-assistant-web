import datetime

def process_command(text):
    text = text.lower()

    if "hello" in text or "hlo" in text:
        return "Hello! How can I help you?"

    elif "open youtube" in text:
        return "Click here to open YouTube: https://youtube.com"

    elif "open google" in text:
        return "Click here to open Google: https://google.com"

    elif "open whatsapp" in text:
        return "Click here to open WhatsApp: https://web.whatsapp.com"

    elif "time" in text:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"The time is {now}"

    else:
        return "Sorry, I didn't understand that."

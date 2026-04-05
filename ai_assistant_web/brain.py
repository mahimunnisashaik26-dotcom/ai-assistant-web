import webbrowser
import datetime

def process_command(text):
    text = text.lower()

    if "hello" in text or "hlo" in text:
        return "Hello! How can I help you?"

    elif "open youtube" in text:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open google" in text:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open whatsapp" in text:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp"

    elif "time" in text:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"The time is {now}"

    else:
        return "Sorry, I didn't understand that."
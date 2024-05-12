import pywhatkit


def send_msg(message):
    # Send message through WhatsApp
    phone_number = "+917489118248"  # Replace with librarian's phone number

    try:
        pywhatkit.sendwhatmsg(phone_number, message, 0, 0)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Failed to send message: {str(e)}")

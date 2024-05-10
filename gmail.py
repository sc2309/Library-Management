import pywhatkit


def send_gmail(bname,name,phone):
    # Send message
    phone_number = "+919479396605"  # Replace with recipient's phone number
    message = f'book {bname} was ordered by {name}, phone no.{phone}, operation : issue'

    try:
        pywhatkit.sendwhatmsg(phone_number, message, 0, 0)  # Send immediately
        print("Message sent successfully!")
    except Exception as e:
        print(f"Failed to send message: {str(e)}")

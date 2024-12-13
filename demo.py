import pywhatkit as kit

# Function to send a WhatsApp message
def send_whatsapp_message(phone_number, message, hour, minute):
   
    try:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        print("Message scheduled successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def whatsapp(phone_number,message,hour,minute):
    """"
    sends a whatsapp message to a specific number 
    """

# Example usage
if __name__ == "__main__":
    phone = "+919337577933"  # Replace with the recipient's phone number
    msg = "Hello! Good morning"
    send_hour = 10  # Replace with the hour (24-hour format)
    send_minute = 41  # Replace with the minute

    send_whatsapp_message(phone, msg, send_hour, send_minute)


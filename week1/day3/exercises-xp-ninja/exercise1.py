class Phone():
    def __init__(self,phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages =[]
    
    def call(self,other_phone):
        message = f"{self.phone_number} called {other_phone}"
        print(message)
        self.call_history.append(message)

    def show_call_history(self):
        print("Call History:")
        for call in self.call_history:
            print(call)
    
    def send_message(self,other_phone,message):
            my_messages = []
            my_dict = {
                "to": other_phone,
                "from": self.phone_number,
                "message": message
            }
            my_messages.append(my_dict)
            
    def show_outgoing_messages(self):
        print("Outgoing Messages:")
        for message in self.messages:
            if(message["from"] == self.phone_number):
                print(f"To: {message['to']}, From: {message['from']}, Message: {message['message']}")
    def show_incoming_messages(self):
        print("Incoming Messages:")
        for message in self.messages:
            if(message["to"] == self.phone_number):
                print(f"To: {message['to']}, From: {message['from']}, Message: {message['message']}")
                
                
    def show_messages_from(self,other_phone):
        print(f"Messages from {other_phone}:")
        for message in self.messages:
            if(message["from"] == other_phone):
                print(f"To: {message['to']}, From: {message['from']}, Message: {message['message']}")
                
#code testing
print("=== Testing Phone Class ===")

# Create two phones
phone1 = Phone("6034543543")
phone2 = Phone("6034543544")

# Test call functionality
print("\nTesting call functionality:")
phone1.call(phone2.phone_number)
phone2.call(phone1.phone_number)

# Test call history
print("\nTesting call history:")
phone1.show_call_history()
phone2.show_call_history()

# Test messaging functionality
print("\nTesting messaging:")
phone1.send_message(phone2.phone_number, "Hello there!")
phone2.send_message(phone1.phone_number, "Hi! How are you?")
phone1.send_message(phone2.phone_number, "I'm good, thanks!")

# Test message display (Note: There's a bug in the original code - messages aren't being stored)
print("\nTesting outgoing messages:")
phone1.show_outgoing_messages()
phone2.show_outgoing_messages()

print("\nTesting incoming messages:")
phone1.show_incoming_messages()
phone2.show_incoming_messages()

print("\nTesting messages from specific number:")
phone1.show_messages_from("0603454354")
phone2.show_messages_from("0603454353")

print("\n=== Test Complete ===")
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Split the email addresses using both comma and space as delimiters
        split_addresses = re.split('[,\s]+', self.email_addresses)
        
        # Define a regex pattern for valid email addresses
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Filter and clean valid email addresses
        valid_addresses = [
            addr.strip() for addr in split_addresses
            if addr.strip() and re.match(email_pattern, addr.strip())
        ]
        
        # Get unique addresses and sort them alphabetically
        unique_addresses = sorted(set(valid_addresses))
        
        return unique_addresses
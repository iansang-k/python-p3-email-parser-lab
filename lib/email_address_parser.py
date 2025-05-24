# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Split on commas, spaces, or combinations of both
        addresses = re.split(r'[,\s]+', self.email_addresses)
        
        # Filter out empty strings and clean up any whitespace
        cleaned_addresses = [addr.strip() for addr in addresses if addr.strip()]
        
        # Get unique addresses and sort alphabetically
        unique_sorted = sorted(set(cleaned_addresses))
        
        return unique_sorted
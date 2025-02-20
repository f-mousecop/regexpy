import re

# Week 7 Lab - Python RegEx
# Use regex to create a specification for a valid email address
'''
    Criteria:
        1. Acceptable chars are alphanumeric (e.g., a-zA-Z, 0-9) and special chars (-, ., _)
        2. Must contain an '@' char 
        3. Prefix appears to the left of the @ symbol
        4. Domain appears to the right of the @ symbol
            1. E.g., john@test.com (.net/.org/etc.)
'''

def validate_email(email):
    specifications = re.compile(
        r"""
        ^[a-zA-Z0-9]                       # Prefix
        [^._-]*([._-][^._-]+){0,3}         # . _ - can only appear 3 times as non-leading/trailing chars
        @                                  # @ symbol
        [a-zA-Z0-9]                        # Domain name (e.g., company)
        [^._-]*([._-][^._-]+){0,1}         # . _ - can only appear 1 as non-leading/trailing chars
        \.(com|org|co|net|info|xyz|online|app|us|uk|edu|gov|mil)$    # Domain e.g., .com, .org, .net, etc.
        """,
        re.VERBOSE
    )
    
    if specifications.search(email):
        return (f'Email is valid: {email}')
    else:
        return (f'Email is not valid: {email}')


valid_emails = [
    "john.doe@test-test.com",
    "jane-fletcher.wesley@test.co",
    "a.b-c@example.gov",
    "x-y.z@example-suffix.edu",
    "james.sergeant@army.mil",
    "first.last@company.info"
]

invalid_emails = [
    "user...name@test.com",   
    "name--.-@test.org",      
    "john.doe@example",        
    "-start@test.com",        
    "end.@test.com",          
    "jane---fletcher@test.com",
    "test@test.o",
    "first$#last@company"
]

print("Test cases for validating emails with RegEx\n")
print("Valid emails:")
print("-------------------------------------")
for email in valid_emails:
    print(validate_email(email))

print('-------------------------------------\n\n')
print('Invalid emails:')
print('-------------------------------------')
for email in invalid_emails:
    print(validate_email(email))
print('-------------------------------------')
from django.core.exceptions import ValidationError
import string

class InputValidator:
    def __init__(self, min_special_characters=1):
        self.min_special_characters = min_special_characters
        self.special_characters = set(string.punctuation)

    def validate(self, password, user=None):
        self.validate_special_characters(password)
        self.validate_uppercase_first_letter(password)

    def validate_special_characters(self, password):
        special_character_count = sum(1 for char in password if char in self.special_characters)
        if special_character_count < self.min_special_characters:
            message = f'The password should at least has {self.min_special_characters} special character(s).'
            raise ValidationError(message)
    
    def validate_uppercase_first_letter(self, password):
        if not password[0].isupper():
            raise ValidationError('The first letter of the password should be an uppercase letter.')
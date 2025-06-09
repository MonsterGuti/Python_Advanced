class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


MIN_PASSWORD_LENGTH = 8
SPECIAL_CHARS = ["@", "*", "&", "%"]


def is_too_common(my_password):
    return (
        my_password.isdigit() or
        my_password.isalpha() or
        all(char in SPECIAL_CHARS for char in my_password)
    )


def has_special_char(my_password):
    return any(char in SPECIAL_CHARS for char in my_password)


while True:
    password = input()
    if password == "Done":
        break

    if len(password) < MIN_PASSWORD_LENGTH:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if is_too_common(password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not has_special_char(password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")

def is_palindrome(text):
    # Створюємо список лише з букв та цифр, переведених у нижній регістр
    cleaned_text = [char.lower() for char in text if char.isalnum()]

    # Порівнюємо список з його реверсом
    return cleaned_text == cleaned_text[::-1]
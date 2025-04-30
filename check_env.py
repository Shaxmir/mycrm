with open(".env", "rb") as f:
    content = f.read()
    print("Сырые байты:", content)
    print("UTF-8 декодировка:")
    try:
        decoded = content.decode("utf-8")
        print(decoded)
    except UnicodeDecodeError as e:
        print("Ошибка декодировки:", e)

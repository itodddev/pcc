first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
message = f"Hello, {full_name.title()}!"
print(message)

print("Language:\n\tPython\n\tC\n\tJavescript\n\n")

favorite_language = 'python '
stripped = favorite_language.rstrip() # lstrip() - left side, strip() - both sides
print(stripped)

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://')) # removes the https://
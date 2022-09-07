### Random Password Generator ###
import secrets
len=int(input("Enter Password Length:"))
print(secrets.token_urlsafe(len))
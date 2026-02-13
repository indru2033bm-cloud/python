def http_status(status):
    match status:
        case 200:
            return "OK"
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
a = int(input("Enter a status code: "))
print(http_status(200))
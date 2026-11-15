def sum_str(a: str, b: str) -> str:
    if a == "": # happy coding !
         a = "0"   
    if b == "":
        b = "0"
    result = int(a) + int(b)
    return str(result)
def line_up(name: str, number: int):

    str_num = str(number)
    if str_num[-1] not in ("1", "2", "3") or str_num[-2:] in ("11", "12", "13"):
        ordinal = str_num + "th"
    
    elif str_num[-1] == "1":
        ordinal = str_num + "st"
    elif str_num[-1] == "2":
        ordinal = str_num + "nd"
    else:
        ordinal = str_num + "rd"
    
    return f"{name}, you are the {ordinal} customer we serve today. Thank you!"

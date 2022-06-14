import datetime
import re

def personal_number_to_date(personal_number):
    match = re.match(
        r"(\d{2})?(\d{2})(\d{2})(\d{2})([-+])?\d{4}",
        personal_number,
    )
    if not match:
        raise ValueError(f"{personal_number} is not a valid personal number")
    century, decade, month, day, separator = match.groups()
    if not century:
        current_year = datetime.date.today().year
        if not separator == "+" and current_year % 100 - int(decade) > 0:
            century = "20" 
        else:
            century = "19"
    year = int(century + decade)
    return datetime.date(*[int(x) for x in (year, month, day)])


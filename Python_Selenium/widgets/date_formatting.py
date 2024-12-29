from datetime import datetime

""" datetime.strptime(date, "%d/%m/%Y"):

1) strptime is used to parse the input string into a datetime object.
Format "%d/%m/%Y" matches the input string:
%d: Day (e.g., 12).
%m: Month (e.g., 6 for June).
%Y: Year (e.g., 1997).

2) strftime("%d %B %Y"):
Formats the datetime object into the desired string:
%d: Day of the month (e.g., 12).
%B: Full month name (e.g., June).
%Y: Year (e.g., 1997).

 """
date = "12/6/1997"
# Parse the date string into a datetime object
date_object = datetime.strptime(date, "%d/%m/%Y")
# Format the datetime object into the desired format
formatted_date = date_object.strftime("%d %B %Y")
#print(formatted_date)

def convert_date_to_new_format(input_date, input_format, output_format):
    try:
        # Parse the input date
        date_object = datetime.strptime(input_date, input_format)
        # Convert to desired format
        return date_object.strftime(output_format)
    except ValueError as e:
        return f"Error: {e}"

input_date = "12-28-24"
#print(convert_date_to_new_format(input_date, "%m-%d-%y", "%d %B %y"))  # Output: "28-12-24"

def parse_date_to_know_format(date_str):
    formats = ["%d %B %Y","%d %m %Y", "%Y %B %d", "%d/%m/%Y", "%m-%d-%Y","%m-%d-%y", "%Y %m %d", "%d %B %Y"]
    for format in formats:
        try:
            datetime.strptime(date_str,format)
            return format
        except ValueError:
            continue
    raise ValueError(f"Date Format not recognized for : {date_str}")
        
#print(parse_date_to_know_format(input_date))
    
def format_user_date(user_date):
    """ verify the user enter date format and then convert it to new format"""
    date_format=parse_date_to_know_format(user_date)
    updated_user_date=convert_date_to_new_format(user_date, date_format, "%Y %B %d")
    #print(updated_user_date)
    current_date=datetime.now()
    updated_current_date=current_date.strftime("%Y %B %d")
    """Verify user enter date is previous or future as compare to present date and return updated_user_date"""
    if updated_current_date == updated_user_date :
        return None,updated_user_date
    is_future_date = updated_current_date < updated_user_date
    return is_future_date, updated_user_date
    


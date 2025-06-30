from datetime import datetime

# get current date and time
datetime_object = datetime.now()
print(datetime_object)
print('Type :- ', type(datetime_object))

def convert_to_inches(feet, inches):
    """Converts feet and inches to total inches"""
    total_inches = feet * 12 + inches
    return total_inches

# Example usage:
feet = 5
inches = 8
total = convert_to_inches(feet, inches)
print(f"{feet} feet and {inches} inches = {total} total inches")

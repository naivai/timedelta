from datetime import datetime, timedelta

now = datetime.now()
print("Current time:", now)

# Subtract 60 seconds
minus_60_seconds = now - timedelta(seconds=60)
print("Minus 60 seconds:", minus_60_seconds)

# Add 2 years — approximate by adding 2 * 365 days (not perfect for leap years)
plus_2_years = now + timedelta(days=2*365)
print("Plus 2 years (approx):", plus_2_years)

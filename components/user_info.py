from datetime import datetime
import geocoder

def get_user_info():
    # Replace these with real data fetching
    current_time = datetime.now().strftime("%H:%M:%S")
    location = geocoder.ip('me').latlng  # Requires 'geocoder' library
    return current_time, location

import requests
import csv
from datetime import datetime

# Read data from CSV file


def read_data(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date_obj = datetime.strptime(row['attendance_date'], '%Y-%m-%d')
            formatted_date = date_obj.strftime('%A, %d %B %Y')

            first_name = row['full_name'].split()[0].strip()
            extracted_data = {
                'name': first_name,
                'attendance_date': formatted_date,
                'phone_number': row['phone_number']
            }
            data.append(extracted_data)
    return data

# Make POST request


def make_post_request(name, phone_number, attendance_date):

    msg = f"Hi {name},\n\nCongratulations on registering for the TDP 23 youth camp! Get ready for a faith-filled journey of spiritual growth, fellowship, and uplifting experiences. We can't wait to see you at the camp and witness God's work in your life. \nJust as you indicated, see you on {attendance_date}!\nYOUTH ALIVE! WORK IS DONE!!"
    data = {
        'recipient[]': [phone_number],
        'sender': 'BRIM YOUTH',
        'message': msg,
        'is_schedule': False,
        'schedule_date': ''
    }
    # response = requests.get(
    #     'https://api.mnotify.com/api/balance/sms?key=EoM1D59N9Yci01HRQgREGYLov', headers=headers)
    response = requests.post(
        'https://api.mnotify.com/api/sms/quick?key=EoM1D59N9Yci01HRQgREGYLov', data)
    return response

# Main script


def main():
    # file_path = input("Enter file path: ")
    # url = input("Enter the POST request URL: ")

    try:
        data = read_data('test.csv')
        # data = read_data(file_path)
    except Exception as e:
        print("Error reading file:", str(e))
        return

    for payload in data:
        name = payload['name']
        phone_number = payload['phone_number']
        attendance_date = payload['attendance_date']
        print(name, phone_number, attendance_date)

        response = make_post_request(name, phone_number, attendance_date)
        print("Response:", response.text)


if __name__ == "__main__":
    main()

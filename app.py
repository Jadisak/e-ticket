import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pyqrcode

# Connect to Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Your Google Sheets Document').sheet1

# Generate QR Code
def generate_qr_code(url):
    qr = pyqrcode.create(url)
    qr.png('registration_link.png', scale=8)

# Streamlit App
def main():
    st.title('Registration App')

    # Display QR Code for registration link
    registration_link = 'https://your-google-form-url'
    generate_qr_code(registration_link)
    st.image('registration_link.png', caption='Scan QR Code to Register', use_column_width=True)

    # Registration Form
    st.subheader('Registration Form')
    name = st.text_input('Name')
    email = st.text_input('Email')

    if st.button('Register'):
        sheet.append_row([name, email])
        st.success('Registration Successful!')

if __name__ == '__main__':
    main()

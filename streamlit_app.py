import os, streamlit as st
from resend import Resend
import resend

# Provide the Resend API key
#client = Resend(api_key=os.environ[""])

resend.api_key = 're_jFPy5iSs_4uBTFPcoHF4XwfBriUNyZyy9' #os.environ["RESEND_API_KEY"]
email_from = st.text_input("From:", "")
#email_to = st.text_input("To:", "")
email_subject = st.text_input("Subject:", "")
email_body = st.text_input("Body:", "")
params = {
    "from": email_from,
    "to": "aulakh1@gmail.com",
    "subject": email_subject,
    "html": "<strong>it works!</strong>"
}



# Set up the Streamlit app
st.subheader("Send Email")


# Send email using Resend
if st.button("Submit"):
    if not email_from or not email_subject or not email_body:
        st.error('Please provide the missing fields.')
    else:
        with st.spinner():
            #client.send_email(to=email_to, subject=email_subject, text=email_body)
            email = resend.Emails.send(params)
            st.success(f"Email sent!")

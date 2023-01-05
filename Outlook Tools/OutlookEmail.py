# https://learndataanalysis.org/source-code-how-to-send-an-outlook-email-with-attachments-using-python-using-pywin32/
# Imports

import win32com.client as win32

# Set up
olApp = win32.Dispatch('Outlook.Application')
olNS = olApp.GetNameSpace('MAPI')

mailitem  = olApp.CreateItem(0)

# Information for email

mailitem.Subject = 'Hello 123'
mailitem.BodyFormat = 'Hello 123'
mailitem.Body = 1
mailitem.To = 'waht@domain.comm'

#Select an account
#mailitem._oleobj_.Invoke(*(64209,0,9,0, olNS.Accounts.item('test1@test.com')))

#Display the email
mailitem.display

#Save email to Draft
#mailitem.save

#Send email
#mailitem.send
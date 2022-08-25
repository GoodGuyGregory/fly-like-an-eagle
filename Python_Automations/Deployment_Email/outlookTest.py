import win32com.client as win32

outlookApplication = win32.Dispatch('outlook.application')

message = outlookApplication.CreateItem(0)

message.To = ''
message.Subject = 'Test Email from Python'
message.Body = "This is the body of the message"

message.Send()

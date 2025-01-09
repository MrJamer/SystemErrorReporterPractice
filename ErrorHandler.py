import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Обробка помилок та критичних ситуацій

class ErrorHandler:
    def __init__(self, logger, email_settings):
        self.logger = logger
        self.email_settings = email_settings

    def handle_error(self, error_message):
        self.logger.log_error(error_message)
        self.send_error_email(error_message)

    def send_error_email(self, message):
        try:
            server = smtplib.SMTP(self.email_settings["smtp_server"], self.email_settings["smtp_port"])
            server.starttls()
            server.login(self.email_settings["email"], self.email_settings["password"])

            msg = MIMEMultipart()
            msg["From"] = self.email_settings["email"]
            msg["To"] = self.email_settings["recipient_email"]
            msg["Subject"] = "Critical Error Alert"
            msg.attach(MIMEText(message, "plain"))

            server.sendmail(self.email_settings["email"], self.email_settings["recipient_email"], msg.as_string())
            server.quit()
            self.logger.log_info(f"Error email sent to {self.email_settings['recipient_email']}")
        except Exception as e:
            self.logger.log_fatal(f"Failed to send error email: {str(e)}")

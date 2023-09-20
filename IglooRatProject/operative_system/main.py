'''
import shutil

def create_backup(folder_path, backup_path):
    try:
        # Create a copy of the specified folder
        shutil.copytree(folder_path, backup_path)
        print(f"Backup created successfully at {backup_path}!")
    except Exception as e:
        print(f"Error creating backup: {e}")

def main():
    # Specify the folder you want to backup
    folder_path = "C:/Users/Gonza/Desktop/recibos"
    # Specify the backup location
    backup_path = "C:/Users/Gonza/Desktop/security_copy"

    # Create the backup
    create_backup(folder_path, backup_path)

if __name__ == "__main__":
    main()
'''

'''
# Import necessary libraries
import shutil  # Library for file operations
import os      # Library for interacting with the operating system
import zipfile # Library for working with ZIP files
import schedule # Library for task scheduling
import time    # Library for time-related operations

def create_backup(folder_path, backup_path):
    try:
        # Create a copy of the specified folder
        backup_folder = f"{backup_path}/{time.strftime('%Y-%m-%d')}"
        shutil.copytree(folder_path, backup_folder)

        # Compress the files into a ZIP archive
        with zipfile.ZipFile(f"{backup_folder}.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(backup_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, backup_folder))

        print(f"Backup created successfully at {backup_folder}.zip")
    except Exception as e:
        print(f"Error creating backup: {e}")

def main():
    # Specify the folder you want to backup
    folder_path = "C:/Users/Gonza/Desktop/recibos"
    # Specify the backup location
    backup_path = "C:/Users/Gonza/Desktop/security_copy"

    # Create the backup
    create_backup(folder_path, backup_path)

def schedule_backup():
    # Schedule the backup to run every Friday at 11:15 AM
    schedule.every().friday.at('11:15').do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_backup()
'''

'''
# Import necessary libraries
import shutil   # Library for file operations
import os       # Library for interacting with the operating system
import zipfile  # Library for working with ZIP files
import schedule # Library for task scheduling
import time     # Library for time-related operations

# Function to create a backup
def create_backup(folder_path, backup_path):
    try:
        # Create a copy of the specified folder
        backup_folder = f"{backup_path}/{time.strftime('%Y-%m-%d')}"
        shutil.copytree(folder_path, backup_folder)

        # Compress the files into a ZIP archive
        with zipfile.ZipFile(f"{backup_folder}.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(backup_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, backup_folder))

        # Print a success message
        print(f"Backup created successfully at {backup_folder}.zip")
    except Exception as e:
        # Print an error message and exit the loop if there's an error
        print(f"Error creating backup: {e}")
        raise SystemExit

# Main function
def main():
    # Specify the folder you want to backup
    folder_path = "C:/Users/Gonza/Desktop/recibos"
    # Specify the backup location
    backup_path = "C:/Users/Gonza/Desktop/security_copy"

    # Create the backup
    create_backup(folder_path, backup_path)
    
    # Delete the files within the original folder (folder_path)
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)

# Function to schedule the backup
def schedule_backup():
    # Schedule the backup to run every Friday at 11:56 AM (adjust the time as needed)
    schedule.every().friday.at('11:56').do(main)

    try:

        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print(f"Error in scheduled backup : {e}")
        # Exit the loop if an error occurs during scheduled task execution
        return
    
# Entry point of the program
if __name__ == "__main__":
    schedule_backup()  # Start scheduling the backup
'''

# Import necessary libraries
import shutil   # Library for file operations
import os       # Library for interacting with the operating system
import zipfile  # Library for working with ZIP files
import schedule # Library for task scheduling
import time     # Library for time-related operations
import smtplib  # Library for SMTP email sending
from email.mime.text import MIMEText # Import MIMEText class for email formatting
from email.mime.multipart import MIMEMultipart # Import MIMEMultipart class for email composition

# Function to create a backup
def create_backup(folder_path, backup_path):
    try:
        # Create a copy of the specified folder
        backup_folder = f"{backup_path}/{time.strftime('%Y-%m-%d')}"
        shutil.copytree(folder_path, backup_folder)

        # Compress the files into a ZIP archive
        with zipfile.ZipFile(f"{backup_folder}.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(backup_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, backup_folder))

        # Print a success message
        print(f"Backup created successfully at {backup_folder}.zip")
        # Send email notification
        send_email_notification(f"Backup created successfully at {backup_folder}.zip")
    except Exception as e:
        # Print an error message and exit the loop if there's an error
        print(f"Error creating backup: {e}")
        raise SystemExit

# Main function
def main():
    # Specify the folder you want to backup
    folder_path = "C:/Users/Gonza/Desktop/recibos"
    # Specify the backup location
    backup_path = "C:/Users/Gonza/Desktop/security_copy"

    # Create the backup
    create_backup(folder_path, backup_path)
    
    # Delete the files within the original folder (folder_path)
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)

# Function to schedule the backup
def schedule_backup():
    # Schedule the backup to run every Friday at 11:56 AM (adjust the time as needed)
    schedule.every().friday.at('11:56').do(main)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print(f"Error in scheduled backup : {e}")
        # Exit the loop if an error occurs during scheduled task execution
        return
    
# Function to send email notification
def send_email_notification(subject, body):
    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'your_email@gmail.com'
    smtp_password = 'your_password'
    to_email = 'recipient_email@gmail.com'

    # Send email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        message = MIMEMultipart()
        message['From'] = smtp_user
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        server.sendmail(smtp_user, to_email, message.as_string())
        print(f"Email notification sent successfully.")
    except Exception as e:
        print(f"Error sending email notification: {e}")

# Entry point of the program
if __name__ == "__main__":
    schedule_backup()  # Start scheduling the backup
    while True:
        schedule.run_pending()
        time.sleep(1)
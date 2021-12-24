import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f=open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'P9elMmuyoMMAAAAAAAAAARRAJZz2PH60xce3ukRtVcE3x5R1ugCaoruWooFeIsnz'
    transferData = TransferData(access_token)

    file_from = input("Enter your source file path: ")
    file_to = input("Enter your destination file path: ")  
    
    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved successfully!")

if __name__ == '__main__':
    main()
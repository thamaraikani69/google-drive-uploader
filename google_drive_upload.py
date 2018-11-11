
            ####---------------------------------------sivaya nama---------------------------------------###

from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaFileUpload,MediaIoBaseDownload
import os
import mimetypes
SCOPES = 'https://www.googleapis.com/auth/drive'




def uploadFile_code(file_name,file_path,mimetype):

    file_metadata = {'name': file_name}
    media = MediaFileUpload(file_path,mimetype=mimetype)
    file = service.files().create(body=file_metadata,media_body=media,fields='id').execute()
    print ('File ID: %s' % file.get('id'))


if __name__ == '__main__':
    t=os.path.realpath('token.json')
    store = file.Storage(t)
    creds = store.get()
    if not creds or creds.invalid:
        k = os.path.realpath('credentials.json')
        flow = client.flow_from_clientsecrets(k, SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    #enter the file path here
    file_path = input('enter the file name')#'C:\\Users\\\Desktop\\unnamed.jpg'
    file_name = os.path.basename(file_path)

    type = mimetypes.guess_type(file_path)
    mimetype = type[0]

    uploadFile_code(file_name,file_path,mimetype)



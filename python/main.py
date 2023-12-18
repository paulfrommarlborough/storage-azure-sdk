from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential,InteractiveBrowserCredential

# not async.
import os

account_name = os.environ['ACCOUNT_NAME']
account_key = os.environ['ACCOUNT_KEY']

print(account_name)

account_url = f"https://{account_name}.blob.core.windows.net"
#credential = DefaultAzureCredential()

print (account_url)

blob_client =BlobServiceClient(account_url, credential=account_key) 
#blob_client =BlobServiceClient().from_connection_string(connection_str) 

print(blob_client)

print('list containers')
containers = blob_client.list_containers(include_metadata=True)
for c in containers:
    container_client = blob_client.get_container_client(c)
    print(c['name'], c['metadata'])
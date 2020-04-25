from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'ahmedlvstore' # Must be replaced by your <storage_account_name>
    account_key = 'Lc0mmzeTv9NcDo9xjDa+GlEKRwmye9XXxwQeC5FgL1YZKtS3+Ka9ksZgRy3MzYDLy8UyibXZz4k6SnxwiqqVZw==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'ahmedlvstore' # Must be replaced by your storage_account_name
    account_key = 'Lc0mmzeTv9NcDo9xjDa+GlEKRwmye9XXxwQeC5FgL1YZKtS3+Ka9ksZgRy3MzYDLy8UyibXZz4k6SnxwiqqVZw==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None

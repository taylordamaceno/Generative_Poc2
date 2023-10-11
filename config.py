from azure.identity import DefaultAzureCredential
from azure.keyvault import KeyVaultClient


def get_keyvault_credentials():
    credential = DefaultAzureCredential()
    keyvault_client = KeyVaultClient(credential)
    secrets = {
        "DATABASE_URL": keyvault_client.get_secret("my-keyvault", "DATABASE_URL").value,
        "OPENAI_API_KEY": keyvault_client.get_secret("my-keyvault", "OPENAI_API_KEY").value,
    }
    return secrets


DATABASE_URL = get_keyvault_credentials()["DATABASE_URL"]
API_KEY = get_keyvault_credentials()["OPENAI_API_KEY"]


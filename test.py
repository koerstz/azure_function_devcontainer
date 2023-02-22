import os
from azure.storage.blob import BlobServiceClient

print("Hey from devcontainer!")


def pytest_generate_tests():
    """ Function to setup test-container in azurite """
    os.environ[
        "AZURE_STORAGE_CONNECTION_STRING"
    ] = "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://azurite:10000/devstoreaccount1;"
    os.environ["STORAGE_CONTAINER"] = "testcontainer"

    # Create a container for Azurite for the first run
    blob_service_client = BlobServiceClient.from_connection_string(
        os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
    )
    try:
        blob_service_client.create_container(os.environ.get("STORAGE_CONTAINER"))
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    pytest_generate_tests()

# Base class for data sources
class DataSource:
    def __init__(self, name="My data source"):
        self.name = name
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def get_data(self):
        return self.data

    def __str__(self):
        return f"DataSource: {self.name}"

# Decorator class for adding encryption to a data source
class EncryptedDataSource:
    def __init__(self, data_source, key):
        self.data_source = data_source
        self.key = key

    def add_data(self, data):
        try:
            encrypted_data = self.encrypt(data)
            self.data_source.add_data(encrypted_data)
        except Exception as e:
            print(f"Error encrypting data: {str(e)}")

    def encrypt(self, data):
        return f"ENCRYPTED-{data}-{self.key}"

    def get_data(self):
        return self.data_source.get_data()

    def decrypt(self, data):
        if data.startswith("ENCRYPTED-") and data.endswith(f"-{self.key}"):
            return data[len("ENCRYPTED-") + len(self.key) + 2:]
        else:
            return data

    def __str__(self):
        return f"EncryptedDataSource: {self.data_source}"

# Decorator class for adding compression to a data source
class CompressedDataSource:
    def __init__(self, data_source, compression_type):
        self.data_source = data_source
        self.compression_type = compression_type

    def add_data(self, data):
        try:
            compressed_data = self.compress(data)
            self.data_source.add_data(compressed_data)
        except Exception as e:
            print(f"Error compressing data: {str(e)}")

    def compress(self, data):
        return f"COMPRESSED-{data}-{self.compression_type}"

    def get_data(self):
        return self.data_source.get_data()

    def decompress(self, data):
        if data.startswith("COMPRESSED-") and data.endswith(f"-{self.compression_type}"):
            return data[len("COMPRESSED-") + len(self.compression_type) + 2:]
        else:
            return data

    def __str__(self):
        return f"CompressedDataSource: {self.data_source}"

# Example usage
source = DataSource("My data source")  # Create a base data source
encrypted_source = EncryptedDataSource(source, "my_key")  # Add encryption to data source
compressed_and_encrypted_source = CompressedDataSource(encrypted_source, "zip")  # Add compression to encrypted data source

# Add data to different sources
source.add_data("Hello, world!")
encrypted_source.add_data("Hello, world!")
compressed_and_encrypted_source.add_data("Hello, world!")

# Print data from different sources
print(source.get_data())  # Output: ['Hello, world!']
print(encrypted_source.get_data())  # Output: ['Hello, world!']
print(compressed_and_encrypted_source.get_data())  # Output: ['Hello, world!']

# Print source information
print(source)
print(encrypted_source)
print(compressed_and_encrypted_source)
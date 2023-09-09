from abc import ABC, abstractmethod

# Step 1: Create an abstract class or interface for ResourceAccess.
class ResourceAccess(ABC):
    @abstractmethod
    def access_resource(self):
        pass

# Step 2: Create a RealResourceAccess class that implements the interface.
class RealResourceAccess(ResourceAccess):
    def __init__(self, resource):
        self.resource = resource

    def access_resource(self):
        try:
            print(f"Access granted to {self.resource.name}.")
        except AttributeError:
            print("Error: Resource information not found.")

# Step 3: Create a ResourceAccessProxy class that also implements the interface.
class ResourceAccessProxy(ResourceAccess):
    def __init__(self, resource):
        self.resource = resource
        self._real_resource_access = None

    def access_resource(self):
        if self._real_resource_access is None:
            self._real_resource_access = RealResourceAccess(self.resource)
        try:
            print("Proxy: Logging access request.")
            self._real_resource_access.access_resource()
            print("Proxy: Logging access request completed.")
        except AttributeError:
            print("Error: Resource information not found.")

class Resource:
    def __init__(self, name):
        self.name = name

# Step 4: Client code interacts with the ResourceAccessProxy, not the RealResourceAccess.
def main():
    resource1 = Resource("Secret File")
    resource2 = Resource("Confidential Database")

    proxy1 = ResourceAccessProxy(resource1)
    proxy2 = ResourceAccessProxy(resource2)

    proxy1.access_resource()  # Output: Proxy: Logging access request. Access granted to Secret File. Proxy: Logging access request completed.
    proxy2.access_resource()  # Output: Proxy: Logging access request. Access granted to Confidential Database. Proxy: Logging access request completed.

if __name__ == "__main__":
    main()
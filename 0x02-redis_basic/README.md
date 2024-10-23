# Redis in Python

## Overview

Redis is an open-source, in-memory data structure store used as a database, cache, and message broker. It supports various data structures, including strings, hashes, lists, sets, and sorted sets. This README provides a guide on how to set up and use Redis with Python.

## Prerequisites

- Python 3.x installed on your machine.
- Redis server installed and running. You can download it from [Redis.io](https://redis.io/download) or use a package manager (e.g., `apt`, `brew`, or `choco`).

## Installation

### Install Redis

**For Linux/Mac**:
```bash
sudo apt update
sudo apt install redis-server
```

**For Windows**:
You can use [Memurai](https://www.memurai.com/) or run Redis in Windows Subsystem for Linux (WSL).

### Install Redis Python Client

You can use the `redis` library to interact with Redis from Python. Install it using pip:

```bash
pip install redis
```

## Usage

### Starting the Redis Server

Before running your Python scripts, ensure that the Redis server is running:

```bash
redis-server
```

### Sample Code

Here’s a simple example of how to use Redis in Python:

```python
import redis

# Create a Redis client
client = redis.Redis()

# Set a key-value pair
client.set('my_key', 'Hello, Redis!')

# Retrieve the value
value = client.get('my_key')
print(value.decode('utf-8'))  # Output: Hello, Redis!
```

### Using the Cache Class

In this section, we'll demonstrate how to use a `Cache` class that interacts with Redis.

#### Cache Class Implementation

```python
import redis
import uuid
from typing import Union

class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key.
        
        Args:
            data: The data to be stored, can be str, bytes, int, or float.
        
        Returns:
            The generated key as a string.
        """
        key = str(uuid.uuid4())  # Generate a random key
        self._redis.set(key, data)  # Store data in Redis using the key
        return key
```

#### Example Usage of Cache Class

```python
# main.py
from exercise import Cache

cache = Cache()
data = b"hello"  # Data to be stored
key = cache.store(data)
print(key)  # Prints the generated key

# Retrieve and print the stored data using Redis client
local_redis = redis.Redis()
print(local_redis.get(key))  # Output: b'hello'
```

## Troubleshooting

If you encounter any issues, check the following:

- Ensure the Redis server is running.
- Verify that you can connect to Redis using the command line:
  ```bash
  redis-cli ping
  ```
  It should return `PONG`.
  
- Ensure that your Python script has the correct permissions and is being executed in an environment where Redis can be accessed.

## Conclusion

This README provides a brief introduction to using Redis with Python. For more advanced features and configurations, refer to the [Redis documentation](https://redis.io/documentation) and the [Python Redis client documentation](https://redis-py.readthedocs.io/en/stable/).

Feel free to customize this README according to your specific project needs!


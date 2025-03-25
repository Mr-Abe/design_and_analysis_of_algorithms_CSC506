import random

class HashTable:
    """Simple Hash Table implementation using chaining."""

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        """Compute the hash value for a given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert or update a key-value pair into the hash table."""
        index = self._hash_function(key)
        bucket = self.table[index]

        for idx, element in enumerate(bucket):
            # If key already exists, update the value
            if element[0] == key:
                bucket[idx] = (key, value)
                return
        # Otherwise, append a new (key, value) pair
        bucket.append((key, value))

    def get(self, key):
        """Retrieve the value associated with a key."""
        index = self._hash_function(key)
        bucket = self.table[index]

        for element in bucket:
            if element[0] == key:
                return element[1]
        return None

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash_function(key)
        bucket = self.table[index]

        for idx, element in enumerate(bucket):
            if element[0] == key:
                del bucket[idx]
                return True
        return False
    
    def show_bucket(self, key):
        """
        Show the bucket corresponding to the given key
        and indicate if a collision has occurred.
        """
        index = self._hash_function(key)
        bucket = self.table[index]
        print(f"\nThe key '{key}' hashes to bucket index {index}.")
        if bucket:
            print(f"Bucket contents: {bucket}")
            if len(bucket) > 1:
                print("-> Collision detected! More than one entry in this bucket.")
            else:
                print("-> No collision: only one entry in this bucket.")
        else:
            print("This bucket is empty (no entry for that key).")

def generate_user_preferences():
    """Simulate random user preferences."""
    possible_preferences = [
        "sports_videos", "comedy_shows", "tech_news", "gaming_streams", 
        "cooking_tutorials", "travel_vlogs", "music_clips", "movie_trailers", 
        "fitness_tips", "fashion_advice"
    ]
    # Randomly pick a few interests to represent a user’s preferences
    num_prefs = random.randint(1, 3)
    return random.sample(possible_preferences, num_prefs)

def populate_hash_table(hash_table, num_users=5):
    """
    Simulated user data for the hash table.
    :param hash_table: An instance of the HashTable class.
    :param num_users: Number of random user records to generate.
    """
    for i in range(num_users):
        user_id = f"user_{100 + i}"
        hash_table.insert(user_id, generate_user_preferences())

def generate_recommendations(user_id, hash_table):
    """
    Dummy function that simulates generating recommendations 
    based on user preferences stored in the hash table.
    """
    user_preferences = hash_table.get(user_id)
    if not user_preferences:
        return f"No preferences found for {user_id}."
    return f"Recommendations for {user_id}: {user_preferences}"

def main():
    # Prompt user for the hash table size
    while True:
        try:
            table_size = int(input("Enter hash table size (e.g., 5, 10, 20): "))
            if table_size <= 0:
                print("Please enter a positive integer for the table size.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Prompt user for how many users to simulate
    while True:
        try:
            user_count = int(input("Enter how many users to simulate (e.g., 5, 10, 20): "))
            if user_count <= 0:
                print("Please enter a positive integer for the number of users.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Create the hash table
    user_data = HashTable(size=table_size)

    # Populate the table with simulated user data
    populate_hash_table(user_data, num_users=user_count)
    print(f"\nHash table created with size={table_size} and {user_count} simulated user entries.\n")

    # Demonstrate user recommendations retrieval and bucket-collision check in a loop
    while True:
        print("Menu options:")
        print("1) Get recommendations for a user")
        print("2) Show bucket info for a given user key")
        print("3) Exit")
        
        choice = input("Select an option (1, 2, or 3): ").strip()
        if choice == '1':
            user_id = input("Enter a user ID (e.g., 'user_101'): ").strip()
            result = generate_recommendations(user_id, user_data)
            print(result)
            print()
        elif choice == '2':
            user_id = input("Enter a user ID to show bucket info (e.g., 'user_101'): ").strip()
            user_data.show_bucket(user_id)
            print()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid selection. Please try again.\n")

if __name__ == "__main__":
    main()
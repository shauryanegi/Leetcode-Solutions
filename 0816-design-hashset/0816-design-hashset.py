class MyHashSet:

    def __init__(self):
        # TC: O(1) | SC: O(bucket_size)
        # Initialize a list of empty buckets
        self.bucket_size = 10007  # Prime number to reduce collisions
        self.buckets = [[] for _ in range(self.bucket_size)]

    def add(self, key: int) -> None:
        # TC: O(k) where k = number of elements in the bucket (worst case)
        # SC: O(1) (amortized, one new element may be added)
        index = key % self.bucket_size
        bucket = self.buckets[index]

        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        # TC: O(k) where k = number of elements in the bucket
        # SC: O(1)
        index = key % self.bucket_size
        bucket = self.buckets[index]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        # TC: O(k) where k = number of elements in the bucket
        # SC: O(1)
        index = key % self.bucket_size
        return key in self.buckets[index]

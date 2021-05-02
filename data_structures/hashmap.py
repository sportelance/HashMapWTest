class HashMap: 

  def __init__(self, size):
    self.size = size
    self.hash_map = self.create_buckets()

  def create_buckets(self):
    return [[] for i in range(self.size)]
  
  def find_val(self, key):
    hashed_key = hash(key) % self.size
    bucket = self.hash_map[hashed_key]
    found_key = False
    found_val = False
    found_index = False
    for index, record in enumerate(bucket):
      record_key, record_val = record
      if record_key == key:
        found_key = True
        found_val = record_val
        found_index = index
        break
    return found_key, found_val, found_index, bucket

  def set(self, key, val):
    found_key, found_val, found_index, bucket = self.find_val(key)
    if found_key:
      bucket[found_index] = (key, val)
    else: 
      bucket.append((key, val))
  
  def get(self, key):
    found_key, found_val, found_index, bucket = self.find_val(key)
    if found_key:
      return found_val
    else:
      return "Record not found"
  
  def delete(self, key):
    found_key, found_val, found_index, bucket = self.find_val(key)
    if found_key:
      bucket.pop(found_index)
    else:
      return "Record not found"
  
  def __str__(self):
    return "".join(str(item) for item in self.hash_map) 
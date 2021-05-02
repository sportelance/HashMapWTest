from data_structures.hashmap import HashMap

map = HashMap(5)

# a user should be able to declare a new hashmap
assert map;

# the hashmap should contain a size variable corresponding with the amount passed into __init__
assert map.size == 5;

# the HashMap should contain a hash_map property
# at this point, that property should contain an empty array of arrays with a length equal to size
assert len(map.hash_map) == map.size; 

# HashMap's get, set, and delete methods rely upon the proper functioning of the find_val method
# If get, set, and delete are fully functional, find_val is as well

# In this example, the data being stored is a large list of directors and their "best" film
# The director's last name is the key, the film's name is the value

# If the user calls set and passes in a value, that value should be hashed and stored in the bucket corresponding to the passed-in key
# as computed by the hash function. By observing where the hash function placed the KVP and hard-coding that value into the assertion case, 
# this test also tests that hash function places the pair in the same bucket consistently
map.set('Kubrick', 'Dr Strangelove')
assert map.hash_map[3] == [('Kubrick', 'Dr Strangelove')]

# if there is already a value corresponding to the passed-in key, that value should be overwritten
map.set('Kubrick', '2001')
assert map.hash_map[3] == [('Kubrick', '2001')]

# Get should return the value associated with the specified key, if one exists
assert map.get('Kubrick') == '2001'

# If that key does not exist, get should return "Record not found"
assert map.get("Wiseau") == "Record not found"

# Delete should remove the value associated with a key, if one exists
map.set('Wiseau', 'The Room')
assert map.get('Wiseau') =='The Room'
map.delete('Wiseau')
assert map.get("Wiseau") == "Record not found"

# The hash function should assign values to different buckets (python's hash function distributes the buckets alphabetically)
map.set('Coen', 'No Country for Old Men')
map.set('Joon-Ho', 'Mother')
map.set('Hitchcock', 'Vertigo')
map.set('Welles', 'Citizen Kane')
for entry in map.hash_map:
  assert len(entry) != 0
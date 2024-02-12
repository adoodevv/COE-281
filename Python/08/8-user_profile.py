# use arbitrary keyword arguments

def build_profile(first, last, **user_info):
   user_info['first_name'] = first
   user_info['last_name'] = last
   return user_info

print(build_profile('joe', 'adoo'))
print(build_profile('joe', 'adoo', location='accra', school='knust'))
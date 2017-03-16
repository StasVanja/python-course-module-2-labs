"""
create dict with 5 items, where keys will be country name and value - domain name, i.e. {Ukraine:UA}
"""

Dictionary = dict(Ukraine = 'UA', Russia = 'RU', Poland = 'PL', Germany = 'DE', France = 'FR')

"""
create another dict with 5 items, where values of countries will be keys, and values will be the capitals i.e.
 {'UA': 'Kiev'}
"""

Dictionary2 = {'UA': 'Kiev', 'RU': 'Moscow', 'PL': 'Warsaw', 'DE': 'Berlin', 'FR': 'Paris'}

"""
add one more element to each dict above
"""

Dictionary.update(Slovakia = 'SK')
Dictionary2.update(SK = 'Slovakia')


"""
print sentence "Domain for COUNTRY is DOMAIN." for each record in countries with the replace from dicts
"""

for key, value in Dictionary.items():
    print("Domain for {} is {}".format(key, value))

"""
print sentence "The capital of COUNTRY is CAPITAL" for each record in capitals with the replace from dicts
"""

for key, value in Dictionary2.items():
    print("The capital of {} is {}".format(key, value))
"""
Merge sentences above together with one cycle
"""

for key, value in Dictionary.items():
    print("Domain for {} is {}. The capital is {}".format(key, value, Dictionary2[value]))

"""
Add to each value of first dict another two domains: COM and GOV
"""

for key, value in Dictionary.items():
    Dictionary[key] = [value, 'COM', 'GOV']

for key, value, in Dictionary.items():
    print("Domain for {} is {}. The capital is {}".format(key,value, Dictionary2[value[0]]))
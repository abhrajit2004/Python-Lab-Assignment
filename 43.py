dictionary = {"Suka":600000,"Indra":700000,"Abhra":500000,"Shoob":800000}
sorted_dictionary = dict(sorted(dictionary.items(),key = lambda item:item[1]))
print("The sorted dictionary is:",sorted_dictionary)
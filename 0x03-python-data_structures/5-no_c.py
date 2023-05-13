def no_c(my_string):
    filtered_chars = filter(lambda x: x.lower() != 'c', my_string)
    return "".join(filtered_chars)

try:
    return my_dict['value']
except KeyError:
    ret = my_dict['value'] = None
    return ret

def get_param(param):
    default = 'parametro incorreto'
    ret = {
        'nome': 'causa',
        'idade': 42,
        'sexo': 'M'
    }

    return ret.get(param, default)


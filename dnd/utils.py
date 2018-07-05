import sys


def get_module_function(module_name, args, default_function='__get'):
    target_module = sys.modules[module_name]

    if len(args) <= 0:
        return getattr(target_module, default_function)(args)

    module_content = dir(target_module)
    request = args.pop(0)
    if f'__{request}' in module_content:
        method = getattr(target_module, f'__{request}')
        return method(args)

    return getattr(target_module, default_function)(args)

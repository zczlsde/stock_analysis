class DefTypesPool():
    def _init_(self):
        self.routes = {}
    def route_types(self, types_str):
        def decorator(f):
            self.routes[types_str] = f
            return f
        return decorator
    def route_output(self, path):
        function_val = self.routes.get(path)
        if function_val:
            return function_val
        else:
            return ValueError('Route "{}"" has not been registered'.format(path))

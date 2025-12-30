from .extra import fold128

class Surface:
    def __init__(self, surface_id, surface_type, parameters, label=None):
        self.surface_id = surface_id
        self.surface_type = surface_type
        self.parameters = parameters
        self.label = label

    def string(self):
        param_str = ' '.join(f"{k}={v}" for k, v in self.parameters.items())
        _cmt = ''
        if self.label:
            _cmt = f"$ {self.label}"
        _str = f"{self.surface_id} {self.surface_type} {param_str}{_cmt}"
        return fold128(_str)+"\n"

class px(Surface):
    def __init__(self, surface_id, D, label=None):
        super().__init__(surface_id, 'PX', {'D': D}, label)
    def string(self):
        return f"{self.surface_id} PX {self.parameters['D']}"+"\n"

class py(Surface):
    def __init__(self, surface_id, D, label=None):
        super().__init__(surface_id, 'PY', {'D': D}, label)
    def string(self):
        return f"{self.surface_id} PY {self.parameters['D']}"+"\n"

class pz(Surface):
    def __init__(self, surface_id, D, label=None):
        super().__init__(surface_id, 'PZ', {'D': D}, label)
    def string(self):
        return f"{self.surface_id} PZ {self.parameters['D']}"+"\n"

class rcc(Surface):
    def __init__(self, surface_id, vx, vy, vz, h1, h2, h3, r, label=None):
        super().__init__(surface_id, 'RCC', {'VX': vx, 'VY': vy, 'VZ': vz, 'H1': h1, 'H2': h2, 'H3': h3, 'R': r}, label)

    def string(self):
        return f"{self.surface_id} RCC {self.parameters['VX']} {self.parameters['VY']} {self.parameters['VZ']} {self.parameters['H1']} {self.parameters['H2']} {self.parameters['H3']} {self.parameters['R']}"+"\n"

class rpp(Surface):
    def __init__(self, surface_id, x1, x2, y1, y2, z1, z2, label=None):
        super().__init__(surface_id, 'RPP', {'X1': x1, 'X2': x2, 'Y1': y1, 'Y2': y2, 'Z1': z1, 'Z2': z2}, label)

    def string(self):
        return f"{self.surface_id} RPP {self.parameters['X1']} {self.parameters['X2']} {self.parameters['Y1']} {self.parameters['Y2']} {self.parameters['Z1']} {self.parameters['Z2']}"+ "\n"

class cx(Surface):
    def __init__(self, surface_id, r, label=None):
        super().__init__(surface_id, 'CX', {'R': r}, label)

    def string(self):
        return f"{self.surface_id} CX {self.parameters['R']}"+"\n"

class so(Surface):
    def __init__(self, surface_id, r, label=None):
        super().__init__(surface_id, 'SO', {'R': r}, label)

    def string(self):
        return f"{self.surface_id} SO {self.parameters['R']}"+"\n"
class FormHelper:
    def transfomed_keys(self, keys, index):
        return [self.transform(key, index) for key in keys]
    
    def transform(self, key, index):
        return str(key) + '_' + str(index)
    
    def row_exists(self, form, keys, index):
        return all(self.transform(key, index) in form for key in keys)
    
    def key_exists(self, form, key, index):
        return self.transform(key, index) in form
    
    def values(self, form, keys, index) -> list:
        return [form[key] for key in self.transfomed_keys(keys, index)]
    
    def value(self, form, key, index):
        return form[self.transform(key, index)]
    
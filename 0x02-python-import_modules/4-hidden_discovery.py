# Load the hidden_4.pyc module
spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Get the names defined in the module
names = dir(module)
for name in sorted(names):
    if not name.startswith("__"):
        print(name)


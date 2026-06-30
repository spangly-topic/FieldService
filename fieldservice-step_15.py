# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: FieldService
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {k.lower(): v for k, v in handlers.items()}

    def dispatch(self, command_text):
        cmd = command_text.strip().lower()
        if not cmd or cmd.startswith('#'): return None
        parts = cmd.split(maxsplit=1)
        name = parts[0]
        args = parts[1].strip() if len(parts) > 1 else ''
        handler = self.handlers.get(name)
        if not callable(handler): return f'Unknown command: {name}'
        try:
            result = handler(args)
            if isinstance(result, str): return result
            return 'OK'
        except Exception as e:
            return f'Error executing "{name}": {e}'

    def register(self, name, func):
        self.handlers[name.lower()] = func

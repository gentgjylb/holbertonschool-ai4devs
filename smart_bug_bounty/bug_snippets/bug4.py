# bug4.py – ConfigManager with shallow-copy/mutated-defaults bug
class ConfigManager:
    def __init__(self):
        self.default_config = {
            "host": "localhost",
            "port": 8080,
            "debug": False,
            "allowed_origins": ["http://localhost:3000"],
        }
        # Bug: assignment, not a copy – both names point to the same dict.
        self.current_config = self.default_config

    def update_config(self, user_config):
        for key, value in user_config.items():
            if isinstance(value, list) and key in self.current_config:
                # Also mutates default_config["allowed_origins"] in-place
                self.current_config[key].extend(value)
            else:
                self.current_config[key] = value

    def get_config(self):
        return self.current_config

    def reset_config(self):
        # default_config was already mutated; reset has no real effect.
        self.current_config = self.default_config

def main():
    manager = ConfigManager()
    user_settings = {
        "port": 9090,
        "debug": True,
        "allowed_origins": ["https://myapp.com"],
    }
    manager.update_config(user_settings)
    print("Updated:", manager.get_config())
    manager.reset_config()
    print("Reset:  ", manager.get_config())  # still shows mutated values
if __name__ == "__main__":
    main()

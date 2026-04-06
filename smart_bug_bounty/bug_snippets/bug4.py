# bug4.py
# Intended behavior: A configuration manager that stores a set of default
# settings, lets user overrides be applied, and supports resetting back
# to the original defaults at any time.

class ConfigManager:
    def __init__(self):
        self.default_config = {
            "host": "localhost",
            "port": 8080,
            "debug": False,
            "allowed_origins": ["http://localhost:3000"],
        }

        # Bug: This creates a reference to the same dict object, not a copy.
        # Both names now point to the identical dictionary in memory.
        self.current_config = self.default_config

    def update_config(self, user_config):
        """Apply user-supplied keys on top of current configuration."""
        for key, value in user_config.items():
            if isinstance(value, list) and key in self.current_config:
                # Mutating the list also mutates self.default_config["allowed_origins"]
                self.current_config[key].extend(value)
            else:
                self.current_config[key] = value

    def get_config(self):
        """Return the currently active configuration."""
        return self.current_config

    def reset_config(self):
        """Reset current configuration back to factory defaults."""
        # Because default_config was mutated above, this re-assigns the
        # already-corrupted object — the reset has no real effect.
        self.current_config = self.default_config


def main():
    manager = ConfigManager()

    user_settings = {
        "port": 9090,
        "debug": True,
        "allowed_origins": ["https://myapp.com"],
    }

    manager.update_config(user_settings)
    print("Updated config:", manager.get_config())

    manager.reset_config()
    print("Reset config:  ", manager.get_config())   # Still shows mutated values


if __name__ == "__main__":
    main()

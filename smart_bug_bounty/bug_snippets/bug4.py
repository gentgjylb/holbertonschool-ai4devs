# A simple configuration manager that merges default configurations
# with user-provided configurations.

class ConfigManager:
    def __init__(self):
        # Default configuration settings
        self.default_config = {
            "host": "localhost",
            "port": 8080,
            "debug": False,
            "allowed_origins": ["http://localhost:3000"]
        }
        self.current_config = self.default_config

    def update_config(self, user_config):
        """
        Updates the current configuration with user specifics.
        """
        # Bug: Modifying self.current_config directly modifies self.default_config
        # because they reference the same dictionary object.
        for key, value in user_config.items():
            if isinstance(value, list) and key in self.current_config:
                # Append to existing list
                self.current_config[key].extend(value)
            else:
                self.current_config[key] = value

    def get_config(self):
        return self.current_config

    def reset_config(self):
        """
        Resets configuration to the defaults.
        """
        # Because of the bug above, default_config is also mutated
        self.current_config = self.default_config

def main():
    manager = ConfigManager()
    
    user_settings = {
        "port": 9090,
        "debug": True,
        "allowed_origins": ["https://myapp.com"]
    }
    
    manager.update_config(user_settings)
    print("Updated Config:", manager.get_config())
    
    # Try to reset
    manager.reset_config()
    print("Reset Config:", manager.get_config())

if __name__ == "__main__":
    main()

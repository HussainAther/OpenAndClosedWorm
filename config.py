import configparser

def load_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def main():
    # Load the configuration file
    config = load_config("config.ini")
    
    # Accessing configurations
    base_url = config['DEFAULT']['BaseURL']
    max_retries = config.getint('DEFAULT', 'MaxRetries')
    log_level = config['DEFAULT']['LogLevel']
    db_host = config['DATABASE']['Host']
    
    # Example of using configurations
    print(f"Base URL: {base_url}")
    print(f"Maximum Retries: {max_retries}")
    print(f"Log Level: {log_level}")
    print(f"Database Host: {db_host}")

if __name__ == "__main__":
    main()


from dotenv import dotenv_values

APP_CONFIG = dotenv_values('.env')

if __name__ == '__main__':
    print(f'Configuracion Variables {APP_CONFIG}')
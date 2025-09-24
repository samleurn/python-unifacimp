class custom_error(Exception):
    def __init__(self, mesagem):
        self._mensagem = mesagem


try:
    raise custom_error('Custom Error!')
except custom_error as e:
    print(f'Error: {e}')


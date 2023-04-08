from instagram.domain.entities import Instagram


class InstagramSerializer:
    def __init__(self, data):
        self.data = data

    def serialized_data(self):
        instagram = Instagram.format_data_to_entity(self.data)
        return {
            'nome_de_usuario': instagram.username,
            'codigo_de_usuario': instagram.code,
            'identificador_unico_de_usuario': instagram.user_id,
        }
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

from DRF.SERIALIZER.serializer.simular_serializer import UserSerializer
from DRF.MODEL.model import DataUser
import json

dados = DataUser()
dados_paylod = dados.payload()

class ReaderView:
    
    def create(self, request_data):
        serializer = UserSerializer(validated_date=request_data)
        response = serializer
        result = {
            "nome_completo": response.get('nome_completo','Não informado'),
            "email": response.get('email','Não informado'),
            "idade": response.get('idade','Não informado')
        }
        
        json_format = json.dumps(result, indent= 4, ensure_ascii=False)
        return f"result: {json_format}"

if __name__ == "__main__":
    view = ReaderView()
    result = view.create(dados_paylod)

    print(result)
        

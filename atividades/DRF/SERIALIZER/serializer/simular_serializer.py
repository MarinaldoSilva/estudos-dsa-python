from DRF.SERIALIZER.funcoes.strings import Funcoes



def UserSerializer(validated_date:dict) -> dict:
    
    format = Funcoes()
    
    validated_date['email'] = format.formalize_email(
        validated_date.get('email')
    )
    validated_date['nome_completo'] = format.format_name(
        validated_date.get('nome_completo')
    )
    validated_date['idade'] = format.verificar_idade(
        validated_date.get('idade')
    )
    
    return validated_date

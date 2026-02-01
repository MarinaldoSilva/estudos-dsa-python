class Funcoes:
    def formalize_email(self,email:str):
        if not email:
            return ""
        format_email = email.strip().lower()
        return format_email

    def format_name(self,name:str):
        if not name:
            return ""
        format = name.title().strip()
        return format
    
    def verificar_idade(self, idade:int):
        if not idade:
            return ""
        if idade <= 17:
            return "Proibido para menores"
        return "Acesso liberado"
    
    


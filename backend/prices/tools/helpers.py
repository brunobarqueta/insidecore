from tools_rest.response_view import ResultViewModel
from . import constantes

def validate_if_id_exist(self) -> ResultViewModel:
    result = ResultViewModel()
    if not self.kwargs.get('pk') >= 1:
        result.add_errors(constantes.PK_INVALIDO)
    else:
        try: 
            instance = self.get_object()
            result.add_result(instance)
        except: result.add_errors(constantes.REGISTRO_INEXISTENTE)
    return result;
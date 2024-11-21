from django.forms import ModelForm
from .models import Investimento

class InvestimentoForm(ModelForm):
    class Meta:
        #Qual a classe que representa esse model(banco de dados)#
        model = Investimento
        #INDICANDO QUE DESEJO TODOS OS CAMPOS DA TABELA DO BANCO NO MEU FORMULARIO '__ALL__'#
        fields = '__all__'
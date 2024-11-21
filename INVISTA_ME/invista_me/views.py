from django.shortcuts import render, HttpResponse, redirect
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required

def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request,'investimentos/investimentos.html',context=dados)

def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html', dados)
@login_required
def criar(request):
    #VERIFICANDO O METODO DO FORMULARIO#
    if request.method == 'POST':
        #PEGANDO AS INFORMAÇÕES INSERIDAS NO FORMULARIO
        investimento_form = InvestimentoForm(request.POST)
        #VERIFICANDO SE O FORMULARIO É VALIDO, OU SEJA, SE TEM DADOS PREENCHIDOS
        if investimento_form.is_valid:
            #CHAMANDO A FUNCAO PARA SALVAR OS DADOS DO FORMULARIO
            investimento_form.save()
        return redirect('investimentos')
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request,'investimentos/novo_investimento.html', context=formulario)
@login_required   
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'GET':
        #POPULANDO O FORMULARIO ATRAVES DA INSTANCIA 'INVESTIMENTO'(PREENCHENDO COM DADOS DO BANCO DE DADOS)
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html',{'formulario':formulario})
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid:
            formulario.save()
        return redirect('investimentos')
@login_required    
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html',{'item':investimento})
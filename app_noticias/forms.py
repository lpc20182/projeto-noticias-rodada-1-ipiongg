from django import forms
'''21 - Criar a página que permite cadastrar uma denúncia, contendo os campos: cidade, estado e descrição'''

class ContatoForm(forms.Form):
    cidade = forms.CharField(max_length=128, min_length=3)
    estado = forms.CharField(required=True)
    descricao = forms.CharField(widget=forms.Textarea)

    def clean(self):
        dados = super().clean()
        # estado deve ser digitado com sigla
        estado = dados.get('estado', None)
        mensagem = dados.get('mensagem')
        if len(estado) > 2:
            self.add_error('estado','Sigla Incorreta')
        return dados
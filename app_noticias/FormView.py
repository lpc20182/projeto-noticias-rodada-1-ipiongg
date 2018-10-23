class ContatoView(FormView):
    template_name = 'app_noticias/contato.html'
    form_class = ContatoForm

    def form_valid(self, form):
        dados = form.clean()
        mensagem = MensagemDeContato(cidade=dados['cidade'], estado=dados['estado'], descricao=dados['descricao'])
        mensagem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse ('contato_sucesso')
    

class ContatoSucessoView(TemplateView):
    template_name = 'app_noticias/contato_sucesso.html'
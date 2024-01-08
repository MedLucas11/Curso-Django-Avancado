from django.test import TestCase
from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Lucas Medeiros'
        self.email = 'lucas@hotmail.com'
        self.assunto = 'Assunto teste'
        self.mensagem = 'Mensagem de teste'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form = ContatoForm(data=self.dados)

    
    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        resp1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        resp2 = form2.send_mail()

        self.assertEquals(resp1, resp2)

     



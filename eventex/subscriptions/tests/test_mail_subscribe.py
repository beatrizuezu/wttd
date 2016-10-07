from django.core import mail
from django.test import TestCase

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Beatriz Harumi', cpf='1234567901', email='beatrizuezu@outlook.com', phone='11-12345-6789')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'beatrizuezu@outlook.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):

        contents = [
            'Beatriz Harumi',
            '1234567901',
            'beatrizuezu@outlook.com',
            '11-12345-6789'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

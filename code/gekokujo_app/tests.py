from django.test import TestCase
from django.urls import reverse

# Create your tests here.

# 成績入力フォームのテスト


class createRecordTest(TestCase):

    def test_get(self):
        response = self.clinet.get(reverse('gekokujo_app:create'))
        self.assertEqual(response.status_code, 200)


# 成績登録処理のテスト

class addRecordTest(TestCase):

import io
import unittest
import PIL.Image
import requests
from requests import request


class MyTestCase(unittest.TestCase):
    def test_home(self):
        response = request('GET', 'http://localhost:9207/')
        sample = response.content.decode()
        self.assertEqual(sample, 'Home page')  # add assertion here

    def test_classify(self):
        img = PIL.Image.open('../data/dog.jpg')
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG')

        with buffer as buf:
            buffer.seek(0)
            response = request('POST', 'http://localhost:9207/classify', data=buf)

        out = response.content.decode('utf-8')
        print(out)
        expected = 'Пембрук'

        self.assertIn(expected, out)

    def test_binary_classify(self):
        img = PIL.Image.open('../data/dog.jpg')
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG')

        with buffer as buf:
            buffer.seek(0)
            response = request('POST', 'http://localhost:9207/classify/binary', data=buf)

        out = response.content.decode('utf-8')
        print(out)
        expected = 'Cat'
        self.assertEqual(expected, out)




if __name__ == '__main__':
    unittest.main()

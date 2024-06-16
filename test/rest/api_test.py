import http.client
import os
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_add_error(self):
        try:
            url = f"{BASE_URL}/calc/add/2/dos"
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as err:
            self.assertEqual(err.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_substract_error(self):
        try:
            url = f"{BASE_URL}/calc/substract/2/nil"
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as err:
            self.assertEqual(err.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply_error(self):
        try:
            url = f"{BASE_URL}/calc/multiply/2/hola"
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as err:
            self.assertEqual(err.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_divide_error(self):
        try:
            url = f"{BASE_URL}/calc/divide/2/0"
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as err:
            self.assertEqual(err.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_power_error(self):
        try:
            url = f"{BASE_URL}/calc/power/0/-1"
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as err:
            self.assertEqual(err.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_sqrt_error(self):
        try:
            url = f"{BASE_URL}/calc/sqrt/-1"
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as err:
            self.assertEqual(err.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_log10_error(self):
        try:
            url = f"{BASE_URL}/calc/log10/0"
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as err:
            self.assertEqual(err.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

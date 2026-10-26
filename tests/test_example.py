import unittest
from unittest.mock import patch
from example import FACT, check_claim


class ExampleTests(unittest.TestCase):
    def test_exact_fact_without_network(self):
        with patch('socket.socket', side_effect=AssertionError('No network')):
            self.assertEqual(check_claim(dict(FACT)), 'SUPPORTED_SYNTHETIC_FACT')

    def test_wrong_value_with_valid_source(self):
        self.assertEqual(check_claim(dict(FACT, value=777700)), 'UNVERIFIED: UNSUPPORTED_CLAIM')

    def test_unknown_source_or_missing_field(self):
        self.assertEqual(check_claim(dict(FACT, source_id='unknown')), 'UNVERIFIED: UNKNOWN_SOURCE')
        claim=dict(FACT); del claim['source_id']
        self.assertEqual(check_claim(claim), 'UNVERIFIED: MISSING_OR_EXTRA_FIELD')

    def test_wrong_type_or_extra_prose(self):
        self.assertEqual(check_claim(dict(FACT,value='123400')), 'UNVERIFIED: UNSUPPORTED_CLAIM')
        self.assertEqual(check_claim(dict(FACT,text='approved')), 'UNVERIFIED: MISSING_OR_EXTRA_FIELD')

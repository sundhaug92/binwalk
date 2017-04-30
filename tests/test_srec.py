from os.path import dirname

import binwalk
from nose.tools import eq_, ok_


def test_hello_world_simple_scan():
    '''
    Test: Open hello-world.srec, scan for signatures
    verify that only one signature is returned
    verify that the only signature returned is Motorola S-rec data-signature
    '''
    scan_result = binwalk.scan(
        dirname(__file__) + '/input-vectors/hello-world.srec',
        signature=True,
        quiet=True)
    ok_(scan_result != [])
    eq_(len(scan_result), 1)
    eq_(scan_result[0].results[0].description,
        'Motorola S-Record; binary data in text format, record type: data (32-bit)')

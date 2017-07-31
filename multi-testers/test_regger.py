import unittest
from unittest import mock
import regger
from concurrent.futures import Future
import pdb

class Test(unittest.TestCase):
    @mock.patch("regger.concurrent.futures.ThreadPoolExecutor")
    def test_method(self, mockpool):
        futs = [Future() for _ in range(regger.MAX_WORKERS)]
        _ = [fut.set_result("Hello.. from.. mock")  for fut in futs]
        pdb.set_trace()
        instance = mockpool.return_value
        instance.submit.side_effect = futs
        regger.thread_futures()

    @mock.patch("regger.concurrent.futures.ThreadPoolExecutor")
    def test_method_with_context_manager(self, mockpool):
        futs = [Future() for _ in range(regger.MAX_WORKERS)]
        _ = [fut.set_result("Hello.. Context man from.. mock")  for fut in futs]
        pdb.set_trace()
        instance = mockpool.return_value.__enter__.return_value
        instance.submit.side_effect = futs
        regger.thread_futures_with_context_manager()


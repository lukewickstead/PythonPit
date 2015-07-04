# # unittest_examples./magic_mock_example.py
# #
# # Example of MagicMock.
# #
# # MagickMock provides mocking and assertion functionality.
# #
#
# from unittest.mock import MagicMock
#
# thing = ProductionClass()
# thing.method = MagicMock(return_value=3)
# value = thing.method(3, 4, 5, key='value')
# thing.method.assert_called_with(3, 4, 5, key='value')
#

# unittest_examples./mock_example.py
#
# Example of MagicMock.
#
# Mock provides mocking and assertion functionality.

from unittest.mock import Mock

# Mocks allow stubbing of data
# The return value can be defined
print("** Simple Stubbed Mock")
mock = Mock(return_value=3)
print(mock.return_value)
print(mock())
print(mock(1))


# Mocks are dynamic; they absorb any call
print("\n\n*** Mocks can absorb any method calls")
mock = Mock()
print(mock.AnyMethod(1, 'a', param='anything'))

# Asserting the mocks was called
print("\n\n*** Asserting Calls Were Made")
mock.AnyMethod.assert_any_calls(1, 'a', param='anything')
mock.AnyMethod.assert_called_with(1, 'a', param='anything')
mock.AnyMethod.assert_called_once_with(1, 'a', param='anything')
# mock.AnyMethod.assert_has_calls(stacks calls)
#
# Assert call count and was called
print("\n\n*** Call Count, Called and Reset_Mock ")
mock = Mock(return_value=None)
mock()
print(mock.call_count)
print(mock.called)
mock.reset_mock()
print(mock.call_count)
print(mock.called)

# TODO: More Examples Of Mocks

#
# # Stub Methods with configure mock
# mock = Mock()
# attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
# mock.configure_mock(**attrs)
# mock.method()
#
# mock.other()
#
#
# # Stub P
# attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
# mock = Mock(some_attribute='eggs', **attrs)
# mock.some_attribute
# mock.method()
# mock.other()
#
# # mock = Mock(return_value=3)
# # mock.return_value
# # mock()

# mock = Mock(side_effect=KeyError('foo'))
# mock()
#
# # Overriding side effect
# values = {'a': 1, 'b': 2, 'c': 3}
# def side_effect(arg):
#     return values[arg]
#
# mock.side_effect = side_effect
# mock('a'), mock('b'), mock('c')

# mock.side_effect = [5, 4, 3, 2, 1]
# mock(), mock(), mock()

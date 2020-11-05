class LoggingContextManager:
    def __enter__(self):
        print("You are in a with-block")
        return 'You are in a with-block!'

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('LoggingContextManager.__exit__:'
                  'normal exit detected.')
        else:
            print('LoggingContextManager.__exit__:'
                  'Exception detected!'
                  'type={}, value={}, traceback={}'.format(
                exc_type, exc_val, exc_tb))


with LoggingContextManager() as x:  # Calling context manager
    print(x)
    raise ValueError('Something has gone wrong!')

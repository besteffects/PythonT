class LoggingContextManager:
    def __enter__(self):
        print("You are in a with-block")
        return 'You are in a with-block!'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('LoggingContextManager.__exit__({}, {}, {}'.format(
            exc_type, exc_val, exc_tb))
        return


with LoggingContextManager() as x:  # Calling context manager
    print(x)
    raise ValueError('Something has gone wrong!')


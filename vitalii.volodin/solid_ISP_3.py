class FileManager:
    @staticmethod
    def check_free_space():
        return True

    @staticmethod
    def create_log_file(filename):
        print('{} successfully created.'.format(filename))


class ITextLog:
    def write_to_log(self):
        print('Write logs...')


class IDBLog(ITextLog):
    def open_connection(self):
        print('Open connection to DB...')

    def close_connection(self):
        print('Close connection to DB...')


class LocalLogger(ITextLog):
    def __init__(self):
        print('Local logger.')



class DBLogger(IDBLog):
    def __init__(self):
        print('DB logger.')


def write_log_to_file():
    local_logger = LocalLogger()
    local_logger.write_to_log()


def write_log_to_db():
    db_logger = DBLogger()
    db_logger.open_connection()
    db_logger.write_to_log()
    db_logger.close_connection()


def main():
    if FileManager.check_free_space():
        FileManager.create_log_file('log.txt')
        write_log_to_file()
        print('Logs have been written successfully')
    else:
        raise IOError

    print("=" * 20)

    if FileManager.check_free_space():
        FileManager.create_log_file('db_log.txt')
        write_log_to_db()
        print('Logs have been written successfully')
    else:
        raise IOError


if __name__ == '__main__':
    main()
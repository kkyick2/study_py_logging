import logging
import logging.config


class MyFilter(logging.Filter):
    def __init__(self, filter_msg):
        super(MyFilter, self).__init__()

        self.filter_msg = filter_msg

    def filter(self, record):
        """
        :param record: LogRecord Object
        :return True to accept record, False to drop record
        """

        if record.levelname == 'INFO':
            return False
        else:
            record.msg += self.filter_msg
        return True


dict_config = {
    'version': 1,
    'disable_existing_loggers': False, # default True
    'filters': {
        'my_filter': {
            '()': MyFilter,
            'filter_msg': 'show how to use filter'
        }
    },
    'formatters': {
        'brief': {
            'datefmt': '%H:%M:%S',
            'format': '%(levelname)-8s; %(name)s; %(message)s;'
        },
        'single-line': {
            'datefmt': '%H:%M:%S',
            'format': '%(levelname)-8s; %(asctime)s; %(name)s; %(module)s:%(funcName)s;%(lineno)d: %(message)s'
        },
        'multi-process': {
            'datefmt': '%H:%M:%S',
            'format': '%(levelname)-8s; [%(process)d]; %(name)s; %(module)s:%(funcName)s;%(lineno)d: %(message)s'
        },
        'multi-thread': {
            'datefmt': '%H:%M:%S',
            'format': '%(levelname)-8s; %(threadName)s; %(name)s; %(module)s:%(funcName)s;%(lineno)d: %(message)s'
        },
        'verbose': {
            'format': '%(levelname)-8s; [%(process)d]; %(threadName)s; %(name)s; %(module)s:%(funcName)s;%(lineno)d'
                      ': %(message)s'
        },
        'multiline': {
            'format': 'Level: %(levelname)s\nTime: %(asctime)s\nProcess: %(process)d\nThread: %(threadName)s\nLogger'
                      ': %(name)s\nPath: %(module)s:%(lineno)d\nFunction :%(funcName)s\nMessage: %(message)s\n'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'brief',
            'filters': ['my_filter'],
            # 'stream': 'ext://sys.stdout'
        },
        'file_handler': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': 'file_handler.log',
            # 'mode': 'a',
            # 'encoding': 'utf-8',
        },
        'null_handler': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'smtp': {
            'level': 'ERROR',
            'class': 'logging.handlers.SMTPHandler',
            'formatter': 'multiline',
            'mailhost': ['127.0.0.1', 60025],
            'fromaddr': 'sender@example.com',
            'toaddrs': ['recipient@example.com'],
            'subject': 'Something went wrong'
        }
    },
    'loggers': {
        '': {  # this is root logger
            'level': 'INFO',
            'handlers': ['null_handler'],
        },
        'parent': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'parent.child': {  # This is child logger of `parent` handler, propagate will up to `parent` handler
            'level': 'DEBUG',
            # 'propagate': False, # default True
            'handlers': ['console', 'file_handler'],
        },
    }
}

# load config
logging.config.dictConfig(dict_config)

if __name__ == '__main__':
    logger = logging.getLogger()
    print(logger.name)  # root

    logger = logging.getLogger('parent').getChild('child')
    print(logger.name)  # parent.child

    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')

    
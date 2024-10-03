# study_py_logging

https://engineeringfordatascience.com/posts/python_logging/

https://github.com/julian-west/e4ds-snippets/tree/master/best-practices/setting-up-logging

## Example0: fail case, cannot log in other py file

```sh
└── src
   ├── main.py                <- main script
   ├── data_processing        <- module for data processing
   │  ├── __init__.py
   │  └── processor.py
   └── model_training         <- module for model_training
      ├── __init__.py
      └── trainer.py

C:\Users\xxx\projects_local\python\study_py_logging>python src\main.py
2024-10-03 00:49:32,894 - INFO - __main__ - Program started
2024-10-03 00:49:32,895 - INFO - __main__ - Main Pre-processing data
2024-10-03 00:49:32,895 - INFO - __main__ - Main Data pre-processing complete
2024-10-03 00:49:32,896 - WARNING - __main__ - Program warning log test
2024-10-03 00:49:32,896 - INFO - __main__ - Program finished

```

## Example1: Simple Project Structure

```sh
└── src1
   ├── main.py                <- main script
   ├── data_processing        <- module for data processing
   │  ├── __init__.py
   │  └── processor.py
   └── model_training         <- module for model_training
      ├── __init__.py
      └── trainer.py

C:\Users\xxx\projects_local\python\study_py_logging>python src1\main.py
2024-10-03 00:49:36,755 - INFO - __main__ - Program started
2024-10-03 00:49:36,756 - INFO - data_processing.processor - Pre-processing data
2024-10-03 00:49:36,756 - INFO - data_processing.processor - Data pre-processing complete
2024-10-03 00:49:36,757 - INFO - model_training.trainer - Training model
2024-10-03 00:49:36,757 - INFO - model_training.trainer - Model training complete
2024-10-03 00:49:36,757 - INFO - __main__ - Main Pre-processing data
2024-10-03 00:49:36,758 - INFO - __main__ - Main Data pre-processing complete
2024-10-03 00:49:36,758 - WARNING - __main__ - Program warning log test
2024-10-03 00:49:36,758 - INFO - __main__ - Program finished
```

## Example2: Detail Project Structure with environment variables (ini config file)

### Getting started

```sh
# create venv
python -m venv venv
venv\Scripts\activate

# install src package in development mode
pip install -e .

# install dependencies in requirements.txt file
pip install -r requirements.txt
```

```sh
├── .env                             <- environment variables
├── README.md
├── config                           <- configuration files
│   ├── logging.dev.ini
│   └── logging.prod.ini
├── logs                             <- log files
├── requirements.txt                 <- dependencies
├── setup.py                         <- setup local package
└── src                              <- project source code
    ├── __init__.py
    ├── data_processing              <- data processing code
    │   ├── __init__.py
    │   └── processor.py
    ├── model_training               <- model training code
    │   ├── __init__.py
    │   └── trainer.py
    └── main.py                      <- main function

(venv) C:\Users\xxx\projects_local\python\study_py_logging>python src2\main.py
2024-10-03 00:49:39,973 - INFO - __main__ - Program started
2024-10-03 00:49:39,973 - INFO - data_processing.processor - Pre-processing data
2024-10-03 00:49:39,974 - INFO - data_processing.processor - Data pre-processing complete
2024-10-03 00:49:39,974 - INFO - model_training.trainer - Training model
2024-10-03 00:49:39,975 - INFO - model_training.trainer - Model training complete
2024-10-03 00:49:39,975 - INFO - __main__ - Main Pre-processing data
2024-10-03 00:49:39,976 - INFO - __main__ - Main Data pre-processing complete
2024-10-03 00:49:39,977 - WARNING - __main__ - Program warning log test
2024-10-03 00:49:39,977 - INFO - __main__ - Program finished
```

## Example3: Detail Project Structure with environment variables (json config file)

```sh
(venv) C:\Users\xxx\projects_local\python\study_py_logging>python src3\main.py
2024-10-03 00:49:43,060 - INFO - __main__ - Program started
2024-10-03 00:49:43,060 - INFO - data_processing.processor - Pre-processing data
2024-10-03 00:49:43,061 - INFO - data_processing.processor - Data pre-processing complete
2024-10-03 00:49:43,061 - INFO - model_training.trainer - Training model
2024-10-03 00:49:43,062 - INFO - model_training.trainer - Model training complete
2024-10-03 00:49:43,062 - INFO - __main__ - Main Pre-processing data
2024-10-03 00:49:43,063 - INFO - __main__ - Main Data pre-processing complete
2024-10-03 00:49:43,065 - WARNING - __main__ - Program warning log test
2024-10-03 00:49:43,065 - INFO - __main__ - Program finished
```

## Example4: Detail Project Structure with environment variables (json config file) update with abs path

```sh
PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir))
```

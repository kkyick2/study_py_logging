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
2024-10-02 23:54:47,285 - INFO - __main__ - Program started
2024-10-02 23:54:47,286 - INFO - __main__ - Main Pre-processing data
2024-10-02 23:54:47,286 - INFO - __main__ - Main Data pre-processing complete
2024-10-02 23:54:47,287 - INFO - __main__ - Program finished

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
2024-10-02 23:51:13,886 - INFO - __main__ - Program started
2024-10-02 23:51:13,886 - INFO - data_processing.processor - Pre-processing data
2024-10-02 23:51:13,887 - INFO - data_processing.processor - Data pre-processing complete
2024-10-02 23:51:13,887 - INFO - model_training.trainer - Training model
2024-10-02 23:51:13,888 - INFO - model_training.trainer - Model training complete
2024-10-02 23:51:13,888 - INFO - __main__ - Main Pre-processing data
2024-10-02 23:51:13,889 - INFO - __main__ - Main Data pre-processing complete
2024-10-02 23:51:13,889 - INFO - __main__ - Program finished
```

## Example2: Detail Project Structure with environment variables

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
2024-10-02 23:55:21,802 - INFO - __main__ - Program started
2024-10-02 23:55:21,803 - INFO - data_processing.processor - Pre-processing data
2024-10-02 23:55:21,804 - INFO - data_processing.processor - Data pre-processing complete
2024-10-02 23:55:21,804 - INFO - model_training.trainer - Training model
2024-10-02 23:55:21,805 - INFO - model_training.trainer - Model training complete
2024-10-02 23:55:21,805 - INFO - __main__ - Main Pre-processing data
2024-10-02 23:55:21,805 - INFO - __main__ - Main Data pre-processing complete
2024-10-02 23:55:21,817 - INFO - __main__ - Program finished
```

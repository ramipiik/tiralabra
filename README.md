# TicTacToe
Course project for tiralabra course at Helsinki University:  
https://tiralabra.github.io/2021_p1/index

## Quick guide
### **1) Install poetry**    
Poetry is used for installing the needed dependancies and starting the application.    
If you have already Poetry installed, you can skip this step.   
     
For installing Poetry on osx/linux/bashonwindows run the below command on command line.    
If it doesn't work, you can try getting for help here: https://python-poetry.org/docs/#installation     
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
```


### **2) Start the application**  
Run the following command in the "Main" directory.
```
poetry run invoke start
```

### Run unit tests (optional)  
Run the following command in the "Main" directory:
```
poetry run invoke test
```

### Check test coverage (optional)  
Run the following command in the "Main" directory. You will get the test coverage report after playing through the game once. 
 ```
 poetry run invoke coverage
 ```
  

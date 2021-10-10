# TicTacToe
Course project for tiralabra course at Helsinki University:  
https://tiralabra.github.io/2021_p1/index

## Getting started
### **1) Install poetry**    
Poetry is used for installing the needed dependancies and starting the application.    
If you have already Poetry installed, you can skip this step.   
     
For installing Poetry on osx/linux/bashonwindows run the below command on command line.        
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
```
If it doesn't work, you can try getting help here:    
https://python-poetry.org/docs/#installation 


### **2) Start the application**  
For starting the application, run the following command in the **"Main" directory**.
```
poetry run invoke start
```
Alternatively, if you don't want to install Poetry, you try just running `python3 main.py` in the "Main" directory.
     
## Tests & styling (optional)
### Run unit tests  
Run the following command in the **"Main" directory**:
```
poetry run invoke test
```

### Test coverage  
Run the following command in the **"Main" directory**. You will get the test coverage report after playing through the game once. 
 ```
 poetry run invoke coverage
 ```
  
### Linting suggestions  
Run the following command in the **"Main" directory**.  
 ```
 poetry run invoke lint
 ```

### Automatic styling  
Run the following command in the **"Main" directory**.  
 ```
 poetry run invoke black
 ```

#!/bin/bash
python3 -m unittest Tests.Test_alphabeta.Test_alphabetaclass -b
python3 -m unittest Tests.Start.Test_Start.Test_Start_Class -b
python3 -m unittest -v Tests.Test_parameters.Test_parameters_class -b

#!/bin/bash
python3 -m unittest Tests.Heuristics.Test_prevent_mustwins -b
python3 -m unittest Tests.Heuristics.Test_mustwin_check -b
python3 -m unittest Tests.Heuristics.Test_closeness_check -b
python3 -m unittest Tests.Heuristics.Test_boundaries_check -b
python3 -m unittest Tests.Heuristics.Test_basic_check -b
python3 -m unittest Tests.test_alphabeta -b
python3 -m unittest Tests.test_start -b
python3 -m unittest Tests.test_parameters -b
python3 -m unittest Tests.test_play -b
python3 -m unittest Tests.test_tictactoe -b


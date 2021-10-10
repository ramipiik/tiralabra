#!/bin/bash
python3 -m unittest Tests.Heuristics.Test_prevent_mustwins -b
python3 -m unittest Tests.Heuristics.Test_mustwin_check -b
python3 -m unittest Tests.Heuristics.Test_closeness_check -b
python3 -m unittest Tests.Heuristics.Test_boundaries_check -b
python3 -m unittest Tests.Heuristics.Test_basic_check -b
python3 -m unittest Tests.test_alphabeta -b
python3 -m unittest Tests.Test_start -b
python3 -m unittest Tests.Test_parameters -b
python3 -m unittest Tests.Test_play -b
python3 -m unittest Tests.Test_tictactoe -b


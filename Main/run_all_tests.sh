#!/bin/bash
python3 -m unittest Tests.Heuristics.test_prevent_mustwins -b
python3 -m unittest Tests.Heuristics.test_mustwin_check -b
python3 -m unittest Tests.Heuristics.test_closeness_check -b
python3 -m unittest Tests.Heuristics.test_boundaries_check -b
python3 -m unittest Tests.Heuristics.test_basic_check -b
python3 -m unittest Tests.test_alphabeta -b
python3 -m unittest Tests.test_start -b
python3 -m unittest Tests.test_parameters -b
python3 -m unittest Tests.test_play -b
python3 -m unittest Tests.test_tictactoe -b


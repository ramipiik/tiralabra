"""Module for running the program through Poetry invoke"""
from invoke import task

@task
def start(ctx):
    ctx.run("python3 ./main.py", pty=True)

@task
def test(ctx):
    ctx.run("python3 -m unittest Tests.Heuristics.test_prevent_mustwins -b")
    ctx.run("python3 -m unittest Tests.Heuristics.test_mustwin_check -b")
    ctx.run("python3 -m unittest Tests.Heuristics.test_closeness_check -b")
    ctx.run("python3 -m unittest Tests.Heuristics.test_boundaries_check -b")
    ctx.run("python3 -m unittest Tests.Heuristics.test_basic_check -b")
    ctx.run("python3 -m unittest Tests.test_alphabeta -b")
    ctx.run("python3 -m unittest Tests.test_start -b")
    ctx.run("python3 -m unittest Tests.test_parameters -b")
    ctx.run("python3 -m unittest Tests.test_play -b")
    ctx.run("python3 -m unittest Tests.test_tictactoe -b")

@task
def coverage(ctx):
    ctx.run("coverage run main.py")
    ctx.run("coverage report -m")

@task
def lint(ctx):
    ctx.run("pylint Heuristics")
    ctx.run("pylint Start")
    ctx.run("pylint Tests")
    ctx.run("pylint alphabeta.py")
    ctx.run("pylint main.py")
    ctx.run("pylint parameters.py")
    ctx.run("pylint play.py")
    ctx.run("pylint tasks.py")
    ctx.run("pylint tictactoe.py")

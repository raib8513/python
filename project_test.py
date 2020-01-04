#!/usr/bin/env bash
set -e

. ~/ .virtualenv/python2.7/bin/activate

PYTHONPATH=. python -m project.commands.test

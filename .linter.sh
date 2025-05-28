#!/bin/bash
cd /home/kavia/workspace/code-generation/easyeventregister-22422-ac4efd5f/easyeventregister
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi


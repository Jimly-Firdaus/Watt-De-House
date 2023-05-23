@echo off
REM Configure the black filter for Git
git config --global filter.black.clean "black --quiet -"
git config --global filter.black.smudge cat
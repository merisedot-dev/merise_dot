# Some utility commands for this project

# erase test_files directory before testing
test:
    rm -rf ./test_files/ && mkdir ./test_files/ && behave

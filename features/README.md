# Testing grounds

This is where tests are being made for this software. We are not using generic unit tests on that one though, the choice has been made to switch to instrumented testing.

Please refer to [behave] documentation for more information about Python instrumented testing. Please also keep in mind that rendering will need to be tested separately.

## Running tests

This procedure assumes your shell is positioned at the root of this repository. First ensure [behave] is installed, as it will be required. Then, run the following command :

```shell
rm -rf ./test_files/ && mkdir ./test_files/ && behave
```

Or, if you have [just] installed :

```shell
just test
```

## Testing conventions

Because we are civilized here, some implicit conventions will be used for testing, as aberrant use cases shall not be tested. These include, but are not limited to :

- having two graphs to handle in *Given* clauses
- bulk entity deletion
- try to segment test scenarios (outline or not) as much has possible
- try to avoid `Scenario Outline` if you don't need it. That will make tests easier to read.
- do not write assertions in implementation of any *Given* clauses. If you need to assert something, you have a problem.
- if you are trying to test for an exception, please collect it in the `Context` object and test for its presence later. If no exceptions are collected, use `None`.

### Verbiage conventions

Some concepts will also be defined here for ease of use and in order to keep the `.feature` files readable. Here are the list :

Phrase       |Definition
-------------|-------------------------------------------------
"we try to"  |Do the action, but collect the exception if risen
"empty graph"|An empty graph and `None` are not the same thing

[behave]: https://behave.readthedocs.io/
[just]: https://github.com/casey/just

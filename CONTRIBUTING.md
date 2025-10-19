# Contribution guidelines

If you feel like something should be added and/or removed in this software, or that something should be fixed, please follow the procedure depending of what you need from this repository.

## Missing feature

If you feel like a feature is missing from the `merise_dot` library, please open an issue first to discuss specifics about the feature, how it should be used and whatnots. Any issue opened this way should have the "enhancement" or "documentation" label, preferably both if the feature doesn't rely on anything documented.

If the issue discussion goes to approve the modification decision, then a PR shall be opened, containing the requested changes. Keep in mind that each PR won't result in a new version because of time and logistic constraints, but each validated PR will be packaged in the next release.

## Bug report

In case of a bug being found in there, please open an issue with the "bug" label and describe what happened. A bug report must contain the following info so I can use it :

- a description of the misbehavior
- steps to reproduce
- any extra information you believe to be relevant to the situation

The issue then may continue into a discussion about the bug to better understand it, then a PR will be made to fix it. Please keep in mind that bugs in need of fixing will lways be sorted depending of the gravity of the bug, in the following order :

1. library breaking bug
2. behavior breaking bug
3. silly little ~~hornets~~ bugs

## Extra testing and documentation

Extra test cases and documentation will always be welcome, wether as standalone or part of an other issue (namely bug reports and enhancements of `merise_dot`). Please refer to [cucumber] documentation to add your extra test cases in a dedicated pull request. Due to Gherkin's nature, it also doubles as scenario documentation, but specifics can be made if they aren't quite as complete as they need to be.

[cucumber]: https://cucumber.io/

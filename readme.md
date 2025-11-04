# Veridica

This project was made for the use of fuzzy comparison algorithmic comparisons for the use in gherkin based test automation.

We found that it was required to have full control over the system to limit dependencies. However that does not mean that others cannot use the code that I have developed and will use.

## Overview

Veridica provides a set of pure Python algorithms to compare strings reliably based on fixed math based algorithms.

It includes:

- Classic string similarity metrics Classic string to string matching based on algorithms like levenstein.

- One-to-many batch comparisons While one to one comparisons can give you a sence of what you are looking for, most usecases involve the comparion for one item to a set. Therefore an implementation was made using classic and recursive techniques that can be directly implemented.

- Timing utilities for measuring comparison performance For now limited to a wrapper function that can give back the time it took to complete for compartive data.

## Installation

```bash
poetry add veridica
```

## Usage

```python
from veridica.similarity import levenshtein
from veridica.batch import compare_many
from veridica.timing import timed

#todo: Create example implementation and example returns.




```

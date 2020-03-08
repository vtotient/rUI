# rUI: Radio User Interface

An interactive python shell to interface with UBC Orbit's custom radio system. Use rUI to get/set radio system registers and run both off-targert and on target-tests.

### YAML testplans

If you have a test plan with no arguments, use null:
```
---
ArduinoTest:
   null
---
DummyTest1:
   arg1: abc
   arg2: 123
   arg3: [1, "dog", 3]
```

##### Docstring format
Lets use the [Google Style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) Docstring.

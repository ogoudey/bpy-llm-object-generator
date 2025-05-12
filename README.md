
# Testing Baseline Performance

Terminal 1:
```
blender <absolute path to a default .blend> --python <absolute path to bpy/interface.py>
```

Terminal 2:
```
python3 interface.py (--np <noun phrase description of geometric object>)
```

This gets the local-to-Blender Python talking with the Python environment of this project. It simply attempts to execute generated code until "success".

## Issues
GPT 4.1's internet snapshot is from some time last year. The internet then did not contain Blender 4.4.3 docs. Either 1. reformulate the problem to an MDP with step-by-step action space, or 2. use a tool to read the docs and plug them into the GPT.

The GPT will create good node trees, but tinkering sometimes needs to be done.

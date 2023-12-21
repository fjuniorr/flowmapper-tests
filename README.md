# Snapshot tests for flowmapper

This repository uses [syrupy](https://github.com/tophat/syrupy) to perform snapshot tests on new versions of `flowmapper` and ensure that flow mappings don't change unexpectedly.

After installing `requirements.txt` and the version of `flowmapper` you want to test run:

```bash
pytest
```

After inspecting any changes in flow mappings and ensure they are all expected you can update the snapshots with:

```bash
pytest --snapshot-update
```

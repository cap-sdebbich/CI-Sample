#!/bin/bash

xcrun xccov view --report --json Build/Logs/Test/*.xcresult > coverage.json

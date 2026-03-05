#!/bin/bash

esptool.py --baud 460800 write_flash 0x1000 ESP32_GENERIC-20251209-v1.27.0.bin

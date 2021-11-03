#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = "7688395"

API_HASH = "d2a4f54c3a3e6f1031558f540ea0d6c5"

BOT_TOKEN = "2037365499:AAHba-q354WnxdYPXkgujpEA6F5qAG8V2o8"

DB_URI = "1BJWap1sBu75ZQGIs9_49Y6cnxFLA4WsBIIdGoLF3kSEqvr6A78A9wcrDAgeybqI-cad33AACVo6RUI7p-GOiXv6TpqzNyss0MmLTYDh3ULqXTbZR1lK4rUCQ-fHEzjDJJCqwjAb80eZFRpdRVpvia3oISlmL_hpJALG4iEEOMJn-aHGQDg72Vq0FVS-097rzgKIjEWgHkOmDR0gcABSZUwaTi-1pDEFCHDplnffM00aLmEyqbvktNePMtnbMuo0d3KOJslyiBE-3FXFVop5mjpQqeAa3Stx9YzLr5t4IiHAp-Fow5Kp7qEotSLKGpCYit9ohIbABPM7GlwzLzd7-68TfGVfIkAY="

USER_SESSION = "@Peppe2003"

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

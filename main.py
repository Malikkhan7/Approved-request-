from flask import Flask, request, redirect, url_for, session

import requests

import os

import hashlib

import uuid

import re  # New import for parsing the model from User-Agent



app = Flask(__name__)

app.secret_key = os.urandom(24)

app.debug = True



APPROVED_KEYS_FILE = 'approved_keys.txt'  # File to store approved keys



# Function to parse mobile name and model from User-Agent

def get_device_name_and_model(user_agent):

    """

    Function to parse the User-Agent string and identify the device type and model.

    """

    if "Android" in user_agent:

        match = re.search(r'\b(\w+\s?\w+)\sBuild', user_agent)  # Extract model name

        device_model = match.group(1) if match else "Unknown Android Model"


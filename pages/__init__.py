import streamlit as st
from PIL import Image

from execute.manga import *
from settings.config import cfg
from settings.connect import *
from call_api.auth.login import *
from call_api.auth.login import login
from call_api.auth.register import signup, verify

from call_api.chapter import *

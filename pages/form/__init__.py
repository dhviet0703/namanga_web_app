import streamlit as st
from PIL import Image

from execute.manga import *
from settings.config import cfg
from settings.connect import *
from call_api.auth.login import *
from call_api.auth.login import login
from call_api.manga import *
from io import BytesIO

import discord
import asyncio
import websocket
import time
import json
import unicodedata
from http.server import BaseHTTPRequestHandler, HTTPServer
from discord.ext import commands

hostName = "localhost"
serverPort = 8090

null = "null"
OldFullArray = [
    {
        "id": 0,
        "nick": "  #0",
        "tokenid": 0,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 0,
        "finalscore": 0,
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 0,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": null,
        "MNn": null,
        "nnmnv": -1,
        "MNW": -1,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 1,
        "nick": "Minion  #1",
        "tokenid": 314,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1341.815999999999,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 92.5,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 96,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 61,
        "MNW": 9248,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 2,
        "nick": "  #2",
        "tokenid": 409,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1358.8600000000024,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 34,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 40,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 16,
        "MNW": 9523,
        "x": 411.7647058823529,
        "y": 1000,
        "rx": 411.7647058823542,
        "ry": 1000.0000000000009,
        "karmamsg": 5
    },
    {
        "id": 3,
        "nick": "Minion  #3",
        "tokenid": 410,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 572.682188792562,
                "y": 1049.8533179042593,
                "mN": 0,
                "angle": 1.5889518528110003,
                "size": 1.3014364624358037
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1091.5589999999993,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 94.5,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 98,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 17,
        "MNW": 9566,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 4,
        "nick": "Minion  #4",
        "tokenid": 411,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 650.3023468011238,
                "y": 1049.823631032678,
                "mN": 0,
                "angle": 1.511981560690219,
                "size": 1.2209665808942183
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 199.91799999999603,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 95.5,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 99,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 18,
        "MNW": 9668,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 5,
        "nick": "Minion  #5",
        "tokenid": 413,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1100.5800000000036,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 95,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 98,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 2,
        "MNW": 9791,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 6,
        "nick": "Minion  #6",
        "tokenid": 412,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1017.233000000002,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 95,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 98,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 19,
        "MNW": 9704,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 7,
        "nick": "Minion  #7",
        "tokenid": 414,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 25.51600000000508,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 95,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 98,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 33,
        "MNW": 9523,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 8,
        "nick": "Minion  #8",
        "tokenid": 364,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 250.4810000000034,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 95,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 98.5,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 95,
        "MNW": 9472,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 9,
        "nick": "  #9",
        "tokenid": 359,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 692.1269999999895,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 34,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 40,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 104,
        "MNW": 9827,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 10,
        "nick": "  #10",
        "tokenid": 358,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 600.5760000000046,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 49,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 19,
        "MNW": 9791,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 11,
        "nick": "  #11",
        "tokenid": 357,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1308.888999999992,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 46.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 90,
        "MNW": 9530,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 12,
        "nick": "  #12",
        "tokenid": 393,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 1037.649216,
                "y": 871,
                "mN": -8.317999999999302,
                "angle": 6.276444427932446,
                "size": 1.7593527677442888
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 841.724000000002,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 48.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 108,
        "MNW": 10095,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 13,
        "nick": "  #13",
        "tokenid": 354,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 0,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 66.65899999999237,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 42.5,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 48,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 78,
        "MNW": 9530,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 14,
        "nick": "  #14",
        "tokenid": 355,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 50.543999999990774,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 49,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 30,
        "MNW": 9530,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 15,
        "nick": "  #15",
        "tokenid": 356,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 250.4810000000034,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 48.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 94,
        "MNW": 9472,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 16,
        "nick": "  #16",
        "tokenid": 360,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 990.3,
                "y": 494.15,
                "mN": 0,
                "angle": 0.7807618161214867,
                "size": 1.4955679148497134
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1358.0070000000014,
        "nn": 0,
        "orientation": -1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 48.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 52,
        "MNW": 9827,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 17,
        "nick": "Minion  #17",
        "tokenid": 400,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1383.8939999999948,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 106.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 23,
        "MNW": 9668,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 18,
        "nick": "Minion  #18",
        "tokenid": 362,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 683.5539999999946,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 106.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 83,
        "MNW": 9407,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 19,
        "nick": "Minion  #19",
        "tokenid": 374,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 100.38599999999678,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 106.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 41,
        "MNW": 9443,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 20,
        "nick": "  #20",
        "tokenid": 363,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 133.23399999998946,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 51,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 82,
        "MNW": 9407,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 21,
        "nick": "Minion  #21",
        "tokenid": 429,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 933,
                "y": 1024,
                "mN": 0,
                "angle": 0.23611087486593701,
                "size": 1.4044267992622386
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 983.918999999989,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 106.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 71,
        "MNW": 9827,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 22,
        "nick": "  #22",
        "tokenid": 404,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1008.9560000000074,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 50.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 72,
        "MNW": 10095,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 23,
        "nick": "  #23",
        "tokenid": 396,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 100.38599999999678,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 50.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 64,
        "MNW": 9443,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 24,
        "nick": "Minion  #24",
        "tokenid": 397,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 675.4750000000076,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 14,
        "MNW": 9472,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 25,
        "nick": "Minion  #25",
        "tokenid": 398,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1358.8600000000024,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 54,
        "MNW": 9523,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 26,
        "nick": "  #26",
        "tokenid": 399,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 775.534999999998,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 50.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 43,
        "MNW": 9566,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 27,
        "nick": "  #27",
        "tokenid": 361,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 825.1329999999998,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 50.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 113,
        "MNW": 8539,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 28,
        "nick": "Minion  #28",
        "tokenid": 401,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1017.233000000002,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 67,
        "MNW": 9704,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 29,
        "nick": "  #29",
        "tokenid": 402,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1100.5800000000036,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 50.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 68,
        "MNW": 9791,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 30,
        "nick": "Minion  #30",
        "tokenid": 366,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 942.1910000000007,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 106,
        "MNW": 9566,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 31,
        "nick": "Minion  #31",
        "tokenid": 403,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 983.918999999989,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 106,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 11,
        "MNW": 9827,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 32,
        "nick": "  #32",
        "tokenid": 367,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 792.2069999999967,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 50.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 89,
        "MNW": 9668,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 33,
        "nick": "Minion  #33",
        "tokenid": 405,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 50.137000000000626,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 109,
        "MNW": 8539,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 34,
        "nick": "Minion  #34",
        "tokenid": 406,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 208.57099999999446,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 87,
        "MNW": 9407,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 35,
        "nick": "  #35",
        "tokenid": 407,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 100.38599999999678,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 50.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 63,
        "MNW": 9443,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 36,
        "nick": "Minion  #36",
        "tokenid": 408,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 675.4750000000076,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 13,
        "MNW": 9472,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 37,
        "nick": "Minion  #37",
        "tokenid": 368,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1183.8890000000047,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 52,
        "MNW": 9704,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 38,
        "nick": "  #38",
        "tokenid": 369,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1267.2360000000062,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 50.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 77,
        "MNW": 9791,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 39,
        "nick": "Minion  #39",
        "tokenid": 370,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1267.2360000000062,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 42,
        "MNW": 9791,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 40,
        "nick": "  #40",
        "tokenid": 375,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 675.4750000000076,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 51.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 96,
        "MNW": 9472,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 41,
        "nick": "  #41",
        "tokenid": 371,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1150.5749999999916,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 49,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 31,
        "MNW": 9827,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 42,
        "nick": "Minion  #42",
        "tokenid": 372,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 50.137000000000626,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 112,
        "MNW": 8539,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 43,
        "nick": "  #43",
        "tokenid": 373,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 208.57099999999446,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 51,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 84,
        "MNW": 9407,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 44,
        "nick": "Minion  #44",
        "tokenid": 376,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1358.8600000000024,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 110,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 34,
        "MNW": 9523,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 45,
        "nick": "Minion  #45",
        "tokenid": 379,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1017.233000000002,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 104,
        "MNW": 9704,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 46,
        "nick": "  #46",
        "tokenid": 380,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1100.5800000000036,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 51.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 103,
        "MNW": 9791,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 47,
        "nick": "Minion  #47",
        "tokenid": 381,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 983.918999999989,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 102,
        "MNW": 9827,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 48,
        "nick": "  #48",
        "tokenid": 382,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 171,
        "finalscore": "171",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 2279.9999999382944,
                "y": 1294.6457713701232,
                "mN": -8.335999999995693,
                "angle": 4.440092069168817,
                "size": 1.023955375687889
            },
            {
                "x": 2419.599778583658,
                "y": 1162.060648596936,
                "mN": -0.008000000001629815,
                "angle": 1.2393334618112055,
                "size": 1.2254844053969542
            },
            {
                "x": 2292.7690232950613,
                "y": 1240.9442125844864,
                "mN": -0.008999999990919605,
                "angle": 4.901351379399272,
                "size": 1.4179437180675558
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 981.1849999999395,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 46,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 51.5,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 31,
            "mNm": 26
        },
        "nnmnv": 62,
        "MNW": 31110,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 5
    },
    {
        "id": 49,
        "nick": "Minion  #49",
        "tokenid": 383,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 50.137000000000626,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 111,
        "MNW": 8539,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 50,
        "nick": "  #50",
        "tokenid": 384,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 208.57099999999446,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 51,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 85,
        "MNW": 9407,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 51,
        "nick": "  #51",
        "tokenid": 378,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1383.8939999999948,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 48.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 105,
        "MNW": 9668,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 52,
        "nick": "Minion  #52",
        "tokenid": 385,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 100.38599999999678,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 0,
        "MNW": 9443,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 53,
        "nick": "  #53",
        "tokenid": 386,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1358.8600000000024,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 50.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 55,
        "MNW": 9523,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 54,
        "nick": "Minion  #54",
        "tokenid": 387,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1358.8600000000024,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 44,
        "MNW": 9523,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 55,
        "nick": "  #55",
        "tokenid": 388,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 775.534999999998,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 50.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 15,
        "MNW": 9566,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 56,
        "nick": "Minion  #56",
        "tokenid": 389,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1383.8939999999948,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 73,
        "MNW": 9668,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 57,
        "nick": "Minion  #57",
        "tokenid": 395,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 208.57099999999446,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 98,
        "MNW": 9407,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 58,
        "nick": "Minion  #58",
        "tokenid": 254,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 116.86300000000483,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 10,
        "MNW": 9284,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 59,
        "nick": "Minion  #59",
        "tokenid": 377,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 775.534999999998,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 1,
        "MNW": 9566,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 60,
        "nick": "  #60",
        "tokenid": 390,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1017.233000000002,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 51,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 76,
        "MNW": 9704,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 61,
        "nick": "Minion  #61",
        "tokenid": 391,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1100.5800000000036,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 106.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 8,
        "MNW": 9791,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 62,
        "nick": "Minion  #62",
        "tokenid": 392,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 983.918999999989,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 100,
        "MNW": 9827,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 63,
        "nick": "Minion  #63",
        "tokenid": 394,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 50.137000000000626,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 110,
        "MNW": 8539,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 64,
        "nick": "Minion  #64",
        "tokenid": 238,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 0,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 900.2330000000038,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 106.5,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 109.5,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 107,
        "MNW": 9248,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 65,
        "nick": "Minion  #65",
        "tokenid": 239,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 0,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1333.5919999999933,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 106,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 56,
        "MNW": 9248,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 66,
        "nick": "Minion  #66",
        "tokenid": 240,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 0,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1091.9369999999944,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 106,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 57,
        "MNW": 9248,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 67,
        "nick": "Minion  #67",
        "tokenid": 241,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 0,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 425.27600000000166,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 106,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 58,
        "MNW": 9248,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 68,
        "nick": "Minion  #68",
        "tokenid": 249,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1091.8680000000168,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 20,
        "MNW": 9284,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 69,
        "nick": "Minion  #69",
        "tokenid": 282,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1150.1370000000024,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 80,
        "MNW": 9386,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 70,
        "nick": "Minion  #70",
        "tokenid": 244,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 0,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 1027.7,
                "y": 39,
                "mN": -0.001999999993131496,
                "angle": 1.7798283793504133,
                "size": 1.3230185408251118
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 158.63800000000265,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 106,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 109,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 50,
        "MNW": 9248,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 71,
        "nick": "Minion  #71",
        "tokenid": 331,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 391.8969999999972,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 106.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 32,
        "MNW": 9313,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 72,
        "nick": "Minion  #72",
        "tokenid": 246,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1475.0770000000048,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 86,
        "MNW": 9284,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 73,
        "nick": "Minion  #73",
        "tokenid": 292,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 650.1209999999992,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 114,
        "MNW": 8539,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 74,
        "nick": "Minion  #74",
        "tokenid": 256,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1058.5970000000016,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 49,
        "MNW": 9284,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 75,
        "nick": "Minion  #75",
        "tokenid": 242,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 0,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1283.6169999999947,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 106,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 59,
        "MNW": 9248,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 76,
        "nick": "Minion  #76",
        "tokenid": 247,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 383.48500000000786,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 53,
        "MNW": 9284,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 77,
        "nick": "Minion  #77",
        "tokenid": 275,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 350.38599999999497,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 4,
        "MNW": 9350,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 78,
        "nick": "Minion  #78",
        "tokenid": 270,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 41.771999999997206,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 79,
        "MNW": 9350,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 79,
        "nick": "Minion  #79",
        "tokenid": 263,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 42.035999999989144,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 35,
        "MNW": 9313,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 80,
        "nick": "Minion  #80",
        "tokenid": 271,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 350.2730000000156,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 40,
        "MNW": 9284,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 81,
        "nick": "Minion  #81",
        "tokenid": 273,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1033.6620000000003,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 106.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 69,
        "MNW": 9350,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 82,
        "nick": "Minion  #82",
        "tokenid": 274,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1292.018,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 3,
        "MNW": 9350,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 83,
        "nick": "Minion  #83",
        "tokenid": 306,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1300.3809999999903,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 36,
        "MNW": 9313,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 84,
        "nick": "Minion  #84",
        "tokenid": 277,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 942.0700000000033,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 27,
        "MNW": 9350,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 85,
        "nick": "Minion  #85",
        "tokenid": 278,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 300.4109999999964,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 28,
        "MNW": 9350,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 86,
        "nick": "Minion  #86",
        "tokenid": 243,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 0,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 866.9619999999886,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 106,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 60,
        "MNW": 9248,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 87,
        "nick": "Minion  #87",
        "tokenid": 284,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1242.0310000000063,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 93,
        "MNW": 9386,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 88,
        "nick": "Minion  #88",
        "tokenid": 285,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 0.3870000000060827,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 24,
        "MNW": 9386,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 89,
        "nick": "Minion  #89",
        "tokenid": 286,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 558.755000000001,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 66,
        "MNW": 9386,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 90,
        "nick": "Minion  #90",
        "tokenid": 287,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 317.1000000000022,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 5,
        "MNW": 9386,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 91,
        "nick": "  #91",
        "tokenid": 288,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1150.4390000000094,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 48.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 92,
        "MNW": 9386,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 92,
        "nick": "Minion  #92",
        "tokenid": 289,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 808.7880000000041,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 67,
        "MNW": 9791,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 93,
        "nick": "Minion  #93",
        "tokenid": 290,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 692.1269999999895,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 76,
        "MNW": 9827,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 94,
        "nick": "Minion  #94",
        "tokenid": 291,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 1019,
                "y": 420.99999999999994,
                "mN": 0,
                "angle": 5.5323312766065165,
                "size": 1.146347568983206
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 591.2499999999818,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 109.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 18,
        "MNW": 9950,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 95,
        "nick": "Minion  #95",
        "tokenid": 225,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 933.4079999999958,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 97,
        "MNW": 9248,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 96,
        "nick": "Minion  #96",
        "tokenid": 293,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 508.541999999994,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 81,
        "MNW": 9407,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 97,
        "nick": "  #97",
        "tokenid": 294,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1175.3919999999925,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 50.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 7,
        "MNW": 9443,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 98,
        "nick": "Minion  #98",
        "tokenid": 295,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1175.3919999999925,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 65,
        "MNW": 9443,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 99,
        "nick": "Minion  #99",
        "tokenid": 297,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 0,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 408.55699999999706,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": {
            "Wvw": 106,
            "mNm": 26
        },
        "mMw": {
            "Wvw": 108.5,
            "mNm": 31.5
        },
        "MNn": {
            "Wvw": 13.5,
            "mNm": 26
        },
        "nnmnv": 88,
        "MNW": 9248,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 100,
        "nick": "Minion  #100",
        "tokenid": 298,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 774.9519999999975,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 117.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 118,
        "MNW": 8539,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 101,
        "nick": "  #101",
        "tokenid": 300,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1283.5720000000074,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 57,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 46,
        "MNW": 9284,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 102,
        "nick": "Minion  #102",
        "tokenid": 301,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 616.9110000000146,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 117,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 47,
        "MNW": 9284,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 103,
        "nick": "Minion  #103",
        "tokenid": 302,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 774.9519999999975,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 117,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 117,
        "MNW": 8539,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 104,
        "nick": "Minion  #104",
        "tokenid": 303,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 575.0879999999961,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 118,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 51,
        "MNW": 9313,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 105,
        "nick": "Minion  #105",
        "tokenid": 304,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 725.3119999999944,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 117,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 70,
        "MNW": 9313,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 106,
        "nick": "Minion  #106",
        "tokenid": 305,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 42.035999999989144,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 117,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 25,
        "MNW": 9313,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 107,
        "nick": "  #107",
        "tokenid": 276,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 108.73099999999613,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 59.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 26,
        "MNW": 9350,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 108,
        "nick": "Minion  #108",
        "tokenid": 272,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 700.247000000003,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 117.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 22,
        "MNW": 9350,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 109,
        "nick": "Minion  #109",
        "tokenid": 308,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1492.0609999999906,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 117,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 38,
        "MNW": 9313,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 110,
        "nick": "Minion  #110",
        "tokenid": 309,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1075.4059999999845,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 115,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 39,
        "MNW": 9313,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 111,
        "nick": "Minion  #111",
        "tokenid": 310,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 1056,
                "y": 251,
                "mN": -8.328999999997905,
                "angle": 4.8125461456496925,
                "size": 1.633970829997447
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 367.0819999999985,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 112.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 9,
        "MNW": 9313,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 112,
        "nick": "Minion  #112",
        "tokenid": 311,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 891.6610000000001,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 114.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 116,
        "MNW": 8539,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 113,
        "nick": "Minion  #113",
        "tokenid": 312,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1475.2520000000077,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 114.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 48,
        "MNW": 9284,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 114,
        "nick": "Minion  #114",
        "tokenid": 279,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1383.7559999999903,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 115.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 29,
        "MNW": 9350,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 115,
        "nick": "Minion  #115",
        "tokenid": 280,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 675.4320000000043,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 115,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 101,
        "MNW": 9350,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 116,
        "nick": "Minion  #116",
        "tokenid": 281,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 1466.7220000000016,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 114.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 115,
        "MNW": 8539,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 117,
        "nick": "Minion  #117",
        "tokenid": 283,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 908.6160000000091,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 115,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 6,
        "MNW": 9386,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 118,
        "nick": "Minion  #118",
        "tokenid": 299,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 25.227000000006228,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 115,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 45,
        "MNW": 9284,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    },
    {
        "id": 119,
        "nick": "Minion  #119",
        "tokenid": 307,
        "MMm": 0,
        "ghoulmode": 0,
        "mW": 1,
        "finalscore": "0",
        "clan": -1,
        "wwV": 0,
        "VVvWM": 0,
        "Wmv": 0,
        "MNV": 0,
        "whichalert": [],
        "stageofalert": [],
        "mvnvM": 0,
        "NMWMV": 0,
        "text": [],
        "WvWwv": [],
        "MVNWv": [],
        "label": [],
        "mNWvv": [
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            },
            {
                "x": 0,
                "y": 0,
                "mN": 0,
                "angle": 0,
                "size": 0
            }
        ],
        "mNvwv": [
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            },
            {
                "type": 0,
                "x": 0,
                "y": 0,
                "mN": 0,
                "wwMnv": 0,
                "NwVWn": 0
            }
        ],
        "Vw": 633.7199999999975,
        "nn": 0,
        "orientation": 1,
        "NmMVW": 1,
        "mWv": -1,
        "MMvnN": 0,
        "vMNnW": null,
        "mMw": {
            "Wvw": 114.5,
            "mNm": 31.5
        },
        "MNn": null,
        "nnmnv": 37,
        "MNW": 9313,
        "x": 0,
        "y": 0,
        "rx": 0,
        "ry": 0,
        "karmamsg": 0
    }
]

PlayerArray = [[1, 314], [2, 409], [3, 410], [4, 411], [5, 413], [6, 412], [7, 414], [8, 364], [9, 359], [10, 358], [11, 357], [12, 393], [13, 354], [14, 355], [15, 356], [16, 360], [17, 400], [18, 362], [19, 374], [20, 363], [21, 429], [22, 404], [23, 396], [24, 397], [25, 398], [26, 399], [27, 361], [28, 401], [29, 402], [30, 366], [31, 403], [32, 367], [33, 405], [34, 406], [35, 407], [36, 408], [37, 368], [38, 369], [39, 370], [40, 375], [41, 371], [42, 372], [43, 373], [44, 376], [45, 379], [46, 380], [47, 381], [48, 382], [49, 383], [50, 384], [51, 378], [52, 385], [53, 386], [54, 387], [55, 388], [56, 389], [57, 395], [58, 254], [59, 377], [60, 390], [61, 391], [62, 392], [63, 394], [64, 238], [65, 239], [66, 240], [67, 241], [68, 249], [69, 282], [70, 244], [71, 331], [72, 246], [73, 292], [74, 256], [75, 242], [76, 247], [77, 275], [78, 270], [79, 263], [80, 271], [81, 273], [82, 274], [83, 306], [84, 277], [85, 278], [86, 243], [87, 284], [88, 285], [89, 286], [90, 287], [91, 288], [92, 289], [93, 290], [94, 291], [95, 225], [96, 293], [97, 294], [98, 295], [99, 297], [100, 298], [101, 300], [102, 301], [103, 302], [104, 303], [105, 304], [106, 305], [107, 276], [108, 272], [109, 308], [110, 309], [111, 310], [112, 311], [113, 312], [114, 279], [115, 280], [116, 281], [117, 283], [118, 299], [119, 307]]

PlayerCycle = 0
johncena = 0


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        global PlayerCycle
        self.wfile.write(bytes(str(PlayerArray[PlayerCycle]), "utf-8"))  
        if PlayerCycle < 118:
            PlayerCycle = PlayerCycle + 1
        else:
            PlayerCycle = 0
            
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
    
    
webServer = HTTPServer((hostName, serverPort), MyServer)
print("Server started http://%s:%s" % (hostName, serverPort))

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print("Server stopped.")

"""
async def ConnectSrv(ip):
  def on_error(ws, error):
    print(" WS Error - " + error)

  def on_close(ws, close_status_code, close_msg):
    print(" WS Closed " + close_msg + " - " + close_status_code)

  def on_open(ws):
    print(" WS Open: ")
    LoginDevast = '[30,"devastmod0token12345","0",-1,0,"John Galileo",0,0,"OGRj2ktlkH54auuB"]' # Password - LUBduUmaPR3Yn6t
    #[dat, token, tokenid, userid, mNVNV, nick, skin, homescreen.NwnNN, password]
    #print(LoginDevast)
    ws.send(LoginDevast)
    ws.send('[1, "!immortal-on"]')
    ws.send('[1, ""]')

  def on_message(ws, message):
    #ws.close()
    print()
    print()
    print(message)
    print()
    print()

  websocket.enableTrace(True)
  host = "wss://"+ ip +"/"
  ws = websocket.WebSocketApp(host,on_message=on_message,on_error=on_error,on_close=on_close,)
  ws.on_open=on_open
  ws.run_forever()

asyncio.run(ConnectSrv("devast184.devast.io"))

"""
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

null = "null"



NewArray = []

for x in PlayerArray:
  if x['tokenid'] > 0:
    NewArray.append([x['id'], x['tokenid']])

print(NewArray)

client = commands.Bot(
    command_prefix='-',
    help_command=None,
    intents = intents
)

@client.command()
async def hello(ctx):
  await ctx.send('Hello!')
  print(PlayerArray[1])

@client.command()
async def ak(ctx):
  print(arg)
  #await ConnectSrv("devast192.devast.io")
    
client.run(
  'MTAxMDI0Njg1NjA1NzU3MzQ1Nw.GuP4HB.DJhPdUR8CS1h55Y7z6u2SBgfocnAfe9JQoX0iU'
)

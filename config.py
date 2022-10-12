"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "8934899"))
        self.API_HASH: str = os.environ.get("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
        self.SESSION: str = os.environ.get("SESSION", "AgCIVfMAxxD1wVnUo6Q31f_P3nP4KUBPUW7strBYewZoYT7R8Hqod_xyDKUnwGZZLkX-_8B_AW5uDLad5pt6STIPtiz4FIYo6rFoqVF-kTgxMAqRyRfCKCrzKB4kEiK3nXPl7LtJSy0FXZGaG5WDEjUolNuSZKFJ66cHonFn1i1z9-_r1pdjDta3rchthoUo0-Qd4UI0LM0TyX0m1AZ8lrBuGNFsbXvdisHvahbzpCbg7ufd1b5rfFlFwwFfOFe6jgtAjOYH4Jiyu2mY689MDxGmV_j2BSOGhxfb_nZTPgsR4E_qZjL8sCfsk8e-oZAUg-hcwMCfqY1L8GqnGsQcCScL7KfelQAAAAE-aiueAA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "5774874510:AAEWKQQGYkDvLyOdOP4q7VQB334oUp-t4Qc")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "1854384004").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()

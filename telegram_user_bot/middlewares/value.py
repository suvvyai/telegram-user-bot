from typing import Any

from pyrogram_patch.middlewares.middleware_types import OnUpdateMiddleware
from pyrogram_patch.middlewares import PatchHelper


class ParamValueMiddleware(OnUpdateMiddleware):
    def __init__(self, key: str, value: Any) -> None:
        self.value = value
        self.key = key

    async def __call__(self, update, client, patch_helper: PatchHelper):
        patch_helper.data[self.key] = self.value

from __future__ import annotations

from typing import Any, Dict, List, Optional

from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from .config import MODEL, OPENAI_API_KEY
from .prompts import SYSTEM_PROMPT
from .tools import fetch_and_extract


class NandaAgent:
    """Trust-first explainer agent orchestrated for the NANDA adapter."""

    def __init__(self) -> None:
        if not OPENAI_API_KEY:
            raise RuntimeError("OPENAI_API_KEY not set")
        self.llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=MODEL, temperature=0.2)

    async def run(self, messages: List[Dict[str, Any]]) -> str:
        """Execute the agent against a NANDA-formatted message history."""
        user_text: Optional[str] = None
        last_user_index: Optional[int] = None
        for idx, message in enumerate(messages):
            if message.get("role") == "user":
                user_text = message.get("content", user_text)
                last_user_index = idx

        url: Optional[str] = None
        if user_text:
            import re

            match = re.search(r"(https?://\S+)", user_text)
            if match:
                url = match.group(1)

        fetched = ""
        if url:
            fetched = await fetch_and_extract(url)

        prompt_blocks: List[SystemMessage | HumanMessage | AIMessage] = [
            SystemMessage(content=SYSTEM_PROMPT)
        ]

        for idx, message in enumerate(messages):
            role = message.get("role")
            content = message.get("content", "")
            if role == "system":
                continue
            if role == "assistant":
                prompt_blocks.append(AIMessage(content=content))
            elif role == "user":
                if fetched and idx == last_user_index:
                    prompt_blocks.append(
                        HumanMessage(content=f"Fetched content from {url}:\n{fetched}")
                    )
                prompt_blocks.append(HumanMessage(content=content))

        response = await self.llm.ainvoke(prompt_blocks)
        return response.content

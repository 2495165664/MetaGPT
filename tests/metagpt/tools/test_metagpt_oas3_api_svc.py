#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/12/26
@Author  : mashenquan
@File    : test_metagpt_oas3_api_svc.py
"""
import asyncio
import subprocess
from pathlib import Path

import pytest
import requests


@pytest.mark.asyncio
async def test_oas2_svc():
    script_pathname = Path(__file__).parent / "../../../metagpt/tools/metagpt_oas3_api_svc.py"
    process = subprocess.Popen(["python", str(script_pathname)])
    await asyncio.sleep(5)

    url = "http://localhost:8080/openapi/greeting/dave"
    headers = {"accept": "text/plain", "Content-Type": "application/json"}
    data = {}
    response = requests.post(url, headers=headers, json=data)
    assert response.text == "Hello dave\n"

    process.terminate()


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
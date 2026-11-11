from time import perf_counter

import httpx


async def check_service(url):
    async with httpx.AsyncClient() as client:
        result = {
            "is_up": False,
            "status_code": None,
            "response_time_ms": None,
            "error": None,
        }
        timeout = httpx.Timeout(5.0)
        start_time = perf_counter()
        try:
            response = await client.get(url, timeout=timeout)
            result["status_code"] = response.status_code
            if 200 <= response.status_code <= 399:
                result["is_up"] = True
        except httpx.ConnectError:
            result["error"] = "Connection failed"
        except httpx.TimeoutException:
            result["error"] = "Request timed out"
        finally:
            end_time = perf_counter()
            elapsed_time = (end_time - start_time) * 1000
            elapsed_time_ms = round(elapsed_time, 2)
            result["response_time_ms"] = elapsed_time_ms
        return result

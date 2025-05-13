# async_agents.py

import asyncio
import random

async def interpreter_agent(input_text: str) -> str:
    # Simulate asynchronous input interpretation
    await asyncio.sleep(random.uniform(0.1, 0.3))
    interpreted = input_text.lower().strip()
    return interpreted

async def preprocessor_agent(interpreted_text: str) -> list:
    # Simulate asynchronous preprocessing
    await asyncio.sleep(random.uniform(0.1, 0.3))
    tokens = interpreted_text.split()
    return tokens

async def core_model_agent(tokens: list) -> str:
    # Simulate asynchronous model generation
    await asyncio.sleep(random.uniform(0.2, 0.5))
    return " ".join(tokens) + " [generated motion]"

async def monitor_agent(output_text: str) -> bool:
    # Simulate asynchronous monitoring
    await asyncio.sleep(random.uniform(0.1, 0.2))
    if "error" in output_text:
        return False
    return True

async def secure_generation_async(raw_input: str) -> str:
    interpreted = await interpreter_agent(raw_input)
    print(f"Interpreter Agent Output: {interpreted}")
    
    tokens = await preprocessor_agent(interpreted)
    print(f"Pre-Processor Agent Output: {tokens}")
    
    model_output = await core_model_agent(tokens)
    print(f"Core Model Agent Output: {model_output}")
    
    is_safe = await monitor_agent(model_output)
    if not is_safe:
        raise RuntimeError("Monitor Agent flagged the output as suspicious!")
    
    print("Monitor Agent: Output verified as safe.")
    return model_output

if __name__ == "__main__":
    raw_input_text = "Test input for asynchronous multi-agent security."
    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(secure_generation_async(raw_input_text))
        print(f"Final Asynchronous Output: {result}")
    except Exception as e:
        print(f"Security check failed: {e}")
    finally:
        loop.close()

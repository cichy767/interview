import time
import asyncio


async def brew_coffe():
    print("start brew_coffe")
    await asyncio.sleep(3)
    print("end brew_coffe")
    return "Coffe ready"


async def toast_bagel():
    print("start toast_bagel")
    await asyncio.sleep(2)
    print("end toast_bagel")
    return "toast bagel ready"


async def main():
    start_time = time.time()
    batch = asyncio.gather(brew_coffe(), toast_bagel())
    result_coffe, result_toast = await batch

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(
        f"result_coffe: {result_coffe} "
        f"result_toast: {result_toast} "
        f"elapsed_time: {elapsed_time:.2f} seconds"
    )


if __name__ == "__main__":
    asyncio.run(main())

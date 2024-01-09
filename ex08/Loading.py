import time

def ft_tqdm(lst):
    total = len(lst)
    start_time = time.time()
    for i, item in enumerate(lst):
        yield item
        progress = i + 1
        elapsed_time = time.time() - start_time
        eta = elapsed_time * (total / progress - 1) if progress > 0 else 0
        # Customize the progress bar format as desired
        percentage = progress / total * 100
        print(f"\r{percentage:.0f}")
        # print(f"\rProgress: {progress}/{total} - ETA: {eta:.2f}s", end="")

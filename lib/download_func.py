import requests, time, sys

def DownloadFile(fileUrl):
    fileResponse = requests.get(fileUrl, stream=True)
    getFileName = fileResponse.url.split("/")[-1]
    downloaded = 0
    total_length = fileResponse.headers.get("Content-Length")
    start = time.perf_counter()
    with open(getFileName, "wb") as file:
        if total_length is None:
            f.write(fileResponse.content)
        else:
            for chunk in fileResponse.iter_content(1024):
                downloaded += len(chunk)
                file.write(chunk)
                done = int(30 * downloaded / int(total_length))
                cursor = "=" * done
                cursor_remain = " " * (30 - done)
                pct_downloaded = downloaded / int(total_length) * 100
                speed = downloaded // (time.perf_counter() - start) / 100000
                downloaded_size = downloaded / 1e+6
                sys.stdout.write(f"\r[{cursor}{cursor_remain}] {speed: .1f} Mbps, Downloaded {pct_downloaded: .2f}%, {downloaded_size: .2f}")
    return True
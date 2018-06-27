from urllib import request

sample = 'https://www.sample-videos.com/text/Sample-text-file-10kb.txt'


def download_stock_data(txt_url):
    response = request.urlopen(txt_url)
    txt = response.read()
    filename = 'sample.txt'
    with open(filename, "wb") as f:
        f.write(txt)
    with open(filename, 'r') as fx:
        processed_text = fx.read()
    processed_text = processed_text.split(" ")

    print(len(processed_text))


download_stock_data(sample)

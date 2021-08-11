import requests

def main():

    url_data = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
    url_description = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names'
    url_test_data = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test'

    urls = [url_data, url_description, url_test_data]

    for url in urls:
        r = requests.get(url)
        if url.endswith('data'):
            open('data/adult.data', 'wb').write(r.content)
        elif url.endswith('names'):
            open('data/adult.names', 'wb').write(r.content)
        elif url.endswith('test'):
            open('data/adult.test', 'wb').write(r.content)
        else:
            raise ValueError


if __name__ == "__main__":
    main()
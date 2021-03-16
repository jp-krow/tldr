# 🎨 TL;DR

TL;DR (Too long didn't read) is a service to summarize text with a given website.

## 📌 Installation

Install requirements in `requirements.txt` with pip

```bash
pip install -r requirements.txt
```

Then load up your favorite python IDE and run `main.py`, or use your terminal

```bash
python main.py
```

## 📝 Usage

Send a `POST` request to the local flask application in page `/sum` with the following:
```
site-language=english
url=[your url here]
sentences=5
cached=true
```

## 🔖 More Information

`site-language` is the language the selected website uses, changing this to another language may mess up the summarization.

`url` is your chosen url.

`sentences` (Optional) tells how much sentences you want to receive back (Defaults to 10 if not provided.)

`cached` (Optional) enables or disables google's cached save of the url (useful if the website has anti-bot measures in place, or keep receiving an error.)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MPL-2.0](https://www.mozilla.org/en-US/MPL/2.0)

# get-quotes

A couple python scripts to gather all types of quotes (mainly anime) from various sites and puts them into a json file. I use it for getting a database of quotes for applications, as well as for typing practise.

The quotes are stored in a json file named `quotes.json` in the following format:

```json
[
  {
    "author": "Author of the quote",
    "title": "Where the quote is from",
    "text": "The quote",
    "id": 123
  },
  ...
]
```

`id` is an one-based integer, providing a unique identifier for retrieving quotes for other applications.

Note that the `quotes.json` file will be *overriden* each time one of the scripts are run. Make sure to move or rename the file if you want to keep the quotes.

A rough approximation of the number of quotes each script will return is given below.

#### Sites:

All credit for quotes goes to these sites.

- `lessreal.py` - www.less-real.com: ~8600 anime quotes


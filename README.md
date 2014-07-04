#mailWS [![Build Status](https://secure.travis-ci.org/chrisenytc/mail-ws.png?branch=master)](http://travis-ci.org/chrisenytc/mail-ws) [![GH version](https://badge-me.herokuapp.com/api/gh/chrisenytc/mail-ws.png)](http://badges.enytc.com/for/gh/chrisenytc/mail-ws)

> An simple implementation of a mail web service

## Getting Started

1º Clone mail-ws repo

```bash
git clone https://github.com/chrisenytc/mail-ws.git
```

2º Enter in mail-ws directory
```bash
cd mail-ws
```

3º Install dependencies

if you no have virtualenv installed. Install it.

```bash
sudo apt-get install python-virtualenv
```

```bash
virtualenv venv --no-site-packages
```

```bash
source venv/bin/activate
```

```bash
make install
```

4º Configure the settings in `api/config`

5º Run mail-ws

```bash
make start
```

Test your mail-ws app

```bash
make test
```

For more information about mongoengine, see documentation [here](http://docs.mongoengine.org/)

## Contributing

See the [CONTRIBUTING Guidelines](CONTRIBUTING.md)

## Support
If you have any problem or suggestion please open an issue [here](https://github.com/chrisenytc/mail-ws/issues).

## License

Copyright (c) 2014, Christopher EnyTC

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
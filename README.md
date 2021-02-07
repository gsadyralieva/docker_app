# Simple Flask App -Docker

Simple app built on Python Flask.

### Prerequisites

* Linux Server

* Python3.8

* Python pip

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

## Usage
Clone Repository:

```bash
git clone https://github.com/gsadyralieva/docker_app.git
```

Change working directory:
```bash
cd docker_app
```

Install requirements:
```bash
pip3 install -r app/requirements.txt
```

Run Application:
```bash
python3.8 app/src/server.py
```
## Docker Image Build

Build Image
```bash
docker image build -t <your-tag> .
```
Push Image
```bash
docker image push <your-image>
```
## Run Container
```bash
docker conatiner run -d --name sampleapp -p <hostport>:5000  <your-image-name>
```

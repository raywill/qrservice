## Intro

A micro json service to decode QR

## Install

Barcode reader
```
yum install zbar.x86_64
```

Flask Web Framework

```
pip install flask
```

## Samples

```
curl -x reactshare.cn:8000 -F "file=http://reactshare.cn/tracelog/IMG_1956.JPG" http://reactshare.cn:8000/upload
curl -x reactshare.cn:8000 -F "file=@sample.jpg" http://reactshare.cn:8000/upload
```

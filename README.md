# Yolov8 Advance Speed Estimation
Herkese merhabalar, bugün Yolov8 ile ileri seviye hız tespiti uygulaması gerçekleştireceğiz. 

<img src="./resimler/resim_1.png" alt="Yolov8 ile Hız Tahmini" width="1280">

Daha önce Yolov8 ile nesne tespiti uygulaması gerçekleştirdiyseniz ultralytics ile birkaç satırda bu işi halledebildiğinizi görmüşsünüzdür. Peki bunun arka planını hiç merak ettiniz mi?
İşte biz de OpenYTU ekibi olarak kendi hız ve yön tespitini içeren kütüphanelerimizi yazdık. Sadece üç satırda yani:

```shell

import Tracker
tracker = Tracker()
frame = tracker(model, frame)

```

İlgili satırlarla hız tespiti yaptık. İşte sanki ultralyticsin hız tespit metodu baştan yazılmış gibi :)
Repomuzu açık kaynak olarak sizinle paylaşıyoruz. Haydi yazılımı çalıştırmak için öncelikle repomuzu klonlayalım:

```shell

git clone https://github.com/openytu/Yolov8_advance_speed_estimation

```

Adrese gidelim

```shell

cd Yolov8_advance_speed_estimation

```


Son olarak gelin kodumuzu çalıştıralım


```shell

python main.py
```

Yeni projelerde görüşmek üzere :)


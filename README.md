# FiGoCo

This is a [FIJI](https://fiji.sc) plugin which will give you the possibility to run a Deep Learning pretrained Keras model in the cloud (using Google Colaboratory as backend and its free GPU solution) directly from FIJI. The main advantages resides in the fact that absolutely no installation is required for the user except for this plugin installation.

### Installation

1) Download and Install [Fiji](https://imagej.net/Fiji/Downloads) and copy the __FiGoCo__ directory directly into your Fiji/Plugins repository (once done, restart Fiji)
2) Create a [NGROK account](https://ngrok.com/) to generate a __token__
3) If you don't already have one, please create a [Gmail account](https//www.google.com/gmail)

and that's it !

### Run the FiGoCo plugin

In order to proper run the FiGoCo plugin, you need to have 2 files:
1) Your pretrained Keras Model (*.h5)
2) Your "homemade" Python __prediction.py__ script which will be run on the server to make the predictions using your model

And then you are ready to start:
1) Open Fiji/Plugin/FiGoCo Menu and select __Setup Server__ : A Google Colaboratory Notebook will popup
2) Run the __Start__ cell to start the creation of the server
3) Once running, a prompt ask you to provide your __NGROK token__, please do so
4) Once the cell finish, it should display a message giving your the address of your server and the port (XXXX)
```
SSH : http:\\0.tcp.ngrok.io:XXXX
```


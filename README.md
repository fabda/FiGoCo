# FiGoCo (Fiji Google Colab)

Deploying and running pretained Deep Learning model on user desktop is often a nightmare an unpleasant for non IT users (frameworks installation, hardware driver, versionning ...).

The goal of this [FIJI](https://fiji.sc) Jython plugin is to facilitate the deployment and the access to your pretrained Deep Learning model using only FIJI as user interface and [Google Colaboratory](https://colab.research.google.com/) cloud environment as background computing ressources (free CPU/GPU/TPU solution): No framework installation, no hardware requirement for high speed computing on the user machine.

You want to give it a try ? Just download __FiGoCo__ from this repo and start following the instructions below :)

### 0) Train a Deep Learning model using Keras

![alt text](https://raw.githubusercontent.com/fabda/FiGoCo/master/images/step1.png)

Could be on your local machine, on the cloud, anywhere. The only condition to meet FiGoCo requirement is to have at the end of your training:
- a trained __model__ saved into HDF5 formation (Keras compliant)
- a Python script __predict.py__ able to run your model (see __demos/predict.py__ on this repo to have an example)

### 1) Fiji & FiGoCo Plugin Installation

1. In case you don't have Fiji installed on your computer, you can download the last version of Fiji website [here](https://imagej.net/Fiji/Downloads)
2. Clone this repo and copy the __FiGoCo__ directory directly into your Fiji/Plugins repository (once done, restart Fiji)
This directory contains two files :
- *Setup_server.py* which will setup and start the FiGoCo server on Google Colaboratory
- *Run_model.py* which will connect to your FiGoCo server, run your model on the user image and send back the results to the user.

Before running this scripts, you need to complete the following step below.

### 2) Create or use an NGROK Token

![alt text](https://raw.githubusercontent.com/fabda/FiGoCo/master/images/step2.png)

The purpose of this step will be to open a tunnel between FIJI and the FiGoCo server. One popular way of doing this is to use __ngrok__:

- In case you don't have an ngrok account, please create a free one on [ngrok website](https://ngrok.com), generate a __authtoken__ and copy it somewhere because you will need it later.
- In case you already have an ngrok accoung, just copy your __authtoken__ somewhere because you will need it later.

Once your token is generated, you'll never need to redo this step: you will reuse it each time you need it to start a FiGoCo server.

### 3) FiGoCo plugin : Setup Server

![alt text](https://raw.githubusercontent.com/fabda/FiGoCo/master/images/step3.png)

1. Open Fiji/Plugin/FiGoCo Menu and select __Setup Server__ : A Google Colaboratory Notebook will popup. 
2. Run the __Start__ cell to start the creation of the server 
3. Once running, a prompt ask you to provide your __NGROK token__, please do so
4. The cell finished its execution by showing a message giving your the address of your server and its port (XXXX)
```
SSH : http:\\0.tcp.ngrok.io:XXXX
```
5. Go Back to Fiji FiGoCo "Setup Server" window and fill the __NGROK server address and port__ and click OK
6. Select your Keras models (*.h5) from your local computer and click OK
7. Select your Python prediction.py script from your local computer and click OK
8. Wait everything is upload to the server ... and your server is ready to process your images

#### Part 2 : FiGoCo plugin : Run Model

![alt text](https://raw.githubusercontent.com/fabda/FiGoCo/master/images/step4.png)

1. Open Fiji/Plugin/FiGoCo Menu and select __Run_model__
2. Provide again the __NGROK server address and port__ and click OK
3. Select your image file (or stack) to process and click OK
4. Wait some minutes (depending of the file size and model execution) and you should see the result appear into a Fiji Window

## Demo

A Demo model has been trained on the Electron Microscopy Dataset from [EPFL](https://www.epfl.ch/labs/cvlab/data/data-em/) using Keras.

In order to run the Demo, you must download the 3 following file:

- Trained Keras model (HDF5 format \*.h5): [here](https://drive.google.com/uc?export=download&id=1490iIpziiom7g36YluBHlzEGCtaKPjb1)
- The Demo Image (TIF stack \*.tif): [here](https://drive.google.com/uc?export=download&id=1ToeUXtgx_tyexcO78CKYaZwooUjbDb4U)
- The Python prediction script (\*.py) : [here](https://drive.google.com/uc?export=download&id=1I_NuHm1Jv4dR4cktcWPoRbab2zZZOBnc)





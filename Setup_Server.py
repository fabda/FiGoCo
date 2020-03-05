from com.jcraft.jsch import JSch
from java.lang import System
import os
import time
from ij.gui import GenericDialog
from fiji.util.gui import GenericDialogPlus
from ij import IJ

from java.awt import Desktop
from java.net import URI

desktop = Desktop.getDesktop()
uri = URI("https://colab.research.google.com/drive/1PRgFZnd0OtT6p61Ce2y0POEoKPNtTE5N#scrollTo=uU-B_7MwFohd") #test url
desktop.browse(uri)


session = None
channel = None

DIALOG = True

if (not DIALOG):
	# ---------------- GLOBAL PARAMETERS --------------------
	HOST = "0.tcp.ngrok.io"
	PORT = 12174
	LOCAL_MODEL_FILENAME    = "C:\\Users\\daian\\Desktop\\Blob\\blob_model.h5"
	LOCAL_IMAGE_FILENAME    = "C:\\Users\\daian\\Desktop\\Blob\\raw\\Blob_test.tif"
	LOCAL_PREDICTION_SCRIPT = "C:\\Users\\daian\\Desktop\\Blob\\prediction.py"
	LOCAL_RESULT_FILENAME   = "C:\\Users\\daian\\Desktop\\results.tif"
	# --------------------------------------------------------
if (DIALOG):
	# ----------------- DIALOG TO FILL GLOBAL PARAMETERS -----

	gui = GenericDialog("Parameters")
	gui.addStringField("NGROK Server address :", "0.tcp.ngrok.io")
	gui.addStringField("PORT :", "")
	gui.showDialog()
	HOST = gui.getNextString()
	PORT = int(gui.getNextString())

	gui = GenericDialogPlus("Parameters")
	gui.addFileField("Select a model file in Keras format (*.h5) : ", "")
	gui.showDialog()
	if gui.wasOKed():
	    LOCAL_MODEL_FILENAME   = gui.getNextString()

	gui = GenericDialogPlus("Parameters")
	gui.addFileField("Select a python script file to upload on the server (*.py)  : ", "")
	gui.showDialog()
	if gui.wasOKed():
	    LOCAL_PREDICTION_SCRIPT   = gui.getNextString()


jsch=JSch()

# SSH Connection to DeepLearning server
IJ.log("-- Connection to Deep Learning Server")
time0 = time.time()
session=jsch.getSession("root", HOST, PORT);
session.setPassword("12345");
session.setConfig("StrictHostKeyChecking", "no");
session.connect();
IJ.log("Execution Time : " + str(time.time()-time0) +" seconds")


# Install all necessary python packages
if (True):
	command = "pip3 install -U segmentation-models tifffile"
	channel=session.openChannel("exec");
	channel.setCommand(command);
	channel.setInputStream(None);
	channel.setErrStream(System.err);
	instream=channel.getInputStream();
	IJ.log("-- Installing necessary python libraries on the server ...")
	channel.connect();
	time0 = time.time()
	while (not channel.isClosed()):
		time.sleep(1)
	channel.disconnect()
	IJ.log("Execution Time : " + str(time.time()-time0) +" seconds")

# Upload the model
if (True):
	channel = session.openChannel("sftp")
	channel.connect()
	IJ.log('-- Uploading model to server ... please wait')
	channel.put(LOCAL_MODEL_FILENAME, "/content/model.h5");
	IJ.log('Done !')

if (True):
	# Upload the prediction python script
	channel = session.openChannel("sftp")
	channel.connect()
	IJ.log('-- Uploading Prediction Python Script to server ... please wait')
	channel.put(LOCAL_PREDICTION_SCRIPT, "/content/prediction.py",channel.OVERWRITE);
	IJ.log('Done !')

channel.disconnect()
session.disconnect()

IJ.log('Server is now ready, please run the "Run model" script to process your image !')	



from com.jcraft.jsch import JSch
from java.lang import System
import os
import time
from ij.gui import GenericDialog
from fiji.util.gui import GenericDialogPlus
from ij import IJ




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
	gui.addFileField("Select an input file (*.tif) : ", "")
	gui.showDialog()
	if gui.wasOKed():
	    LOCAL_IMAGE_FILENAME   = gui.getNextString()

	LOCAL_RESULT_FILENAME = LOCAL_IMAGE_FILENAME+"_prediction.tif"



jsch=JSch()

# SSH Connection to DeepLearning server
IJ.log("-- Connection to Deep Learning Server")
time0 = time.time()
session=jsch.getSession("root", HOST, PORT);
session.setPassword("12345");
session.setConfig("StrictHostKeyChecking", "no");
session.connect();
IJ.log("Execution Time : " + str(time.time()-time0) +" seconds")




if (True):
	#Download results
	channel = session.openChannel("sftp")
	channel.connect()
	IJ.open(LOCAL_IMAGE_FILENAME)
	IJ.log("Opening : " + LOCAL_IMAGE_FILENAME)
	IJ.log('-- Uploading image to server ... please wait')
	channel.put(LOCAL_IMAGE_FILENAME, "/content/toprocess.tif");
	IJ.log('Done !')


if (True):
	# Run the prediction script
	command = "python3 /content/prediction.py > /content/log.txt"
	channel=session.openChannel("exec");
	channel.setCommand(command);
	channel.setInputStream(None);
	channel.setErrStream(System.err);
	instream=channel.getInputStream();
	IJ.log("-- Running prediction on server ...")
	channel.connect();
	time0 = time.time()
	while (not channel.isClosed()):
		time.sleep(1)
	channel.disconnect()
	IJ.log("Execution Time : " + str(time.time()-time0) +" seconds")

		

if (True):
	#Download results
	channel = session.openChannel("sftp")
	channel.connect()
	IJ.log('-- Downloading results from server ... please wait')
	channel.get("/content/results.tif", LOCAL_RESULT_FILENAME);
	IJ.log('Done !')
	IJ.open(LOCAL_RESULT_FILENAME)

if (True):
	# Delete predictions image
	command = "rm -f /content/results.tif"
	channel=session.openChannel("exec");
	channel.setCommand(command);
	channel.setInputStream(None);
	channel.setErrStream(System.err);
	instream=channel.getInputStream();
	IJ.log("-- Cleaning server ...")
	channel.connect();
	time0 = time.time()
	while (not channel.isClosed()):
		time.sleep(1)
	channel.disconnect()
	IJ.log("Execution Time : " + str(time.time()-time0) +" seconds")


channel.disconnect()
session.disconnect()


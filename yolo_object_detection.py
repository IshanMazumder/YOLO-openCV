#Download --> yolov3.cfg , yolov3.weights, coco.names
import cv2
#load object
net = cv.dnn.readNet("yolov3.weights","yolov3.cfg")
classes = []
with open ("coco.names", "r") as f:
	classes = [line.strip() for line in f.readlines()]

layers_names = net.getLayerNames()
output_layers = [layers_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Loading Image
img = cv.imread("path")
img = cv.resize(img, none, fx=0.4, fy=0.4)
height, width, channels = img.shape
# convert to blob - to get the feature from the algo
blob = cv2.dnn.blobFromImage(img, 0.00392, (416,416),(0,0,0), true, crop = False)


class_ids = []
confidences = []
boxes = []

# lets check whats inside blob
net.setInput(blob)
outs = net.forward(output_layers)

# showing info about detected objects
for out in outs:
	for detection in out:
		scores = detection[5:]
		class_id = np.argmax(score)
		confidence = scores[class_id]
		if confidence > 0.5:
			center_x = int(detection[0] * width)
			center_y = int(detection[1] * height)
			w = int( detection[2] * width)
			h = int(detection[3] * height)
			# rectangle co ordinates
			x = int(center_x - w/2)
			y = int(center_y - h/2)
			
			boxes.append([x,y,w,h])
			confidences.append(float(confidence))
			class_ids.apprnd(class_id)

indexes = cv.dnn.NMSBoxes(boxes, confidences,0.5,0.4)

for i in range(len(boxes)):
	x,y,w,h = boxes[i]
	if i in indexes:
	`	labels = classes[class_ids[i]]
		cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
	
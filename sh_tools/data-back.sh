rm /data1/renyu/data/coco -r

mkdir /data1/renyu/data/coco
# mkdir /data1/renyu/data/coco/annotations
# mkdir /data1/renyu/data/coco/train2017
# mkdir /data1/renyu/data/coco/val2017

unzip /data1/renyu/data/coco-bp/train2017.zip -d /data1/renyu/data/coco
unzip /data1/renyu/data/coco-bp/val2017.zip -d /data1/renyu/data/coco
unzip /data1/renyu/data/coco-bp/annotations_trainval2017.zip -d /data1/renyu/data/coco
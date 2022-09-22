"""for  X跨域蒸馏
-train: voc全(train.txt+val.txt)
-val: coco(5k, 仅voc类别)
-coco的类别名和类别id转成voc的

"""
import argparse, os

def parse_args():
    parser = argparse.ArgumentParser(description='Train a detector')
    parser.add_argument('--coco_src', help='the source dir of coco')
    parser.add_argument('--voc07_src', help='the source dir of voc')
    parser.add_argument('--voc12_src', help='the source dir of voc')
    parser.add_argument(
        '--cocovocx',default='data/cocovoc', help='dir of the mixed data')
    
    args = parser.parse_args() 
    return args


def mv_voc07_2coco(voc07_src,cocovocx):
    """
    把voc07的train和val的图片放入 coco 的train2017
    -train.txt 得到image_id eg.2008_000008  str
    -ann_dic['images'][i]['filename'][-15:-4] 得到 2008_000008
    """
    
    #pascal_voc.py: 生成voc12_train.json  voc12_val.json
    os.system('python tools/dataset_converters/pascal_voc.py '+voc07_src+' '+'-o '+cocovocx+'/annotations/  '+'--out-format  coco')

    jpg_root=voc07_src+'/VOC2007/JPEGImages/'
    jpg_des_train=cocovocx+'/train2017/'
    # jpg_des_val=cocovoc+'/val2017/'
    voc_train=open(voc07_src+'/VOC2007/ImageSets/Main/train.txt')
    voc_val=open(voc07_src+'/VOC2007/ImageSets/Main/val.txt')

    lines_train=voc_train.readlines()
    # print(lines_train[0],type(lines_train[0]))
    lines_val=voc_val.readlines()
    for line in lines_train:
        os.system('ln -s '+jpg_root+line[:-1]+'.jpg  '+jpg_des_train)
    for line in lines_val:
        os.system('ln -s '+jpg_root+line[:-1]+'.jpg  '+jpg_des_train)

def mv_voc12_2coco(voc12_src,cocovocx):
    """
    把voc12的train和val的图片放入 coco 的train2017
    -train.txt 得到image_id eg.2008_000008  str
    -ann_dic['images'][i]['filename'][-15:-4] 得到 2008_000008
    """
    
    #pascal_voc.py: 生成voc12_train.json  voc12_val.json
    os.system('python tools/dataset_converters/pascal_voc.py '+voc12_src+' '+'-o '+cocovocx+'/annotations/  '+'--out-format  coco')

    jpg_root=voc12_src+'/VOC2012/JPEGImages/'
    jpg_des_train=cocovocx+'/train2017/'
    # jpg_des_val=cocovoc+'/val2017/'
    voc_train=open(voc12_src+'/VOC2012/ImageSets/Main/train.txt')
    voc_val=open(voc12_src+'/VOC2012/ImageSets/Main/val.txt')

    lines_train=voc_train.readlines()
    print(lines_train[0],type(lines_train[0]))
    lines_val=voc_val.readlines()
    for line in lines_train:
        os.system('ln -s '+jpg_root+line[:-1]+'.jpg  '+jpg_des_train)
    for line in lines_val:
        os.system('ln -s '+jpg_root+line[:-1]+'.jpg  '+jpg_des_train)


def mv_voc2cocovocx(voc_src,cocovocx):
    """
    把voc的train和val的图片都放入 cocovocx 的train2017
    -train.txt 得到image_id eg.2008_000008  str
    -ann_dic['images'][i]['filename'][-15:-4] 得到 2008_000008
    """
    
    #pascal_voc.py: 生成voc12_train.json  voc12_val.json
    os.system('python tools/dataset_converters/pascal_voc.py '+voc_src+' '+'-o '+cocovocx+'/annotations/  '+'--out-format  coco')

    jpg_root=voc_src+'/VOC2012/JPEGImages/'
    jpg_des_train=cocovocx+'/train2017/'
    jpg_des_val=cocovocx+'/train2017/'
    voc_train=open(voc_src+'/VOC2012/ImageSets/Main/train.txt')
    voc_val=open(voc_src+'/VOC2012/ImageSets/Main/val.txt')

    lines_train=voc_train.readlines()
    print(lines_train[0],type(lines_train[0]))
    lines_val=voc_val.readlines()
    for line in lines_train:
        os.system('ln -s '+jpg_root+line[:-1]+'.jpg  '+jpg_des_train)
    for line in lines_val:
        os.system('ln -s '+jpg_root+line[:-1]+'.jpg  '+jpg_des_val)

def mv_coco2cocovocx(coco_src, cocovocx):
    '''选择5k jpgs
    -从val2017中选择5k
    -仅voc类别
    '''

    ann_root_val= coco_src+'/annotations/instances_val2017.json'
    jpg_root_val= coco_src+'/val2017/'

    import json,os,random,copy
    ann_val=open(ann_root_val)
    ann_dic_val=json.load(ann_val)

    #--------------软链接json-------------
    os.system('cp '+coco_src+'/annotations/instances_val2017.json    '+cocovocx+'/annotations/')
    
    #------val: 5k 张图片-----
    jpg_list_val=os.listdir(jpg_root_val)
    # jpg_list_val=random.sample(jpg_list_val,5000)
    print('---all jpgs from coco-val:',len(jpg_list_val),jpg_list_val[:10])
    jpg_ids_val=[]
    for item in jpg_list_val:
        jpg_ids_val.append(int( item[:-4] ) )
        os.system('ln -s '+coco_src+'/val2017/'+item+'  '+cocovocx+'/val2017/')
    
    #------val: 处理json文件-----
    ann_dic_tmp_val={}
    ann_dic_tmp_val.update({'info':ann_dic_val['info']})
    ann_dic_tmp_val.update({'licenses':ann_dic_val['licenses']})
    # imgs_list_val=[]
    ann_list_val=[]

    # for i in range(len(os.listdir(jpg_root_val))):
    #     if ann_dic_val['images'][i]['id'] in jpg_ids_val:
    #         imgs_list_val.append(ann_dic_val['images'][i])
    for i in range(len(ann_dic_val['annotations'])):
        if ann_dic_val['annotations'][i]['image_id'] in jpg_ids_val:
            ann_list_val.append(ann_dic_val['annotations'][i])
    
    ann_dic_tmp_val.update({'images':ann_dic_val['images']})
    ann_dic_tmp_val.update({'annotations':ann_list_val})
    ann_dic_tmp_val.update({'categories':ann_dic_val['categories']})
    ann_out_val=open(cocovocx+'/annotations/instances_val2017.json','w')
    ann_out_val.write(json.dumps(ann_dic_tmp_val, indent=4))

def remap_coco_cls(cocovocx):
    """
    删减coco的类别
    需要改json文件的annotations的category_id 和 categories的id
    """
    import json

    f_coco=open(cocovocx+'/annotations/instances_val2017.json')

    ann_dic_coco=json.load(f_coco)

    dic1={
        "supercategory" : "indoor" ,
        "id": 91,
        "name" : "sofa"
    }
    dic2={
        "supercategory" : "indoor" ,
        "id": 92,
        "name" : "tvmonitor"
    }
    ann_dic_coco['categories'].append(dic1)
    ann_dic_coco['categories'].append(dic2)

    #
    coco_clsid=[2,16,9,44,6,3,17,62,21,18,19,1,20,7,67,5,4,64,91,92]

    #images: 删除多余的类
    for i in range(len(ann_dic_coco['categories'])):
        if ann_dic_coco['categories'][i]['id'] not in coco_clsid:
            del ann_dic_coco['categories'][i]

    #annotations: 删除多余的类
    for i in range(len(ann_dic_coco['annotations'])):
        if ann_dic_coco['annotations'][i]['category_id'] not in coco_clsid:
            del ann_dic_coco['annotations'][i]    
    
    f2=open(cocovocx+'/annotations/instances_val2017.json','w')
    f2.write(json.dumps(ann_dic_coco, indent=4))

def coco_add_cls(cocovocx):
    import json

    f_train=open(cocovocx+'/annotations/instances_train2017.json')
    f_val=open(cocovocx+'/annotations/instances_val2017.json')
    ann_train=json.load(f_train)
    ann_val=json.load(f_val)

    dic1={
        "supercategory" : "indoor" ,
        "id": 91,
        "name" : "sofa"
    }
    dic2={
        "supercategory" : "indoor" ,
        "id": 92,
        "name" : "tvmonitor"
    }

    ann_train['categories'].append(dic1)
    ann_train['categories'].append(dic2)
    json_train=open(cocovocx+'/annotations/instances_train2017.json','w')
    json_train.write(json.dumps(ann_train, indent=4))

    ann_val['categories'].append(dic1)
    ann_val['categories'].append(dic2)
    json_val=open(cocovocx+'/annotations/instances_val2017.json','w')
    json_val.write(json.dumps(ann_val, indent=4))

def remap_voc_cls(cocovocx):
    """
    voc的类别改成coco的类别
    需要改json文件的annotations的category_id 和 categories的id
    """
    import json

    f_coco=open(cocovocx+'/annotations/instances_val2017.json')
    f_voc_train=open(cocovocx+'/annotations/voc12_train.json')
    f_voc_val=open(cocovocx+'/annotations/voc12_val.json')

    ann_dic_coco=json.load(f_coco)
    ann_dic_voc_train=json.load(f_voc_train)
    ann_dic_voc_val=json.load(f_voc_val)
    ann_list=[ann_dic_voc_train,ann_dic_voc_val]

    # 
    coco_clsid=[2,16,9,44,6,3,17,62,21,18,19,1,20,7,67,5,4,64,91,92]

    for ann_dic_voc in ann_list: 
        #直接一次性换掉整个categories
        ann_dic_voc['categories']=ann_dic_coco['categories']
            
        for i in range(len(ann_dic_voc['images'])):
            ann_dic_voc['images'][i]['file_name']=ann_dic_voc['images'][i]['file_name'][-15:]

        for i in range(len(ann_dic_voc['annotations'])):
            if ann_dic_voc['annotations'][i]['category_id'] ==   0:
                ann_dic_voc['annotations'][i]['category_id']=5
            elif ann_dic_voc['annotations'][i]['category_id'] == 1:
                ann_dic_voc['annotations'][i]['category_id']=2
            elif ann_dic_voc['annotations'][i]['category_id'] == 2:
                ann_dic_voc['annotations'][i]['category_id']=16
            elif ann_dic_voc['annotations'][i]['category_id'] == 3:
                ann_dic_voc['annotations'][i]['category_id']=9
            elif ann_dic_voc['annotations'][i]['category_id'] == 4:
                ann_dic_voc['annotations'][i]['category_id']=44
            elif ann_dic_voc['annotations'][i]['category_id'] == 5:
                ann_dic_voc['annotations'][i]['category_id']=6
            elif ann_dic_voc['annotations'][i]['category_id'] == 6:
                ann_dic_voc['annotations'][i]['category_id']=3
            elif ann_dic_voc['annotations'][i]['category_id'] == 7:
                ann_dic_voc['annotations'][i]['category_id']=17
            elif ann_dic_voc['annotations'][i]['category_id'] == 8:
                ann_dic_voc['annotations'][i]['category_id']=62
            elif ann_dic_voc['annotations'][i]['category_id'] == 9:
                ann_dic_voc['annotations'][i]['category_id']=21
            elif ann_dic_voc['annotations'][i]['category_id'] == 10:
                ann_dic_voc['annotations'][i]['category_id']=67
            elif ann_dic_voc['annotations'][i]['category_id'] == 11:
                ann_dic_voc['annotations'][i]['category_id']=18
            elif ann_dic_voc['annotations'][i]['category_id'] == 12:
                ann_dic_voc['annotations'][i]['category_id']=19
            elif ann_dic_voc['annotations'][i]['category_id'] == 13:
                ann_dic_voc['annotations'][i]['category_id']=4
            elif ann_dic_voc['annotations'][i]['category_id'] == 14:
                ann_dic_voc['annotations'][i]['category_id']=1
            elif ann_dic_voc['annotations'][i]['category_id'] == 15:
                ann_dic_voc['annotations'][i]['category_id']=64
            elif ann_dic_voc['annotations'][i]['category_id'] == 16:
                ann_dic_voc['annotations'][i]['category_id']=20
            elif ann_dic_voc['annotations'][i]['category_id'] == 17:
                ann_dic_voc['annotations'][i]['category_id']=91
            elif ann_dic_voc['annotations'][i]['category_id'] == 18:
                ann_dic_voc['annotations'][i]['category_id']=7
            elif ann_dic_voc['annotations'][i]['category_id'] == 19:
                ann_dic_voc['annotations'][i]['category_id']=92
        
        if ann_dic_voc == ann_dic_voc_train:
            f1=open(cocovocx+'/annotations/voc12_train.json','w')
            f1.write(json.dumps(ann_dic_voc, indent=4))
        if ann_dic_voc == ann_dic_voc_val:
            f2=open(cocovocx+'/annotations/voc12_val.json','w')
            f2.write(json.dumps(ann_dic_voc, indent=4))

def out_coco_from_coco(cocovoc_dir):
    #---把coco的json和图片移出coco
    cocovoc_dir=cocovoc_dir
    os.system('rm '+cocovoc_dir+'/annotations/*')

    os.system('rm '+cocovoc_dir+'/train2017/*')
    
    os.system('rm '+cocovoc_dir+'/val2017/*')

def main():
    args = parse_args()

    #清理文件夹cocovocx
    out_coco_from_coco(args.cocovocx)

    #把coco的图片放入cocovocx(test, 5k, 仅voc类别), 同时处理好json
    mv_coco2cocovocx(args.coco_src, args.cocovocx)

    #coco类别->voc类别
    remap_coco_cls(args.cocovocx)

    #把voc07放入cocovocx
    mv_voc07_2coco(args.voc07_src,args.cocovocx)

    #把voc12放入cocovocx
    mv_voc12_2coco(args.voc12_src,args.cocovocx)

    # 验证结果
    f_coco_train=open(args.cocovocx+'/annotations/instances_train2017.json')
    f_voc_val=open(args.cocovocx+'/annotations/voc12_val.json')
    import json
    ann_coco=json.load(f_coco_train)
    ann_voc=json.load(f_voc_val)
    print('len(ann_coco["images"]):',len(ann_coco["images"]))
    print('len(ann_voc["categories"]):',len(ann_voc['categories']))


main()
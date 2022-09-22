#--------------------------conda  python-------------------------------------
# wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py38_4.8.3-Linux-x86_64.sh --no-check-certificate

# bash Miniconda3-py38_4.8.3-Linux-x86_64.sh

# conda init
# source ~/.bashrc
# echo "ssssssss"

# conda config --show-sources
# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/

#-----------------------------cuda11.1 python3.8 conda------------------------
conda remove -n pytorch --all
conda create -n mmdet python=3.7 -y
conda activate mmdet
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge -y
# pip install torch==1.8.0+cu111 torchvision==0.9.0+cu111 torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html

#------------------mmdetection setup-----------------------------------
pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.8.0/index.html

cd /data1/renyu/mmdetection
pip install -r requirements/build.txt
pip install -v -e .  # or "python setup.py develop"

# mkdir ~/.pip
# echo -e "[global]
# index-url = https://pypi.tuna.tsinghua.edu.cn/simple
# [install]
# trusted-host = https://pypi.tuna.tsinghua.edu.cn" >> ~/.pip/pip.conf

# #---------------------------------------nvcc -V ---------------------------------------------
# echo -e "export LD_LIBRARY_PATH=/usr/local/cuda/lib" >> ~/.bashrc
# echo -e "export PATH=$PATH:/usr/local/cuda/bin" >> ~/.bashrc
# source ~/.bashrc

# apt install tree
# conda install tqdm -y

# python -c "python;import torch;print(torch.cuda.is_available())"
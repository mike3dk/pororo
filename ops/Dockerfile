FROM ubuntu:focal

WORKDIR /app

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt upgrade -y && \
    apt install -y apt-utils \
    git \
    gcc \
    wget \
    build-essential \
    cmake \
    libpq-dev \
    libsndfile-dev \
    libboost-system-dev \
    libboost-thread-dev \
    libboost-program-options-dev \
    libboost-test-dev \
    libeigen3-dev \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libsndfile1-dev \
    libopenblas-dev \
    libfftw3-dev \
    libgflags-dev \
    libgoogle-glog-dev \
    libgl1-mesa-glx \
    libomp-dev \
    python3-pip

# 1. upgrade pip
RUN pip install --upgrade pip

# 2. install python-mecab-ko
RUN pip install python-mecab-ko==1.3.3

# 3. install pororo
RUN pip install pororo

# 4. install brainspeech
RUN pip install soundfile \
    torchaudio==0.6.0 \
    pydub

# RUN conda install -y -c conda-forge librosa

# 5. install etc modules
RUN pip install \
    librosa \
    kollocate \
    koparadigm \
    g2pk \
    fugashi \
    ipadic \
    romkan \
    g2pM \
    jieba \
    opencv-python \
    scikit-image \
    editdistance==0.5.3 \
    epitran==1.2 \
    fastdtw==0.3.4 \
    future \
    Pillow==7.2.0 \
    pinyin==0.4.0 \
    scikit-learn \
    scipy \
    SoundFile==0.10.2 \
    numba==0.48 \
    ko_pron

RUN pip install \
    torch==1.6.0 \
    torchvision==0.7.0 \
    # pillow==4.1.1 \
    fairseq==0.10.2 \
    transformers==4.1.1 \
    sentence_transformers==0.4.1.2 \
    nltk==3.5 \
    word2word \
    wget \
    joblib \
    lxml \
    g2p_en \
    whoosh \
    marisa-trie \
    kss \
    dataclasses \
    six \
    numpy==1.23.5

RUN pip install \
    fastapi \
    uvicorn

# WORKDIR /app/external_lib

# RUN git clone https://github.com/kpu/kenlm.git
# WORKDIR /app/external_lib/kenlm/build
# RUN cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_POSITION_INDEPENDENT_CODE=ON
# RUN make
# ENV KENLM_ROOT_DIR="/app/external_lib/kenlm/"

# WORKDIR /app/external_lib
# RUN git clone -b v0.2 https://github.com/facebookresearch/wav2letter.git
# WORKDIR /app/external_lib/wav2letter/bindings/python
# RUN pip install -e .

WORKDIR /app
COPY src /app/src
COPY pororo /app/pororo

RUN python3 /app/src/run_ner.py "오사카"

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5001"]


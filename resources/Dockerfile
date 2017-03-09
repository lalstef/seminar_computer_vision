# Dockerfile
FROM kavolorn/opencv

RUN apt-get update
RUN apt-get install -y curl
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN apt-get install -y libfreetype6-dev
RUN python3 -m pip install matplotlib scipy imutils jupyter
RUN apt-get install -y git
EXPOSE 7777
RUN mkdir /home/code
RUN cd /home/code
RUN mkdir ~/.jupyter
RUN echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py

RUN git clone https://github.com/lalstef/seminar_computer_vision /home/code/seminar_computer_vision
WORKDIR /home/code/seminar_computer_vision/

ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod a+x /usr/bin/tini

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["jupyter", "notebook", "--ip", "0.0.0.0", "--port", "7777"]

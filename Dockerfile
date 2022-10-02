FROM python:3.10.7 

USER root
RUN apt-get update && apt-get install wget
RUN pip3 install jupyter

ENV JUPYTER_USER Ni
RUN useradd -ms /bin/bash ${JUPYTER_USER}

#downlaod files onto container
RUN wget https://raw.githubusercontent.com/charleneni56/Applied_Cloud_Computing/Week_2/ass2.ipynb -P ./home/${JUPYTER_USER}/pyNotebook/
RUN wget https://raw.githubusercontent.com/charleneni56/Applied_Cloud_Computing/Week_2/requirements.txt -P ./home/${JUPYTER_USER}/pyNotebook/

#chown changes the user and/or group ownership of each given file
RUN chown ${JUPYTER_USER}:${JUPYTER_USER} ./home/${JUPYTER_USER}/pyNotebook/*
#hmod stands for "change mode." It restricts the way a file can be accessed
RUN chmod u+rw ./home/${JUPYTER_USER}/pyNotebook/*

#pip instals all needed pacages for the python notebook to run
RUN pip3 install -r ./home/${JUPYTER_USER}/pyNotebook/requirements.txt

USER ${JUPYTER_USER}
WORKDIR /home/${JUPYTER_USER}/pyNotebook/

#Expose the port before its used for better working 
EXPOSE 8888

ENTRYPOINT ["jupyter", "notebook","./applied_cloud_computing_ass2.ipynb", "--ip=0.0.0.0","--allow-root"]
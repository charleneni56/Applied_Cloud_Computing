## docker build -t test .  - build a container called test
## docker run -d -p 9999:8888 test:
## port mapping goes host-to-IP, run the image "test"
FROM python:latest
RUN apt-get update
RUN apt-get install wget
RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv
RUN awk -F',' 'FNR==2{print $3}' fb_sub.csv >> company.txt
FROM python:3

ADD driver.py /
ADD speech.py /
ADD wikibot.py /
ADD moviebot.py /
ADD dependencies.txt /

RUN apt-get update && apt-get install -y libgirepository1.0-dev && apt-get install libcairo2-dev && apt-get install alsa-utils dbus espeak-data kmod libapparmor1 libasound2 libasound2-data libasyncns0 libdbus-1-3 libespeak1 libfftw3-single3 libflac8 libjack-jackd2-0 libkmod2 libnewt0.52 libogg0 libopus0 libpopt0 libportaudio2 libpulse0 libsamplerate0 libslang2 libsndfile1 libsonic0 libvorbis0a libvorbisenc2 libwrap0 libx11-xcb1 libxi6 libxtst6 python-espeak whiptail
RUN pip install --no-use-pep517 PyGObject==3.38.0
RUN pip install -r dependencies.txt

CMD [ "python3", "./driver.py" ]
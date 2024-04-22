# Chinese Pronunciation Master

**IMPORTANT:** This is just a Proof of Concept (PoC) to show how to use Riva, do not expect a full-fledged application.

## Setting up the environment at AWS
There are some scripts at folders init_scripts that can do this automatically, but sometimes it does not work so smooth, namely:
- setup_script.sh [API_KEY] [ORG]
  - API_KEY & ORG are the ones gotten with an account at Nvidia NGC
- configure_ngc.exp
- docker_login_ngc.exp
* The above scripts need `expect`
```
$ sudo apt-get install expect
```
```
$ sudo ./setup_script.sh [APIKEY] [ORG]
```

### Manual setup
```
sudo su
ngc version upgrade
ngc config set
chmod -R go+rx /opt/ngc-cli
exit
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y nvidia-docker2
sudo systemctl restart docker
sudo docker run --rm --gpus all nvidia/cuda:11.0.3-base nvidia-smi
docker login nvcr.io
	Username: $oauthtoken
	Password: [APIKEY]
ngc config set
docker pull nvcr.io/nvidia/riva/riva-speech:2.15.0-servicemaker
ngc registry resource download-version "nvidia/riva/riva_quickstart:2.15.0"
cd riva_quickstart_v2.15.0/
sudo chmod ugo+rx *
conda create --name=conda-riva python=3.10
```
* Heuristically python 3.10 did not cause problems

### riva-speech container
Using the `config.sh` hereby at `init_scripts/config.sh`:
```
./riva_init.sh [config.sh]
./riva_start.sh [config.sh]
```
Note: `riva_init.sh` will take a while to finish (~45 minutes), so be patient.
Bonus track: to run live examples (e.g. those at [asr-basics](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/tutorials/asr-basics.html)) run `jupyter lab --allow-root --ip 0.0.0.0 --port 8888`

## Flask

### Locally
Located at where this repository has been cloned (**could be the local machine used for developing** just adjust `config.py`, fundamentally `RIVA_SPEECH_API_URL`), run:
```
$ pip install -r requirements.txt
```
At react-app
```
$ npm install
$ npm run build
```
Run the server
```
$ python main.py
```
To use develop locally using React just go to `react-app` and run:
```
$ npm start
```

### At AWS
Possible dependency problem, troubleshoot:
```
sudo apt-get update
sudo apt-get install -y portaudio19-dev python3-pyaudio
```


## References
- [NVIDIA RIVA](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/index.html)
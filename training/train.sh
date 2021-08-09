python3 prepare.py
precise-train android.net /opt/precise/training/android -e 1000 -b 128
precise-test android.net /opt/precise/training/android
precise-convert android.net
rm -rf /opt/precise/training/android
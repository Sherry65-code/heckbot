#include<iostream>
using namespace std;

int main()
{
    cout << "Welcome to heckbot setup:" << endl;
    cout << "Installing heckbot dependencies on your PC..." << endl;
    cout << "Which package manager are you using >> p for pacman or p for pacman:";
    char pmn;
    cin >> pmn;
    if (pmn == 'p'){
        cout << "Installing Dependencies...";
        system("sudo pacman -Sy festival --noconfirm");
        system("sudo pacman -S festival-us --noconfirm");
        system("sudo rm -r /usr/share/festival/voices/us/cmu_us_awb_cg  /usr/share/festival/voices/us/cmu_us_slt_cg");
        system("sudo pacman -S python-pip python-pyaudio --noconfirm");
        system("sudo pip3 install SpeechRecognition");
        system("clear");
        cout << "Setup has been done, Now you can run the 'run' file in terminal";
    }
    else{
        cout << "Wrong bedu";
    }
    return 0;
}
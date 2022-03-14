#pragma once
#include "MainClass.h"

class ZodiacSings : public MainClass
{
private:
    string name = "";
    string birthday = "";
    string number = "";
    string characteristic = "";
    vector<ZodiacSings> ZS;

public:
    ZodiacSings() {}

    ZodiacSings(string name, string birthday, string number, string characteristic);

    string getName();

    string getBirthday();

    string getNumber();

    string getCharacteristic();

    void input(string file) override;

    bool searching(string a,string bith) override;

    vector<ZodiacSings>& returnVec();
};

#pragma once
#include "MainClass.h"

class Hostel : public MainClass
{
private:
    string name = "";
    string group = "";
    int room = 0;
    string date = "";
    map <string, vector<Hostel>> host;

public:
    Hostel() {};

    Hostel(string name, string group, int room, string date);

    string getName();

    string getGroup();

    int getRoom();

    string getDate();

    void input(string file) override;

    bool searching(string date, string datemap) override;

    map <string, vector<Hostel>>& returnMap();
};


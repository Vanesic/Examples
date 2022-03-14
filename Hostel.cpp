#include "Hostel.h"

Hostel::Hostel(string name, string group, int room, string date)
{
    this->name = name;
    this->group = group;
    this->room = room;
    this->date = date;
}

string Hostel::getName()
{
    return name;
}

string Hostel::getGroup()
{
    return group;
}

int Hostel::getRoom()
{
    return room;
}

string Hostel::getDate()
{
    return date;
}

void Hostel::input(string file)
{
    ifstream ifs;
    ifs.open(file);
    if (!ifs.is_open()) {
        throw exception("Файл не удалось открыть!");
    }

    string emptyStr = "";
    string name = "";
    string group = "";
    int room = 0;
    string date = "";

    int count;
    ifs >> count;
    vector <Hostel> hostvec;
    hostvec.reserve(count);

    getline(ifs, emptyStr);
    for (int i = 0; i < count; i++) {
        getline(ifs, emptyStr);
        getline(ifs, name);
        getline(ifs, group);
        ifs >> room;
        getline(ifs, emptyStr);
        getline(ifs, date);

        Hostel element(name, group, room, date);

        hostvec.emplace_back(element);

        if (host.find(group) == host.end())
            host.emplace(group, hostvec);
        else
            host[group].emplace_back(element);
    }

    ifs.close();
}



bool Hostel::searching(string date, string mapdate)
{
    if (mapdate.find(date) != string::npos)
        return true;
    else
        return false;
}

map<string, vector<Hostel>>& Hostel::returnMap()
{
    return host;
}



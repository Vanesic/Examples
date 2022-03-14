#include "ZodiacSings.h"

ZodiacSings::ZodiacSings(string name, string birthday, string number, string characteristic)
{
    this->name = name;
    this->birthday = birthday;
    this->number = number;
    this->characteristic = characteristic;
}

string ZodiacSings::getName() {
    return name;
}

string ZodiacSings::getBirthday() {
    return birthday;
}

string ZodiacSings::getNumber() {
    return number;
}

string ZodiacSings::getCharacteristic() {
    return characteristic;
}

void ZodiacSings::input(string file)
{
    ifstream ifs;

    ifs.open(file);
    if (!ifs.is_open()) {
        throw exception("Файл не удалось открыть!");
    }

    string emptyStr;
    string name;
    string birthday;
    string number;
    string characteristic;

    int count;
    ifs >> count;
    ZS.reserve(count);

    getline(ifs, emptyStr);
    for (int i = 0; i < count; i++) {

        getline(ifs, emptyStr);
        getline(ifs, name);
        getline(ifs, birthday);
        getline(ifs, number);
        getline(ifs, characteristic);

        ZodiacSings element(name, birthday, number, characteristic);

        ZS.emplace_back(element);
    }

    ifs.close();
}

bool ZodiacSings::searching(string a, string bith)
{
    if (bith == a)
        return true;
    else
        return false;
}

vector<ZodiacSings>& ZodiacSings::returnVec()
{
    return ZS;
}


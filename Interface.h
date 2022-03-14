#pragma once
#include "MainClass.h"
#include "Hostel.h"
#include "ZodiacSings.h"

class Interface
{
private:
	vector <ZodiacSings> ZSvec;
	map <string, vector<Hostel>> Hostmap;
public:
	void selectElement()
	{
		ZodiacSings ZS;
		char num = ' ';
		cout << "Выберите из списка элементы, с которыми вы хотите работать: " << endl;
		cout << " 1 - Знаки зодиака\n 2 - Общежитие\n 0 - Выход из программы" << endl;
		cin >> num;
		if (num == '1')
		{
			// Чтение данных из файла
			try {
				ZS.input("ZodiacSings's_info.txt");
				ZSvec = ZS.returnVec();
				sort(ZSvec.begin(),
					ZSvec.end(),
					[](ZodiacSings& a, ZodiacSings& b) { return a.getBirthday() < b.getBirthday(); }
				);
			}
			catch (exception& ex) {
				cerr << ex.what() << endl;
			}

			// Вывод всех имеющихся данных в консоль
			cout << "Список:" << endl;
			for (int i = 0; i < ZSvec.size(); i++) {
				cout << ZSvec[i].getBirthday() << endl;
			}

			// Запрос данных для поиска
			string bith = "";
			cout << "Введите дату рождения: ";
			while (bith == "") {
				getline(cin, bith, '\n');
			}
			// Поиск по заданным данным
			for (int i = 0; i < 10; i++) {
				if (ZS.searching(bith, ZSvec[i].getBirthday()) == true) {
					cout << "ФИО:  " << ZSvec[i].getName() << endl;
					cout << "Дата рождения:  " << ZSvec[i].getBirthday() << endl;
					cout << "Номер:  " << ZSvec[i].getNumber() << endl;
					cout << "Характеристика знака:  " << ZSvec[i].getCharacteristic() << endl;
				}
			}
		}

		else if (num == '2')
		{
			Hostel hostel;

			// Чтение данных из файла
			try {
				hostel.input("Hostel's_info.txt");
				Hostmap = hostel.returnMap();
			}
			catch (exception& ex) {
				cerr << ex.what() << endl;
			}

			// Вывод всех имеющихся данных в консоль   
			cout << "Список: " << endl;
			map <string, vector<Hostel>> ::iterator it = Hostmap.begin();
			for (it; it != Hostmap.end(); ++it) {
				cout << it->first << endl;
			}

			// Запрос данных для поиска
			string group = "";
			cout << "Введите группу: ";
			while (group == "") {
				getline(cin, group, '\n');
			}

			cout << "Введите год: ";
			string year = "";

			while (year == "") {
				getline(cin, year, '\n');
			}

			// Поиск по заданным данным и вывод
			for (int i = 0; i < Hostmap[group].size(); i++)
			{
				if (hostel.searching(year, Hostmap[group][i].getDate())) {
					cout << endl;
					cout << "ФИО:  " << Hostmap[group][i].getName() << endl;
					cout << "Группа  " << Hostmap[group][i].getGroup() << endl;
					cout << "Комната:  " << Hostmap[group][i].getRoom() << endl;
					cout << "Дата:  " << Hostmap[group][i].getDate() << endl;
				}
			}
			cout << endl;
		}

		else if (num == '0')
		{
			return;
		}

		else
		{
			cout << "Введена некорректная команда" << endl;
		}
	}
};


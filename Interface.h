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
		cout << "�������� �� ������ ��������, � �������� �� ������ ��������: " << endl;
		cout << " 1 - ����� �������\n 2 - ���������\n 0 - ����� �� ���������" << endl;
		cin >> num;
		if (num == '1')
		{
			// ������ ������ �� �����
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

			// ����� ���� ��������� ������ � �������
			cout << "������:" << endl;
			for (int i = 0; i < ZSvec.size(); i++) {
				cout << ZSvec[i].getBirthday() << endl;
			}

			// ������ ������ ��� ������
			string bith = "";
			cout << "������� ���� ��������: ";
			while (bith == "") {
				getline(cin, bith, '\n');
			}
			// ����� �� �������� ������
			for (int i = 0; i < 10; i++) {
				if (ZS.searching(bith, ZSvec[i].getBirthday()) == true) {
					cout << "���:  " << ZSvec[i].getName() << endl;
					cout << "���� ��������:  " << ZSvec[i].getBirthday() << endl;
					cout << "�����:  " << ZSvec[i].getNumber() << endl;
					cout << "�������������� �����:  " << ZSvec[i].getCharacteristic() << endl;
				}
			}
		}

		else if (num == '2')
		{
			Hostel hostel;

			// ������ ������ �� �����
			try {
				hostel.input("Hostel's_info.txt");
				Hostmap = hostel.returnMap();
			}
			catch (exception& ex) {
				cerr << ex.what() << endl;
			}

			// ����� ���� ��������� ������ � �������   
			cout << "������: " << endl;
			map <string, vector<Hostel>> ::iterator it = Hostmap.begin();
			for (it; it != Hostmap.end(); ++it) {
				cout << it->first << endl;
			}

			// ������ ������ ��� ������
			string group = "";
			cout << "������� ������: ";
			while (group == "") {
				getline(cin, group, '\n');
			}

			cout << "������� ���: ";
			string year = "";

			while (year == "") {
				getline(cin, year, '\n');
			}

			// ����� �� �������� ������ � �����
			for (int i = 0; i < Hostmap[group].size(); i++)
			{
				if (hostel.searching(year, Hostmap[group][i].getDate())) {
					cout << endl;
					cout << "���:  " << Hostmap[group][i].getName() << endl;
					cout << "������  " << Hostmap[group][i].getGroup() << endl;
					cout << "�������:  " << Hostmap[group][i].getRoom() << endl;
					cout << "����:  " << Hostmap[group][i].getDate() << endl;
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
			cout << "������� ������������ �������" << endl;
		}
	}
};


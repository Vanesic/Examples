#pragma once
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <fstream>


using namespace std;

class MainClass
{
public:
	virtual void input(string file)=0;

	virtual bool searching(string a, string b)=0;
};


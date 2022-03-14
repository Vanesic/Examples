#include "Interface.h"
#include "Windows.h"
#include <locale>
#include "Hostel.h"
#include "ZodiacSings.h"

int main() {
	setlocale(LC_ALL, "Russian");
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);
	Interface IF;
	IF.selectElement();
	return 0;
}
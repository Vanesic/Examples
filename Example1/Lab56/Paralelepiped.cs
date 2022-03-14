using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab56
{
	class Paralelepiped : Body
	{
        private float a, b, c;
        public Paralelepiped(float a, float b, float c)
        {
            this.a = a;
            this.b = b;
            this.c = c;
        }

        public override void calculateData()
        {
            area = (a * b + b * c + a * c) * 2;
            volume = a * b * c;
        }
    }
}

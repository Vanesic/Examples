using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab56
{
	class Cone : Body
	{
        private float h, R, l;
        public Cone(float h, float r)
        {
            this.h = h;
            R = r;
            l = Convert.ToSingle(Math.Sqrt(Math.Pow(this.h, 2) + Math.Pow(R, 2)));
        }

        public override void calculateData()
        {
            area = Convert.ToSingle(Math.PI * l * R + Math.Pow(R, 2) * Math.PI);
            volume = Convert.ToSingle(Math.PI * Math.Pow(R, 2) * h / 3);
        }
    }
}

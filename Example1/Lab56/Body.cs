using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab56
{
	abstract class Body
	{
        protected float area = 0, volume = 0;
        abstract public void calculateData();

        public float getArea()
        {
            return area;
        }

        public float getVolume()
        {
           return volume;
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab56
{
	class Ball: Body
	{ 
        private float R;
        public Ball(float R)
        {
            this.R = R;
        }

        public override void calculateData()
        {
            area = Convert.ToSingle(4 * Math.PI * Math.Pow(R, 2));
            volume = (float)(4 / 3 * Math.PI * Math.Pow(R, 3));
        }

    }
}

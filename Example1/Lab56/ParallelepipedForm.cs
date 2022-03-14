using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lab56
{
	public partial class ParallelepipedForm : Form
	{
		public ParallelepipedForm()
		{
			InitializeComponent();
		}

		private void ParallelepipedForm_FormClosing(object sender, FormClosingEventArgs e)
		{
			Application.Exit();
		}

		private void backButton_Click(object sender, EventArgs e)
		{
			this.Hide();
			Menu menu = new Menu();
			menu.Show();
		}

		private void button1_Click(object sender, EventArgs e)
		{
            Body parallelepiped = null;
            try
            {
                float a = Convert.ToSingle(aSIde.Text);
                float b = Convert.ToSingle(bSide.Text);
                float c = Convert.ToSingle(cSide.Text);
                if (a < 0 || b < 0 || c < 0)
                    throw new Exception("Данные не могут быть отрицательными!");
                parallelepiped = new Paralelepiped(a,b,c);
            }
            catch (FormatException ex)
            {
                aSIde.Text = "";
                bSide.Text = "";
                cSide.Text = "";
                Area.Text = "Площадь = ";
                Valume.Text = "Объем = ";
                MessageBox.Show(ex.Message, "Ошибка!", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            catch (Exception ex)
            {
                aSIde.Text = "";
                bSide.Text = "";
                cSide.Text = "";
                Area.Text = "Площадь = ";
                Valume.Text = "Объем = ";
                MessageBox.Show(ex.Message, "Ошибка!", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            parallelepiped.calculateData();
            Area.Text ="Площадь = " +parallelepiped.getArea().ToString();
            Valume.Text ="Объем = "+ parallelepiped.getVolume().ToString();
        }

	}
}

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
	public partial class ConeForm : Form
	{
		public ConeForm()
		{
			InitializeComponent();
		}

		private void backButton_Click(object sender, EventArgs e)
		{
			this.Hide();
			Menu menu = new Menu();
			menu.Show();
		}

		private void ConeForm_FormClosing(object sender, FormClosingEventArgs e)
		{
			Application.Exit();
		}

		private void button1_Click(object sender, EventArgs e)
		{
			Body cone = null;
			try
			{
				float h = Convert.ToSingle(height.Text);
				float R = Convert.ToSingle(Radiuscone.Text);
				if (R < 0 || h < 0)
					throw new Exception("Данные не могут быть отрицательными!");
				cone = new Cone(h, R);
			}
			catch (FormatException ex)
			{
				height.Text = "";
				Radiuscone.Text = "";
				Area.Text = "Площадь = ";
				Valume.Text = "Объем = ";
				MessageBox.Show(ex.Message, "Ошибка!", MessageBoxButtons.OK, MessageBoxIcon.Error);
				return;
			}
			catch (Exception ex)
			{
				height.Text = "";
				Radiuscone.Text = "";
				Area.Text = "Площадь = ";
				Valume.Text = "Объем = ";
				MessageBox.Show(ex.Message, "Ошибка!", MessageBoxButtons.OK, MessageBoxIcon.Error);
				return;
			}

			cone.calculateData();
			Area.Text = "Площадь = "+ cone.getArea().ToString();
			Valume.Text = "Объем = "+ cone.getVolume().ToString();
		}

	}
}

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
	public partial class BallForm : Form
	{
		public BallForm()
		{
			InitializeComponent();
		}

		private void BallForm_FormClosing(object sender, FormClosingEventArgs e)
		{
			Application.Exit();
		}

		private void button2_Click(object sender, EventArgs e)
		{
			this.Hide();
			Menu menu = new Menu();
			menu.Show();
			Radius.Text = "";
		}

		private void button1_Click(object sender, EventArgs e)
		{
			Body ball = null;
			try
			{
				float R = Convert.ToSingle(Radius.Text);
				if (R < 0)
					throw new Exception("Данные не могут быть отрицательными!");
				ball = new Ball(R);
			}
			catch (FormatException ex)
			{
				Radius.Text = "";
				Area.Text = "Площадь = ";
				Valume.Text = "Объем = ";
				MessageBox.Show(ex.Message, "Ошибка!", MessageBoxButtons.OK, MessageBoxIcon.Error);
				return;
			}
			catch (Exception ex)
			{
				Radius.Text = "";
				Area.Text = "Площадь = ";
				Valume.Text = "Объем = ";
				MessageBox.Show(ex.Message, "Ошибка!", MessageBoxButtons.OK, MessageBoxIcon.Error);
				return;
			}

			ball.calculateData();
			Area.Text ="Площадь = "+ ball.getArea().ToString();
			Valume.Text ="Объем = "+ ball.getVolume().ToString();
		}
	}
}

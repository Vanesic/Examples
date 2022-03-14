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
	public partial class Menu : Form
	{
		public Menu()
		{
			InitializeComponent();
		}

		private void ballForm_Click(object sender, EventArgs e)
		{
			this.Hide();
			BallForm ball = new BallForm();
			ball.Show();
		}

		private void Menu_FormClosing(object sender, FormClosingEventArgs e)
		{
			Application.Exit();
		}

		private void ConeForm_Click(object sender, EventArgs e)
		{
			this.Hide();
			ConeForm cone = new ConeForm();
			cone.Show();
		}

		private void paralForm_Click(object sender, EventArgs e)
		{
			this.Hide();
			ParallelepipedForm parall = new ParallelepipedForm();
			parall.Show();
		}
	}
}

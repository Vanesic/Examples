
namespace Lab56
{
	partial class BallForm
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Windows Form Designer generated code

		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(BallForm));
			this.BallLabel = new System.Windows.Forms.Label();
			this.BallLabelHeip = new System.Windows.Forms.Label();
			this.BallPict = new System.Windows.Forms.PictureBox();
			this.Radius = new System.Windows.Forms.TextBox();
			this.Valume = new System.Windows.Forms.Label();
			this.label4 = new System.Windows.Forms.Label();
			this.Area = new System.Windows.Forms.Label();
			this.button1 = new System.Windows.Forms.Button();
			this.backButton = new System.Windows.Forms.Button();
			((System.ComponentModel.ISupportInitialize)(this.BallPict)).BeginInit();
			this.SuspendLayout();
			// 
			// BallLabel
			// 
			this.BallLabel.BackColor = System.Drawing.Color.Transparent;
			this.BallLabel.Dock = System.Windows.Forms.DockStyle.Top;
			this.BallLabel.Font = new System.Drawing.Font("Montserrat SemiBold", 40F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
			this.BallLabel.Location = new System.Drawing.Point(0, 0);
			this.BallLabel.Name = "BallLabel";
			this.BallLabel.Size = new System.Drawing.Size(1006, 92);
			this.BallLabel.TabIndex = 0;
			this.BallLabel.Text = "Шар";
			this.BallLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// BallLabelHeip
			// 
			this.BallLabelHeip.Location = new System.Drawing.Point(52, 168);
			this.BallLabelHeip.Name = "BallLabelHeip";
			this.BallLabelHeip.Size = new System.Drawing.Size(349, 142);
			this.BallLabelHeip.TabIndex = 1;
			this.BallLabelHeip.Text = "Введите радиус шара в соответствующее поле для вычисления объема и площади поверх" +
    "ности";
			this.BallLabelHeip.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// BallPict
			// 
			this.BallPict.Image = ((System.Drawing.Image)(resources.GetObject("BallPict.Image")));
			this.BallPict.Location = new System.Drawing.Point(597, 126);
			this.BallPict.Name = "BallPict";
			this.BallPict.Size = new System.Drawing.Size(368, 299);
			this.BallPict.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
			this.BallPict.TabIndex = 2;
			this.BallPict.TabStop = false;
			// 
			// Radius
			// 
			this.Radius.BackColor = System.Drawing.Color.GreenYellow;
			this.Radius.Location = new System.Drawing.Point(102, 440);
			this.Radius.Name = "Radius";
			this.Radius.Size = new System.Drawing.Size(226, 39);
			this.Radius.TabIndex = 15;
			// 
			// Valume
			// 
			this.Valume.AutoSize = true;
			this.Valume.Location = new System.Drawing.Point(625, 483);
			this.Valume.Name = "Valume";
			this.Valume.Size = new System.Drawing.Size(114, 37);
			this.Valume.TabIndex = 4;
			this.Valume.Text = "Объем";
			// 
			// label4
			// 
			this.label4.BackColor = System.Drawing.Color.Transparent;
			this.label4.Location = new System.Drawing.Point(58, 440);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(44, 39);
			this.label4.TabIndex = 5;
			this.label4.Text = "R:";
			// 
			// Area
			// 
			this.Area.AutoSize = true;
			this.Area.Location = new System.Drawing.Point(625, 545);
			this.Area.Name = "Area";
			this.Area.Size = new System.Drawing.Size(150, 37);
			this.Area.TabIndex = 6;
			this.Area.Text = "Площадь";
			// 
			// button1
			// 
			this.button1.BackColor = System.Drawing.Color.MediumSpringGreen;
			this.button1.Location = new System.Drawing.Point(102, 577);
			this.button1.Name = "button1";
			this.button1.Size = new System.Drawing.Size(198, 46);
			this.button1.TabIndex = 7;
			this.button1.Text = "Посчитать!";
			this.button1.UseVisualStyleBackColor = false;
			this.button1.Click += new System.EventHandler(this.button1_Click);
			// 
			// backButton
			// 
			this.backButton.BackColor = System.Drawing.SystemColors.GradientActiveCaption;
			this.backButton.Cursor = System.Windows.Forms.Cursors.Hand;
			this.backButton.FlatAppearance.BorderSize = 0;
			this.backButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.backButton.Location = new System.Drawing.Point(12, 12);
			this.backButton.Name = "backButton";
			this.backButton.Size = new System.Drawing.Size(99, 37);
			this.backButton.TabIndex = 8;
			this.backButton.Text = "Назад";
			this.backButton.UseVisualStyleBackColor = false;
			this.backButton.Click += new System.EventHandler(this.button2_Click);
			// 
			// BallForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(17F, 36F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
			this.ClientSize = new System.Drawing.Size(1006, 673);
			this.Controls.Add(this.backButton);
			this.Controls.Add(this.button1);
			this.Controls.Add(this.Area);
			this.Controls.Add(this.label4);
			this.Controls.Add(this.Valume);
			this.Controls.Add(this.Radius);
			this.Controls.Add(this.BallPict);
			this.Controls.Add(this.BallLabelHeip);
			this.Controls.Add(this.BallLabel);
			this.Font = new System.Drawing.Font("Montserrat SemiBold", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
			this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
			this.Margin = new System.Windows.Forms.Padding(7);
			this.MaximumSize = new System.Drawing.Size(1024, 720);
			this.MinimumSize = new System.Drawing.Size(1024, 720);
			this.Name = "BallForm";
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
			this.Text = "AreaAndVolume";
			this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.BallForm_FormClosing);
			((System.ComponentModel.ISupportInitialize)(this.BallPict)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Label BallLabel;
		private System.Windows.Forms.Label BallLabelHeip;
		private System.Windows.Forms.PictureBox BallPict;
		private System.Windows.Forms.TextBox Radius;
		private System.Windows.Forms.Label Valume;
		private System.Windows.Forms.Label label4;
		private System.Windows.Forms.Label Area;
		private System.Windows.Forms.Button button1;
		private System.Windows.Forms.Button backButton;
	}
}
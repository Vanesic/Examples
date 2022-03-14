
namespace Lab56
{
	partial class ParallelepipedForm
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
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(ParallelepipedForm));
			this.ParalLabel = new System.Windows.Forms.Label();
			this.backButton = new System.Windows.Forms.Button();
			this.label1 = new System.Windows.Forms.Label();
			this.aSIde = new System.Windows.Forms.TextBox();
			this.label4 = new System.Windows.Forms.Label();
			this.bSide = new System.Windows.Forms.TextBox();
			this.ConeLabelHeip = new System.Windows.Forms.Label();
			this.cSideLabel = new System.Windows.Forms.Label();
			this.cSide = new System.Windows.Forms.TextBox();
			this.ParallPict = new System.Windows.Forms.PictureBox();
			this.Area = new System.Windows.Forms.Label();
			this.Valume = new System.Windows.Forms.Label();
			this.button1 = new System.Windows.Forms.Button();
			((System.ComponentModel.ISupportInitialize)(this.ParallPict)).BeginInit();
			this.SuspendLayout();
			// 
			// ParalLabel
			// 
			this.ParalLabel.BackColor = System.Drawing.Color.Transparent;
			this.ParalLabel.Dock = System.Windows.Forms.DockStyle.Top;
			this.ParalLabel.Font = new System.Drawing.Font("Montserrat SemiBold", 40F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
			this.ParalLabel.Location = new System.Drawing.Point(0, 0);
			this.ParalLabel.Name = "ParalLabel";
			this.ParalLabel.Size = new System.Drawing.Size(1006, 79);
			this.ParalLabel.TabIndex = 0;
			this.ParalLabel.Text = "Параллелепипед";
			this.ParalLabel.TextAlign = System.Drawing.ContentAlignment.TopCenter;
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
			this.backButton.TabIndex = 18;
			this.backButton.Text = "Назад";
			this.backButton.UseVisualStyleBackColor = false;
			this.backButton.Click += new System.EventHandler(this.backButton_Click);
			// 
			// label1
			// 
			this.label1.BackColor = System.Drawing.Color.Transparent;
			this.label1.Location = new System.Drawing.Point(108, 397);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(38, 39);
			this.label1.TabIndex = 23;
			this.label1.Text = "a:";
			// 
			// aSIde
			// 
			this.aSIde.BackColor = System.Drawing.Color.GreenYellow;
			this.aSIde.Location = new System.Drawing.Point(146, 397);
			this.aSIde.Multiline = true;
			this.aSIde.Name = "aSIde";
			this.aSIde.Size = new System.Drawing.Size(226, 33);
			this.aSIde.TabIndex = 15;
			// 
			// label4
			// 
			this.label4.BackColor = System.Drawing.Color.Transparent;
			this.label4.Location = new System.Drawing.Point(108, 455);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(38, 39);
			this.label4.TabIndex = 21;
			this.label4.Text = "b:";
			// 
			// bSide
			// 
			this.bSide.BackColor = System.Drawing.Color.GreenYellow;
			this.bSide.Location = new System.Drawing.Point(146, 455);
			this.bSide.Name = "bSide";
			this.bSide.Size = new System.Drawing.Size(226, 39);
			this.bSide.TabIndex = 15;
			// 
			// ConeLabelHeip
			// 
			this.ConeLabelHeip.Location = new System.Drawing.Point(86, 141);
			this.ConeLabelHeip.Name = "ConeLabelHeip";
			this.ConeLabelHeip.Size = new System.Drawing.Size(359, 226);
			this.ConeLabelHeip.TabIndex = 19;
			this.ConeLabelHeip.Text = "Введите три стороны параллелепипеда (длину, ширину, высоту) в соответствующие пол" +
    "я для вычисления объема и площади поверхности параллелепипеда";
			this.ConeLabelHeip.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// cSideLabel
			// 
			this.cSideLabel.BackColor = System.Drawing.Color.Transparent;
			this.cSideLabel.Location = new System.Drawing.Point(108, 517);
			this.cSideLabel.Name = "cSideLabel";
			this.cSideLabel.Size = new System.Drawing.Size(38, 39);
			this.cSideLabel.TabIndex = 25;
			this.cSideLabel.Text = "c:";
			// 
			// cSide
			// 
			this.cSide.BackColor = System.Drawing.Color.GreenYellow;
			this.cSide.Location = new System.Drawing.Point(146, 517);
			this.cSide.Name = "cSide";
			this.cSide.Size = new System.Drawing.Size(226, 39);
			this.cSide.TabIndex = 15;
			// 
			// ParallPict
			// 
			this.ParallPict.Image = ((System.Drawing.Image)(resources.GetObject("ParallPict.Image")));
			this.ParallPict.Location = new System.Drawing.Point(615, 131);
			this.ParallPict.Name = "ParallPict";
			this.ParallPict.Size = new System.Drawing.Size(358, 270);
			this.ParallPict.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
			this.ParallPict.TabIndex = 26;
			this.ParallPict.TabStop = false;
			// 
			// Area
			// 
			this.Area.AutoSize = true;
			this.Area.Location = new System.Drawing.Point(621, 546);
			this.Area.Name = "Area";
			this.Area.Size = new System.Drawing.Size(150, 37);
			this.Area.TabIndex = 28;
			this.Area.Text = "Площадь";
			// 
			// Valume
			// 
			this.Valume.AutoSize = true;
			this.Valume.Location = new System.Drawing.Point(621, 484);
			this.Valume.Name = "Valume";
			this.Valume.Size = new System.Drawing.Size(114, 37);
			this.Valume.TabIndex = 27;
			this.Valume.Text = "Объем";
			// 
			// button1
			// 
			this.button1.BackColor = System.Drawing.Color.MediumSpringGreen;
			this.button1.Location = new System.Drawing.Point(155, 597);
			this.button1.Name = "button1";
			this.button1.Size = new System.Drawing.Size(198, 46);
			this.button1.TabIndex = 29;
			this.button1.Text = "Посчитать!";
			this.button1.UseVisualStyleBackColor = false;
			this.button1.Click += new System.EventHandler(this.button1_Click);
			// 
			// ParallelepipedForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(17F, 36F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
			this.ClientSize = new System.Drawing.Size(1006, 673);
			this.Controls.Add(this.button1);
			this.Controls.Add(this.Area);
			this.Controls.Add(this.Valume);
			this.Controls.Add(this.ParallPict);
			this.Controls.Add(this.cSideLabel);
			this.Controls.Add(this.cSide);
			this.Controls.Add(this.label1);
			this.Controls.Add(this.aSIde);
			this.Controls.Add(this.label4);
			this.Controls.Add(this.bSide);
			this.Controls.Add(this.ConeLabelHeip);
			this.Controls.Add(this.backButton);
			this.Controls.Add(this.ParalLabel);
			this.Font = new System.Drawing.Font("Montserrat SemiBold", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
			this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
			this.Margin = new System.Windows.Forms.Padding(7);
			this.MaximumSize = new System.Drawing.Size(1024, 720);
			this.MinimumSize = new System.Drawing.Size(1024, 720);
			this.Name = "ParallelepipedForm";
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
			this.Text = "AreaAndVolume";
			this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.ParallelepipedForm_FormClosing);
			((System.ComponentModel.ISupportInitialize)(this.ParallPict)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Label ParalLabel;
		private System.Windows.Forms.Button backButton;
		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.TextBox aSIde;
		private System.Windows.Forms.Label label4;
		private System.Windows.Forms.TextBox bSide;
		private System.Windows.Forms.Label ConeLabelHeip;
		private System.Windows.Forms.Label cSideLabel;
		private System.Windows.Forms.TextBox cSide;
		private System.Windows.Forms.PictureBox ParallPict;
		private System.Windows.Forms.Label Area;
		private System.Windows.Forms.Label Valume;
		private System.Windows.Forms.Button button1;
	}
}
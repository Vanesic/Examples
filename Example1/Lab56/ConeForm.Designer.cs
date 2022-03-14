
namespace Lab56
{
	partial class ConeForm
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
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(ConeForm));
			this.button1 = new System.Windows.Forms.Button();
			this.Area = new System.Windows.Forms.Label();
			this.label4 = new System.Windows.Forms.Label();
			this.Valume = new System.Windows.Forms.Label();
			this.Radiuscone = new System.Windows.Forms.TextBox();
			this.BallPict = new System.Windows.Forms.PictureBox();
			this.ConeLabelHeip = new System.Windows.Forms.Label();
			this.label1 = new System.Windows.Forms.Label();
			this.height = new System.Windows.Forms.TextBox();
			this.backButton = new System.Windows.Forms.Button();
			this.ConeLabel = new System.Windows.Forms.Label();
			((System.ComponentModel.ISupportInitialize)(this.BallPict)).BeginInit();
			this.SuspendLayout();
			// 
			// button1
			// 
			this.button1.BackColor = System.Drawing.Color.MediumSpringGreen;
			this.button1.Location = new System.Drawing.Point(98, 543);
			this.button1.Name = "button1";
			this.button1.Size = new System.Drawing.Size(198, 46);
			this.button1.TabIndex = 14;
			this.button1.Text = "Посчитать!";
			this.button1.UseVisualStyleBackColor = false;
			this.button1.Click += new System.EventHandler(this.button1_Click);
			// 
			// Area
			// 
			this.Area.AutoSize = true;
			this.Area.Location = new System.Drawing.Point(621, 511);
			this.Area.Name = "Area";
			this.Area.Size = new System.Drawing.Size(150, 37);
			this.Area.TabIndex = 13;
			this.Area.Text = "Площадь";
			// 
			// label4
			// 
			this.label4.BackColor = System.Drawing.Color.Transparent;
			this.label4.Location = new System.Drawing.Point(60, 406);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(38, 39);
			this.label4.TabIndex = 12;
			this.label4.Text = "R:";
			// 
			// Valume
			// 
			this.Valume.AutoSize = true;
			this.Valume.Location = new System.Drawing.Point(621, 449);
			this.Valume.Name = "Valume";
			this.Valume.Size = new System.Drawing.Size(114, 37);
			this.Valume.TabIndex = 11;
			this.Valume.Text = "Объем";
			// 
			// Radiuscone
			// 
			this.Radiuscone.BackColor = System.Drawing.Color.GreenYellow;
			this.Radiuscone.Location = new System.Drawing.Point(98, 406);
			this.Radiuscone.Name = "Radiuscone";
			this.Radiuscone.Size = new System.Drawing.Size(226, 39);
			this.Radiuscone.TabIndex = 15;
			// 
			// BallPict
			// 
			this.BallPict.Image = ((System.Drawing.Image)(resources.GetObject("BallPict.Image")));
			this.BallPict.Location = new System.Drawing.Point(603, 121);
			this.BallPict.Name = "BallPict";
			this.BallPict.Size = new System.Drawing.Size(358, 270);
			this.BallPict.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
			this.BallPict.TabIndex = 9;
			this.BallPict.TabStop = false;
			// 
			// ConeLabelHeip
			// 
			this.ConeLabelHeip.Location = new System.Drawing.Point(54, 161);
			this.ConeLabelHeip.Name = "ConeLabelHeip";
			this.ConeLabelHeip.Size = new System.Drawing.Size(331, 131);
			this.ConeLabelHeip.TabIndex = 8;
			this.ConeLabelHeip.Text = "Введите высоту и радиус конуса в соответствующие поля для нахождения площади и об" +
    "ъема";
			this.ConeLabelHeip.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// label1
			// 
			this.label1.BackColor = System.Drawing.Color.Transparent;
			this.label1.Location = new System.Drawing.Point(60, 348);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(38, 39);
			this.label1.TabIndex = 16;
			this.label1.Text = "h:";
			// 
			// height
			// 
			this.height.BackColor = System.Drawing.Color.GreenYellow;
			this.height.Location = new System.Drawing.Point(98, 348);
			this.height.Multiline = true;
			this.height.Name = "height";
			this.height.Size = new System.Drawing.Size(226, 33);
			this.height.TabIndex = 15;
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
			this.backButton.TabIndex = 17;
			this.backButton.Text = "Назад";
			this.backButton.UseVisualStyleBackColor = false;
			this.backButton.Click += new System.EventHandler(this.backButton_Click);
			// 
			// ConeLabel
			// 
			this.ConeLabel.BackColor = System.Drawing.Color.Transparent;
			this.ConeLabel.Dock = System.Windows.Forms.DockStyle.Top;
			this.ConeLabel.Font = new System.Drawing.Font("Montserrat SemiBold", 40F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
			this.ConeLabel.Location = new System.Drawing.Point(0, 0);
			this.ConeLabel.Name = "ConeLabel";
			this.ConeLabel.Size = new System.Drawing.Size(1006, 82);
			this.ConeLabel.TabIndex = 18;
			this.ConeLabel.Text = "Конус";
			this.ConeLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// ConeForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(17F, 36F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
			this.ClientSize = new System.Drawing.Size(1006, 673);
			this.Controls.Add(this.backButton);
			this.Controls.Add(this.label1);
			this.Controls.Add(this.height);
			this.Controls.Add(this.button1);
			this.Controls.Add(this.Area);
			this.Controls.Add(this.label4);
			this.Controls.Add(this.Valume);
			this.Controls.Add(this.Radiuscone);
			this.Controls.Add(this.BallPict);
			this.Controls.Add(this.ConeLabelHeip);
			this.Controls.Add(this.ConeLabel);
			this.Font = new System.Drawing.Font("Montserrat SemiBold", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
			this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
			this.Margin = new System.Windows.Forms.Padding(7);
			this.MaximumSize = new System.Drawing.Size(1024, 720);
			this.MinimumSize = new System.Drawing.Size(1024, 720);
			this.Name = "ConeForm";
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
			this.Text = "AreaAndVolume";
			this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.ConeForm_FormClosing);
			((System.ComponentModel.ISupportInitialize)(this.BallPict)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Button button1;
		private System.Windows.Forms.Label Area;
		private System.Windows.Forms.Label label4;
		private System.Windows.Forms.Label Valume;
		private System.Windows.Forms.TextBox Radiuscone;
		private System.Windows.Forms.PictureBox BallPict;
		private System.Windows.Forms.Label ConeLabelHeip;
		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.TextBox height;
		private System.Windows.Forms.Button backButton;
		private System.Windows.Forms.Label ConeLabel;
	}
}
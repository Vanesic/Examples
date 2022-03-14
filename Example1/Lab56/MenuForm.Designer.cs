
namespace Lab56
{
	partial class Menu
	{
		/// <summary>
		/// Обязательная переменная конструктора.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// Освободить все используемые ресурсы.
		/// </summary>
		/// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Код, автоматически созданный конструктором форм Windows

		/// <summary>
		/// Требуемый метод для поддержки конструктора — не изменяйте 
		/// содержимое этого метода с помощью редактора кода.
		/// </summary>
		private void InitializeComponent()
		{
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Menu));
			this.labelPrivet = new System.Windows.Forms.Label();
			this.subheading = new System.Windows.Forms.Label();
			this.ballForm = new System.Windows.Forms.Button();
			this.ConeForm = new System.Windows.Forms.Button();
			this.paralForm = new System.Windows.Forms.Button();
			this.SuspendLayout();
			// 
			// labelPrivet
			// 
			this.labelPrivet.BackColor = System.Drawing.Color.Transparent;
			this.labelPrivet.Dock = System.Windows.Forms.DockStyle.Top;
			this.labelPrivet.Font = new System.Drawing.Font("Montserrat SemiBold", 20F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
			this.labelPrivet.Location = new System.Drawing.Point(0, 0);
			this.labelPrivet.Margin = new System.Windows.Forms.Padding(7, 0, 7, 0);
			this.labelPrivet.Name = "labelPrivet";
			this.labelPrivet.Size = new System.Drawing.Size(1008, 51);
			this.labelPrivet.TabIndex = 0;
			this.labelPrivet.Text = "Приветствую в приложении \"AreaAndVolume\"!";
			this.labelPrivet.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// subheading
			// 
			this.subheading.BackColor = System.Drawing.Color.Transparent;
			this.subheading.Dock = System.Windows.Forms.DockStyle.Top;
			this.subheading.Location = new System.Drawing.Point(0, 51);
			this.subheading.Margin = new System.Windows.Forms.Padding(7, 0, 7, 0);
			this.subheading.Name = "subheading";
			this.subheading.Size = new System.Drawing.Size(1008, 74);
			this.subheading.TabIndex = 1;
			this.subheading.Text = "Пожалуйста, выберете фигуру, объём и площадь поверхности которой, вы хотите вычис" +
    "лить";
			this.subheading.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// ballForm
			// 
			this.ballForm.BackColor = System.Drawing.SystemColors.ButtonHighlight;
			this.ballForm.Cursor = System.Windows.Forms.Cursors.Hand;
			this.ballForm.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.ballForm.Image = ((System.Drawing.Image)(resources.GetObject("ballForm.Image")));
			this.ballForm.Location = new System.Drawing.Point(12, 128);
			this.ballForm.Name = "ballForm";
			this.ballForm.Size = new System.Drawing.Size(314, 541);
			this.ballForm.TabIndex = 2;
			this.ballForm.Text = "Шар";
			this.ballForm.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
			this.ballForm.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText;
			this.ballForm.UseVisualStyleBackColor = false;
			this.ballForm.Click += new System.EventHandler(this.ballForm_Click);
			// 
			// ConeForm
			// 
			this.ConeForm.BackColor = System.Drawing.SystemColors.ButtonHighlight;
			this.ConeForm.Cursor = System.Windows.Forms.Cursors.Hand;
			this.ConeForm.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.ConeForm.Image = ((System.Drawing.Image)(resources.GetObject("ConeForm.Image")));
			this.ConeForm.Location = new System.Drawing.Point(345, 128);
			this.ConeForm.Name = "ConeForm";
			this.ConeForm.Size = new System.Drawing.Size(314, 541);
			this.ConeForm.TabIndex = 3;
			this.ConeForm.Text = "Конус";
			this.ConeForm.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText;
			this.ConeForm.UseVisualStyleBackColor = false;
			this.ConeForm.Click += new System.EventHandler(this.ConeForm_Click);
			// 
			// paralForm
			// 
			this.paralForm.BackColor = System.Drawing.SystemColors.ButtonHighlight;
			this.paralForm.Cursor = System.Windows.Forms.Cursors.Hand;
			this.paralForm.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.paralForm.Image = ((System.Drawing.Image)(resources.GetObject("paralForm.Image")));
			this.paralForm.Location = new System.Drawing.Point(682, 128);
			this.paralForm.Name = "paralForm";
			this.paralForm.Padding = new System.Windows.Forms.Padding(0, 55, 0, 0);
			this.paralForm.Size = new System.Drawing.Size(314, 541);
			this.paralForm.TabIndex = 4;
			this.paralForm.Text = "Параллелепипед";
			this.paralForm.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
			this.paralForm.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText;
			this.paralForm.UseVisualStyleBackColor = false;
			this.paralForm.Click += new System.EventHandler(this.paralForm_Click);
			// 
			// Menu
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(14F, 29F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
			this.ClientSize = new System.Drawing.Size(1008, 681);
			this.Controls.Add(this.paralForm);
			this.Controls.Add(this.ConeForm);
			this.Controls.Add(this.ballForm);
			this.Controls.Add(this.subheading);
			this.Controls.Add(this.labelPrivet);
			this.Font = new System.Drawing.Font("Montserrat SemiBold", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
			this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
			this.Margin = new System.Windows.Forms.Padding(7);
			this.MaximumSize = new System.Drawing.Size(1024, 720);
			this.MinimumSize = new System.Drawing.Size(1024, 720);
			this.Name = "Menu";
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
			this.Text = "AreaAndVolume";
			this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Menu_FormClosing);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.Label labelPrivet;
		private System.Windows.Forms.Label subheading;
		private System.Windows.Forms.Button ballForm;
		private System.Windows.Forms.Button ConeForm;
		private System.Windows.Forms.Button paralForm;
	}
}



namespace Gary_Engine
{
    partial class ObjectDetection
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(ObjectDetection));
            this.backgroundWorker1 = new System.ComponentModel.BackgroundWorker();
            this.fullAreaSearch = new System.Windows.Forms.Button();
            this.radioLoaded = new System.Windows.Forms.RadioButton();
            this.radioWeb = new System.Windows.Forms.RadioButton();
            this.label3 = new System.Windows.Forms.Label();
            this.selectAll = new System.Windows.Forms.CheckBox();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // fullAreaSearch
            // 
            this.fullAreaSearch.FlatAppearance.MouseDownBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(23)))), ((int)(((byte)(21)))), ((int)(((byte)(32)))));
            this.fullAreaSearch.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(24)))), ((int)(((byte)(22)))), ((int)(((byte)(34)))));
            this.fullAreaSearch.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.fullAreaSearch.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.fullAreaSearch.Location = new System.Drawing.Point(474, 464);
            this.fullAreaSearch.Name = "fullAreaSearch";
            this.fullAreaSearch.Padding = new System.Windows.Forms.Padding(5, 0, 0, 0);
            this.fullAreaSearch.Size = new System.Drawing.Size(235, 45);
            this.fullAreaSearch.TabIndex = 17;
            this.fullAreaSearch.Text = "Detect";
            this.fullAreaSearch.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.fullAreaSearch.UseVisualStyleBackColor = true;
            this.fullAreaSearch.Click += new System.EventHandler(this.fullAreaSearch_Click);
            // 
            // radioLoaded
            // 
            this.radioLoaded.AutoSize = true;
            this.radioLoaded.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.radioLoaded.Location = new System.Drawing.Point(638, 437);
            this.radioLoaded.Name = "radioLoaded";
            this.radioLoaded.Size = new System.Drawing.Size(117, 21);
            this.radioLoaded.TabIndex = 16;
            this.radioLoaded.TabStop = true;
            this.radioLoaded.Text = "Loaded Video";
            this.radioLoaded.UseVisualStyleBackColor = true;
            // 
            // radioWeb
            // 
            this.radioWeb.AutoSize = true;
            this.radioWeb.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.radioWeb.Location = new System.Drawing.Point(542, 437);
            this.radioWeb.Name = "radioWeb";
            this.radioWeb.Size = new System.Drawing.Size(90, 21);
            this.radioWeb.TabIndex = 15;
            this.radioWeb.TabStop = true;
            this.radioWeb.Text = "Web Cam";
            this.radioWeb.UseVisualStyleBackColor = true;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.label3.Location = new System.Drawing.Point(432, 437);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(96, 17);
            this.label3.TabIndex = 14;
            this.label3.Text = "Select Source";
            // 
            // selectAll
            // 
            this.selectAll.AutoSize = true;
            this.selectAll.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.selectAll.Location = new System.Drawing.Point(134, 63);
            this.selectAll.Name = "selectAll";
            this.selectAll.Size = new System.Drawing.Size(141, 21);
            this.selectAll.TabIndex = 18;
            this.selectAll.Text = "Select All Classes";
            this.selectAll.UseVisualStyleBackColor = true;
            this.selectAll.CheckedChanged += new System.EventHandler(this.selectAll_CheckedChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.label1.Location = new System.Drawing.Point(220, 12);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(671, 29);
            this.label1.TabIndex = 19;
            this.label1.Text = "Select Classes and Video source for Full Object Detection ";
            // 
            // ObjectDetection
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(23)))), ((int)(((byte)(21)))), ((int)(((byte)(32)))));
            this.ClientSize = new System.Drawing.Size(1165, 530);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.selectAll);
            this.Controls.Add(this.fullAreaSearch);
            this.Controls.Add(this.radioLoaded);
            this.Controls.Add(this.radioWeb);
            this.Controls.Add(this.label3);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximumSize = new System.Drawing.Size(1183, 577);
            this.MinimumSize = new System.Drawing.Size(1183, 577);
            this.Name = "ObjectDetection";
            this.Text = "ObjectDetection Settings";
            this.Load += new System.EventHandler(this.ObjectDetection_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.ComponentModel.BackgroundWorker backgroundWorker1;
        private System.Windows.Forms.Button fullAreaSearch;
        private System.Windows.Forms.RadioButton radioLoaded;
        private System.Windows.Forms.RadioButton radioWeb;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.CheckBox selectAll;
        private System.Windows.Forms.Label label1;
    }
}
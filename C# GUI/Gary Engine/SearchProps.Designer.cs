
namespace Gary_Engine
{
    partial class SearchProps
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(SearchProps));
            this.trackBar1 = new System.Windows.Forms.TrackBar();
            this.fromLabel = new System.Windows.Forms.Label();
            this.toLabel = new System.Windows.Forms.Label();
            this.trackBar2 = new System.Windows.Forms.TrackBar();
            this.fromvaluelbl = new System.Windows.Forms.Label();
            this.tovaluelbl = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.radioButton1 = new System.Windows.Forms.RadioButton();
            this.radioButton2 = new System.Windows.Forms.RadioButton();
            this.radioButton3 = new System.Windows.Forms.RadioButton();
            this.fullAreaSearch = new System.Windows.Forms.Button();
            this.specificAreaSearch = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.radioButton4 = new System.Windows.Forms.RadioButton();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar2)).BeginInit();
            this.SuspendLayout();
            // 
            // trackBar1
            // 
            this.trackBar1.Location = new System.Drawing.Point(91, 29);
            this.trackBar1.Name = "trackBar1";
            this.trackBar1.Size = new System.Drawing.Size(327, 56);
            this.trackBar1.TabIndex = 0;
            this.trackBar1.Scroll += new System.EventHandler(this.trackBar1_Scroll);
            // 
            // fromLabel
            // 
            this.fromLabel.AutoSize = true;
            this.fromLabel.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.fromLabel.Location = new System.Drawing.Point(26, 29);
            this.fromLabel.Name = "fromLabel";
            this.fromLabel.Size = new System.Drawing.Size(40, 17);
            this.fromLabel.TabIndex = 1;
            this.fromLabel.Text = "From";
            // 
            // toLabel
            // 
            this.toLabel.AutoSize = true;
            this.toLabel.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.toLabel.Location = new System.Drawing.Point(26, 105);
            this.toLabel.Name = "toLabel";
            this.toLabel.Size = new System.Drawing.Size(28, 17);
            this.toLabel.TabIndex = 2;
            this.toLabel.Text = "To ";
            // 
            // trackBar2
            // 
            this.trackBar2.Location = new System.Drawing.Point(91, 105);
            this.trackBar2.Name = "trackBar2";
            this.trackBar2.Size = new System.Drawing.Size(327, 56);
            this.trackBar2.TabIndex = 3;
            this.trackBar2.Scroll += new System.EventHandler(this.trackBar2_Scroll);
            // 
            // fromvaluelbl
            // 
            this.fromvaluelbl.AutoSize = true;
            this.fromvaluelbl.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.fromvaluelbl.Location = new System.Drawing.Point(424, 29);
            this.fromvaluelbl.Name = "fromvaluelbl";
            this.fromvaluelbl.Size = new System.Drawing.Size(33, 17);
            this.fromvaluelbl.TabIndex = 4;
            this.fromvaluelbl.Text = "SEC";
            // 
            // tovaluelbl
            // 
            this.tovaluelbl.AutoSize = true;
            this.tovaluelbl.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.tovaluelbl.Location = new System.Drawing.Point(424, 105);
            this.tovaluelbl.Name = "tovaluelbl";
            this.tovaluelbl.Size = new System.Drawing.Size(33, 17);
            this.tovaluelbl.TabIndex = 5;
            this.tovaluelbl.Text = "SEC";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.label1.Location = new System.Drawing.Point(16, 164);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(172, 17);
            this.label1.TabIndex = 6;
            this.label1.Text = "Minimum Search Threshold";
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(189, 161);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(165, 24);
            this.textBox1.TabIndex = 7;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.label2.Location = new System.Drawing.Point(359, 161);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(104, 17);
            this.label2.TabIndex = 8;
            this.label2.Text = "In Pixels Suared";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.label3.Location = new System.Drawing.Point(26, 194);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(75, 17);
            this.label3.TabIndex = 9;
            this.label3.Text = "Scan Mode";
            // 
            // radioButton1
            // 
            this.radioButton1.AutoSize = true;
            this.radioButton1.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.radioButton1.Location = new System.Drawing.Point(125, 194);
            this.radioButton1.Name = "radioButton1";
            this.radioButton1.Size = new System.Drawing.Size(63, 21);
            this.radioButton1.TabIndex = 10;
            this.radioButton1.TabStop = true;
            this.radioButton1.Text = "Quick";
            this.radioButton1.UseVisualStyleBackColor = true;
            this.radioButton1.CheckedChanged += new System.EventHandler(this.radioButton1_CheckedChanged);
            // 
            // radioButton2
            // 
            this.radioButton2.AutoSize = true;
            this.radioButton2.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.radioButton2.Location = new System.Drawing.Point(215, 194);
            this.radioButton2.Name = "radioButton2";
            this.radioButton2.Size = new System.Drawing.Size(79, 21);
            this.radioButton2.TabIndex = 11;
            this.radioButton2.TabStop = true;
            this.radioButton2.Text = "Regular ";
            this.radioButton2.UseVisualStyleBackColor = true;
            this.radioButton2.CheckedChanged += new System.EventHandler(this.radioButton2_CheckedChanged);
            // 
            // radioButton3
            // 
            this.radioButton3.AutoSize = true;
            this.radioButton3.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.radioButton3.Location = new System.Drawing.Point(318, 194);
            this.radioButton3.Name = "radioButton3";
            this.radioButton3.Size = new System.Drawing.Size(61, 21);
            this.radioButton3.TabIndex = 12;
            this.radioButton3.TabStop = true;
            this.radioButton3.Text = "Deep";
            this.radioButton3.UseVisualStyleBackColor = true;
            this.radioButton3.CheckedChanged += new System.EventHandler(this.radioButton3_CheckedChanged);
            // 
            // fullAreaSearch
            // 
            this.fullAreaSearch.FlatAppearance.MouseDownBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(23)))), ((int)(((byte)(21)))), ((int)(((byte)(32)))));
            this.fullAreaSearch.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(24)))), ((int)(((byte)(22)))), ((int)(((byte)(34)))));
            this.fullAreaSearch.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.fullAreaSearch.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.fullAreaSearch.Location = new System.Drawing.Point(148, 258);
            this.fullAreaSearch.Name = "fullAreaSearch";
            this.fullAreaSearch.Padding = new System.Windows.Forms.Padding(4, 0, 0, 0);
            this.fullAreaSearch.Size = new System.Drawing.Size(206, 45);
            this.fullAreaSearch.TabIndex = 13;
            this.fullAreaSearch.Text = "Search Full Area";
            this.fullAreaSearch.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.fullAreaSearch.UseVisualStyleBackColor = true;
            this.fullAreaSearch.Click += new System.EventHandler(this.fullAreaSearch_Click);
            // 
            // specificAreaSearch
            // 
            this.specificAreaSearch.FlatAppearance.MouseDownBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(23)))), ((int)(((byte)(21)))), ((int)(((byte)(32)))));
            this.specificAreaSearch.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(24)))), ((int)(((byte)(22)))), ((int)(((byte)(34)))));
            this.specificAreaSearch.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.specificAreaSearch.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.specificAreaSearch.Location = new System.Drawing.Point(278, 258);
            this.specificAreaSearch.Name = "specificAreaSearch";
            this.specificAreaSearch.Padding = new System.Windows.Forms.Padding(4, 0, 0, 0);
            this.specificAreaSearch.Size = new System.Drawing.Size(206, 45);
            this.specificAreaSearch.TabIndex = 14;
            this.specificAreaSearch.Text = "Search Specific Area";
            this.specificAreaSearch.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.specificAreaSearch.UseVisualStyleBackColor = true;
            this.specificAreaSearch.Visible = false;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.label4.Location = new System.Drawing.Point(29, 226);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(42, 17);
            this.label4.TabIndex = 15;
            this.label4.Text = "label4";
            // 
            // radioButton4
            // 
            this.radioButton4.AutoSize = true;
            this.radioButton4.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.radioButton4.Location = new System.Drawing.Point(405, 194);
            this.radioButton4.Name = "radioButton4";
            this.radioButton4.Size = new System.Drawing.Size(52, 21);
            this.radioButton4.TabIndex = 16;
            this.radioButton4.TabStop = true;
            this.radioButton4.Text = "Full ";
            this.radioButton4.UseVisualStyleBackColor = true;
            this.radioButton4.CheckedChanged += new System.EventHandler(this.radioButton4_CheckedChanged);
            // 
            // SearchProps
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(23)))), ((int)(((byte)(21)))), ((int)(((byte)(32)))));
            this.ClientSize = new System.Drawing.Size(511, 315);
            this.Controls.Add(this.radioButton4);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.specificAreaSearch);
            this.Controls.Add(this.fullAreaSearch);
            this.Controls.Add(this.radioButton3);
            this.Controls.Add(this.radioButton2);
            this.Controls.Add(this.radioButton1);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.tovaluelbl);
            this.Controls.Add(this.fromvaluelbl);
            this.Controls.Add(this.trackBar2);
            this.Controls.Add(this.toLabel);
            this.Controls.Add(this.fromLabel);
            this.Controls.Add(this.trackBar1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximumSize = new System.Drawing.Size(529, 362);
            this.MinimumSize = new System.Drawing.Size(529, 362);
            this.Name = "SearchProps";
            this.Text = "Search Settings";
            this.Load += new System.EventHandler(this.SearchProps_Load);
            ((System.ComponentModel.ISupportInitialize)(this.trackBar1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar2)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TrackBar trackBar1;
        private System.Windows.Forms.Label fromLabel;
        private System.Windows.Forms.Label toLabel;
        private System.Windows.Forms.TrackBar trackBar2;
        private System.Windows.Forms.Label fromvaluelbl;
        private System.Windows.Forms.Label tovaluelbl;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.RadioButton radioButton1;
        private System.Windows.Forms.RadioButton radioButton2;
        private System.Windows.Forms.RadioButton radioButton3;
        private System.Windows.Forms.Button fullAreaSearch;
        private System.Windows.Forms.Button specificAreaSearch;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.RadioButton radioButton4;
    }
}
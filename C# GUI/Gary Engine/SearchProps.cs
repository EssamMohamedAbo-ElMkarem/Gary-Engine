using System;
using WMPLib;
using System.Windows.Forms;
using System.Threading;
using System.Drawing;

namespace Gary_Engine
{
    public partial class SearchProps : Form
    {
        string main_class;
        string sub_classes;
        bool smart_search;
        string scan_rate = "quick";
        string threshold = "12000";
        string vid_path;
        bool theme;
        string search_text;
        double fromSec;
        double toSec;

        public SearchProps(string main_class, string search_text, bool smart_search, string vid_path, bool theme)
        {
            Console.WriteLine("SMART CONSTRUCTOR CALLED");
            this.main_class = main_class;
            this.search_text = search_text; // equals sub classes in case of original search
            this.theme = theme;
            this.vid_path = vid_path;
            this.smart_search = smart_search;
            InitializeComponent();
            
            foreach (Control c in this.Controls)
            {
                UiController.UpdateColorControls(this, c, theme);
            }
            
            label4.Text = "";
        }

        private void SearchProps_Load(object sender, EventArgs e)
        {

            ToolTip toolTip = new ToolTip();

            // Set up the delays for the ToolTip.
            toolTip.ToolTipTitle = "Gary Tips";
            toolTip.UseFading = true;
            toolTip.UseAnimation = true;
            toolTip.IsBalloon = true;
            toolTip.AutoPopDelay = 5000;
            toolTip.InitialDelay = 1000;
            toolTip.ReshowDelay = 500;
            // Force the ToolTip text to be displayed whether or not the form is active.
            toolTip.ShowAlways = true;

            // Set up the ToolTip text for the Button and Checkbox.
            toolTip.SetToolTip(this.radioButton1, "This mode is used to process the video with a low sampling rate resulting in performance boosting and noticeble accuracy loss.");
            toolTip.SetToolTip(this.radioButton2, "This mode is used to process the video with a medium sampling rate resulting in performance boosting a little bit and slight accuracy loss.");
            toolTip.SetToolTip(this.radioButton3, "This mode is used to process the entire video resulting in full deep search and no accuracy loss.");

            var player = new WindowsMediaPlayer();
            var clip = player.newMedia(vid_path);
            Console.WriteLine(TimeSpan.FromSeconds(clip.duration));
            trackBar1.Minimum = 0;
            trackBar1.Maximum = (int)clip.duration;
            trackBar2.Minimum = 0;
            trackBar2.Maximum = (int)clip.duration;
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            fromvaluelbl.Text = "SEC " + TimeSpan.FromSeconds(trackBar1.Value).ToString();
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            tovaluelbl.Text = "SEC " + TimeSpan.FromSeconds(trackBar2.Value).ToString();
        }

        private void fullAreaSearch_Click(object sender, EventArgs e)
        {
            fromSec = trackBar1.Value;
            toSec = trackBar2.Value;
            threshold = textBox1.Text.ToString();
            
            if(radioButton1.Checked == true)
            {
                scan_rate = "quick";
            }
            else if(radioButton2.Checked == true)
            {
                scan_rate = "normal";
            }
            else if(radioButton3.Checked == true)
            {
                scan_rate = "deep";
            }
            else if (radioButton4.Checked == true)
            {
                scan_rate = "full";
            }
            else
            {
                MessageBox.Show("Please, Choose a suitable rate(quick is default)", "Warning");
            }

            if (smart_search) 
            {
                
                PythonConnect pc = new PythonConnect();
                ThreadStart thread_start = new ThreadStart(() => { pc.VSE(vid_path, main_class, search_text, "smart", scan_rate, fromSec.ToString(), toSec.ToString(), threshold); });
                Thread thread = new Thread(thread_start);
                thread.Start();
            }
            else
            {
                PythonConnect pc = new PythonConnect();
                ThreadStart thread_start = new ThreadStart(() => { pc.VSE(vid_path, main_class, search_text, "original", scan_rate, fromSec.ToString(), toSec.ToString(), threshold); });
                Thread thread = new Thread(thread_start);
                thread.Start();
                // Delay for 2.5 seconds to activate recommender system
            }
            Thread.Sleep(2500);
            DialogResult dialogResult = MessageBox.Show("Would you like Gary to suggest something to do while we take care of what you're looking for?", "Enjoy with Gary!", 
                MessageBoxButtons.YesNoCancel, MessageBoxIcon.Question);
            if(dialogResult == DialogResult.Yes)
            {
                RecommenderSysQ recommenderSys = new RecommenderSysQ(theme);
                recommenderSys.Show();
            }
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            label4.Text = "Medium scan depth with average accuracy";
            label4.ForeColor = Color.Yellow;
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            label4.Text = "Shallaw scan depth with poor accuracy";
            label4.ForeColor = Color.Green;
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            label4.Text = "Time Consuming with Guranteed accuracy";
            label4.ForeColor = Color.Red;
        }

        private void radioButton4_CheckedChanged(object sender, EventArgs e)
        {
            label4.Text = "FULL SCAN DROPS NO OCCURENCE";
            label4.ForeColor = Color.Red;
        }
    }
}

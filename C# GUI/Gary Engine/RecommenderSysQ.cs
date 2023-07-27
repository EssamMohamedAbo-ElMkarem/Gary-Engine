using System;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace Gary_Engine
{
    public partial class RecommenderSysQ : Form
    {
        public RecommenderSysQ(bool theme)
        {
            InitializeComponent();
            label5.Text = "";
            
            foreach (Control c in this.Controls)
            {
                UiController.UpdateColorControls(this, c, theme);
            }
            
            MessageBox.Show("This feature requires internet access", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }

        private void yes_Click(object sender, EventArgs e)
        {
            try
            {
                string feeling_message = richTextBox1.Text;
                string type = "";
                string duration = "";
                string url = "";
                if (feeling_message != "")
                {
                    if (radioButton1.Checked == false && radioButton2.Checked == false && radioButton3.Checked == false)
                    {
                        MessageBox.Show("Please, choose the conten type", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    }
                    else if (radioButton4.Checked == false && radioButton5.Checked == false && radioButton6.Checked == false)
                    {
                        MessageBox.Show("Please, choose the conten duration", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    }
                    else
                    {
                        if (radioButton1.Checked == true)
                        {
                            type = "song";
                        }
                        else if (radioButton2.Checked == true)
                        {
                            type = "video";
                        }
                        else if (radioButton3.Checked == true)
                        {
                            type = "article";
                        }

                        if (radioButton4.Checked == true)
                        {
                            duration = "long";
                        }
                        else if (radioButton5.Checked == true)
                        {
                            duration = "medium";
                        }
                        else if (radioButton6.Checked == true)
                        {
                            duration = "short";
                        }
                        Console.WriteLine("{0} {1} {2}", feeling_message, type, duration);
                        label5.Text = "Gary is thinking now....";
                        label5.ForeColor = Color.Yellow;
                        PythonConnect pc = new PythonConnect();
                        pc.Recommender(feeling_message, type, duration);
                        while (File.Exists("tmp_outputs/recommender_outputs/recommender_output.json") == false)
                        {
                            Console.WriteLine("Waiting for JSON file to be created");
                        }
                        dynamic output = FilesHandler.returnFromJson("tmp_outputs/recommender_outputs/recommender_output.json");
                        Console.WriteLine(output);
                        label5.Text = output[0]["title"];
                        label5.ForeColor = Color.Green;
                        Console.WriteLine(label5.Text);
                        url = output[0]["link"];
                        System.Diagnostics.Process.Start(url);
                    }
                }
                else
                {
                    MessageBox.Show("Please, talk about what you are feeling to help Gary suggest the suitable content", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }
            catch (Exception)
            {
                MessageBox.Show("Something went wrong. Please, try again later", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void tryAgain_Click(object sender, EventArgs e)
        {
            string url = "";
            Random random = new Random();
            int i = random.Next(1, 11);
            dynamic output = FilesHandler.returnFromJson("tmp_outputs/recommender_outputs/recommender_output.json");
            Console.WriteLine(output);
            label5.Text = output[i]["title"];
            label5.ForeColor = Color.Green;
            Console.WriteLine(label5.Text);
            url = output[i]["link"];
            System.Diagnostics.Process.Start(url);
        }

        private void RecommenderSysQ_Load(object sender, EventArgs e)
        {

        }
    }
}

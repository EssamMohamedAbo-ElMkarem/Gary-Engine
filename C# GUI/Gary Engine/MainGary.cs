using System;
using System.IO;
using System.Threading;
using System.Drawing;
using System.Collections.Generic;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace Gary_Engine
{
    public partial class MainGary : Form
    {
        [DllImport("winmm.dll", EntryPoint = "mciSendStringA", ExactSpelling = true, CharSet = CharSet.Ansi, SetLastError = true)]
        private static extern int record(string lpstrCommand, string lpstrReturnString, int uReturnLength, int hwndCallback);
        private Dictionary<ComboBox, string> comboDict = new Dictionary<ComboBox, string>();
        private bool darktheme = true;
        private string currentFile = ""; // Current running video
        private string vid_path = "";
       
        public MainGary(bool theme)
        {
            InitializeComponent();
            if(theme == false)
            {
                foreach (Control c in this.Controls)
                {
                    c.BackColor = Color.White;
                    c.ForeColor = Color.Blue;
                }
            }
            HideSubMenu();
        }

        
        // Hide all submenues
        private void HideSubMenu()
        {
            panel1.Visible = false;
            panelMediaSubMenu.Visible = false;
            panelOccurancesSubMenu.Visible = false;
        }

        // Show clicked submenu
        private void ShowSubMenu(Panel subMenu)
        {
            if (subMenu.Visible == false)
            {
                HideSubMenu();
                subMenu.Visible = true;
            }
            else
                subMenu.Visible = false;
        }

        private void btnMedia_Click(object sender, EventArgs e)
        {
            ShowSubMenu(panelMediaSubMenu);
        }

        private void btnOpenFile_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "Video Files (*.avi;*.mpg;*.mpeg)|*.avi;*.mpg;*.mpeg";
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                currentFile = openFileDialog.FileName;
                axWindowsMediaPlayer1.URL = currentFile;
            }
            HideSubMenu();
        }

        private void btnDisplayOutput_Click(object sender, EventArgs e)
        {
            try
            {
                axWindowsMediaPlayer1.URL = Path.GetDirectoryName(System.Reflection.Assembly.GetEntryAssembly().Location) + "/Python/Lib/site-packages/Gary/garySE/output_dir/output_video.avi";
            }
            catch(Exception)
            {
                MessageBox.Show("It seems like there is no output generated yet", "waring", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            HideSubMenu();
        }

        private void OccurancesBtn_Click(object sender, EventArgs e)
        {
            OccurancesDetails.Items.Clear();
            string line = "";

            ShowSubMenu(panelOccurancesSubMenu);
            try
            {
                using (var reader = new System.IO.StreamReader(Path.GetDirectoryName(System.Reflection.Assembly.GetEntryAssembly().Location) + "/Python/Lib/site-packages/Gary/garySE/output_dir/TimeStamps.txt"))
                {
                    while ((line = reader.ReadLine()) != null)
                    {
                        string[] line_arr = line.Split();
                        string occurance = line_arr[0].Replace('_', ' ');
                        line = occurance + " from " + line_arr[1] + " to " + line_arr[2];
                        OccurancesDetails.Items.Add(line);
                    }
                }
            }
            catch(Exception ex)
            {
                Console.WriteLine(ex);
                MessageBox.Show("There are no occurances yet!", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }
        
        private void btnHelp_Click(object sender, EventArgs e)
        {
            ShowSubMenu(panel1);
            
        }
        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        // Perform full object detection for the chosen video
        private void objectdetection_Click(object sender, EventArgs e)
        {
            ObjectDetection od = new ObjectDetection(currentFile, darktheme);
            od.Show();
        }

        private void nerfbtn_Click(object sender, EventArgs e)
        {
            string image_path = "";
            openFileDialogNerf.Filter = "Image|*.jpg;*.jpeg;*.png;";  
            if (openFileDialogNerf.ShowDialog() == DialogResult.OK){
                image_path = openFileDialogNerf.FileName; //set image path to the file dialog name
            }
            if(image_path != ""){
                
                    PythonConnect pc = new PythonConnect();
                    ThreadStart thread_start = new ThreadStart(() => { pc.RunPifuhd(image_path); });
                    Thread thread = new Thread(thread_start);
                    thread.Start();
            }
        }

        private void emotion_Click(object sender, EventArgs e)
        {
            vid_path = currentFile;
            if (vid_path == "")
            {
                MessageBox.Show("Please, Enter a valid video path", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                PythonConnect pc = new PythonConnect();
                ThreadStart thread_start = new ThreadStart(() => { pc.OnTheSpot(vid_path); });
                Thread thread = new Thread(thread_start);
                thread.Start();
            }
            /*
            var confirmResult = MessageBox.Show("Yes: Loaded Video No: WebCam", "You want to use the loaded video?",
                MessageBoxButtons.YesNoCancel);
            if (confirmResult == DialogResult.Yes)
            {
                vid_path = currentFile;
                if (vid_path == "")
                {
                    MessageBox.Show("Please, Enter a valid video path", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
                else
                {
                    PythonConnect pc = new PythonConnect();
                    ThreadStart thread_start = new ThreadStart(() => { pc.EmotionDetection(vid_path); });
                    Thread thread = new Thread(thread_start);
                    thread.Start();
                }
            }
            else if (confirmResult == DialogResult.No)
            {
                vid_path = "0";
                PythonConnect pc = new PythonConnect();
                ThreadStart thread_start = new ThreadStart(() => { pc.EmotionDetection(vid_path); });
                Thread thread = new Thread(thread_start);
                thread.Start();
            }
            */
        }

        private void process_query_Click_1(object sender, EventArgs e)
        {
            string path = currentFile;
            string main_class = "";
            string sub_classes = "";

            if (currentFile == "")
            {
                MessageBox.Show("Please, Load a video first", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                if (radioSmart.Checked == true)
                {
                    Console.WriteLine("Inside smart search");
                    string query_text = queryText.Text;
                    string main_class_list = "['" + comboBox1.Text + "']";
                    SearchProps sp = new SearchProps(main_class_list.ToLower(), query_text, true, path, darktheme);
                    sp.Show();
                }
                else if(radioOriginal.Checked == true)
                {
                    main_class = comboBox1.Text;
                    string main_class_list = "['" + comboBox1.Text + "']";
                    if (main_class != "")
                    {
                        if (main_class == "Person")
                        {
                            ComboBox[] comboBoxes = { comboBox2, comboBox3, comboBox4, comboBox5, comboBox6, comboBox7 };
                            foreach (ComboBox comboBox in comboBoxes)
                            {
                                if (comboBox.Text == "")
                                {
                                    continue;
                                }
                                else
                                {
                                    sub_classes += comboDict[comboBox] + ":" + comboBox.Text.ToLower() + ",";
                                }
                            }
                            sub_classes = sub_classes.Remove(sub_classes.Length - 1);
                            sub_classes += "";
                        }
                        else if (main_class == "Car")
                        {
                            sub_classes = "car_type:" + comboBox2.Text + ",color:" + comboBox3.Text;
                        }
                        SearchProps sp = new SearchProps(main_class_list.ToLower(), sub_classes, false, path, darktheme);
                        sp.Show();
                    }
                    else
                    {
                        MessageBox.Show("Please, Choose a valid main class", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    }
                }
                Console.WriteLine(sub_classes.ToLower());
            }
        }

        private void MainGary_Load(object sender, EventArgs e)
        {
           
            comboDict.Add(comboBox2, "gender");
            comboDict.Add(comboBox3, "avg_age");
            comboDict.Add(comboBox4, "hat");
            comboDict.Add(comboBox5, "Glasses");
            comboDict.Add(comboBox7, "mask");
            comboDict.Add(comboBox6, "clothes");

            radioOriginal.Checked = true;
            radioSmart.Checked = false;
            originalSearchActivate();

            //Tool tips section
            // Create the ToolTip and associate with the Form container.
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
            toolTip.SetToolTip(this.objectdetection, "This button runs full object detection over the video already loaded in the media player or the web cam embedded in your machine.");
            toolTip.SetToolTip(this.radioOriginal, "You can choose the prefered classes you want to search for and make sure to choose not interested if the feature is out of your search query.");
            toolTip.SetToolTip(this.radioSmart, "Gary gives you the ability to provide an in-English generic search query and it will take care of the rest for you.");
            toolTip.SetToolTip(this.process_query, "Start searching for what you want.");
            toolTip.SetToolTip(this.emotion, "Gary gives you the ability to pause a real-time video and click on any spesific object then give you a detailed analysis for the object.");
            toolTip.SetToolTip(this.faceenhance, "If you have a low quality face image don't worry Gary will take care of it and will super-resolute it.");
            toolTip.SetToolTip(this.actiondetection, "This runs the action detection capabilities of Gary so watch yourself..Gary knows what you're doing inside the video.");
            toolTip.SetToolTip(this.nerfbtn, "All you have to do is to upload your 2D image leave the 3D generation of the entire scene for Gary.");
            toolTip.SetToolTip(this.ontheSpot, "This runs Video Summarization feature");
        }

        private void radioOriginal_CheckedChanged(object sender, EventArgs e)
        {
            originalSearchActivate();
        }

        private void radioSmart_CheckedChanged(object sender, EventArgs e)
        {
            smartSearchActivated();
        }

        private void smartSearchActivated()
        {
            queryText.Visible = true;
            comboBox1.Visible = true;
            comboBox2.Visible = false;
            comboBox3.Visible = false;
            comboBox4.Visible = false;
            comboBox5.Visible = false;
            comboBox6.Visible = false;
            comboBox7.Visible = false;
        }

        private void originalSearchActivate()
        {
            queryText.Visible = false;
            comboBox1.Visible = true;
            comboBox2.Visible = true;
            comboBox3.Visible = true;
            comboBox4.Visible = true;
            comboBox5.Visible = true;
            comboBox6.Visible = true;
            comboBox7.Visible = true;

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (comboBox1.Text == "Person")
            {
                comboBox2.Items.Clear();
                comboBox3.Items.Clear();
                comboBox4.Items.Clear();
                comboBox5.Items.Clear();
                comboBox6.Items.Clear();
                comboBox7.Items.Clear();
                /*
                comboBox3.Visible = true;
                comboBox4.Visible = true;
                comboBox5.Visible = true;
                comboBox6.Visible = true;
                comboBox7.Visible = true;
                */
                comboBox2.Items.Add("Male");
                comboBox2.Items.Add("Female");
                comboBox2.Items.Add("NotInterested");

                comboBox3.Items.Add("Young");
                comboBox3.Items.Add("Youth");
                comboBox3.Items.Add("Old");
                comboBox3.Items.Add("NotInterested");

                comboBox4.Items.Add("Without_Cap");
                comboBox4.Items.Add("Cap");
                comboBox4.Items.Add("Capuchon");
                comboBox4.Items.Add("IceCap");
                comboBox4.Items.Add("Helmet");
                comboBox4.Items.Add("Hijab");
                comboBox4.Items.Add("Bonnet");
                comboBox4.Items.Add("NotInterested");

                comboBox5.Items.Add("With_Glasses");
                comboBox5.Items.Add("Without_Glasses");
                comboBox5.Items.Add("NotInterested");

                comboBox6.Items.Add("T-Shirt");
                comboBox6.Items.Add("Shirt");
                comboBox6.Items.Add("Pants");
                comboBox6.Items.Add("Shorts");
                comboBox6.Items.Add("Jacket");
                comboBox6.Items.Add("Hijab");
                comboBox6.Items.Add("Dress");
                comboBox6.Items.Add("Suit");
                comboBox6.Items.Add("Skirt");
                comboBox6.Items.Add("Bag");
                comboBox6.Items.Add("Hoodie");
                comboBox6.Items.Add("NotInterested");

                comboBox7.Items.Add("With_Mask");
                comboBox7.Items.Add("Without_Mask");
                comboBox7.Items.Add("NotInterested");
            }
            else if(comboBox1.Text == "Car")
            {
                comboBox4.Visible = false;
                comboBox5.Visible = false;
                comboBox6.Visible = false;
                comboBox7.Visible = false;

                comboBox2.Items.Clear();
                string[] carBodyTypes = new string[] { "Van", "SUV", "Minivan", "Cab", "Wagon", "Sedan", "Hatchback", "Coupe", "Convertible", "Other"};
                foreach(string type in carBodyTypes)
                {
                    comboBox2.Items.Add(type);
                }
                comboBox3.Items.Add("Red");
                comboBox3.Items.Add("Green");
                comboBox3.Items.Add("Blue");
                comboBox3.Items.Add("White");
                comboBox3.Items.Add("Black");
                comboBox3.Items.Add("Yellow");
            }
        }

        private void newGary_Click(object sender, EventArgs e)
        {
            MainGary mg = new MainGary(darktheme);
            mg.Show();
        }

        private void OccurancesDetails_SelectedIndexChanged(object sender, EventArgs e)
        {
            var occurance = OccurancesDetails.Items[OccurancesDetails.SelectedIndex].ToString();
            string[] occurance_details = occurance.Split();
            string frame_name = occurance_details[0];
            float frame_second = float.Parse(occurance_details[3]);
            axWindowsMediaPlayer1.Ctlcontrols.currentPosition = frame_second;
        }

        private void actiondetection_Click(object sender, EventArgs e)
        {
            bool sports = false;
            var confirmResult = MessageBox.Show("Yes: Sports Activities No: Normal Activities", "You want to use the loaded video?",
                MessageBoxButtons.YesNoCancel);
            if (confirmResult == DialogResult.Yes)
            {
                sports = true;
            }
            else if (confirmResult == DialogResult.No)
            {
                sports = false;
            }
            vid_path = currentFile;
            if (vid_path == "")
            {
                MessageBox.Show("Please, Enter a valid video path", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                PythonConnect pc = new PythonConnect();
                ThreadStart thread_start = new ThreadStart(() => { pc.YOWO(vid_path, sports); });
                Thread thread = new Thread(thread_start);
                thread.Start();
            }
        }

        private void faceenhance_Click(object sender, EventArgs e)
        {
            string input_path = "";
            openFileDialog1.Filter = "Image Files|*.jpg;*.jpeg;*.png;"; 
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                input_path = openFileDialog1.FileName; 
            }
            if (input_path != "")
            {                 
                    PythonConnect pc = new PythonConnect();
                    ThreadStart thread_start = new ThreadStart(() => { pc.FaceRestoration(input_path); });
                    Thread thread = new Thread(thread_start);
                    thread.Start();
            }
            else
            {
                MessageBox.Show("Enter a valid face image path", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void full_object_detection_help_Click(object sender, EventArgs e)
        {
            showTutorial("Full Object Detection Tutorial", "1- Full object detection feature utilizes deep learning vision algorithm in order to retrieve all existing objects inside a video input with bounding boxes around them" +
                Environment.NewLine  + Environment.NewLine + "2- You have to set the appropriate settings for your analysis by choosing the specific object classes found inside the input video" +
                Environment.NewLine + Environment.NewLine + "3- You have the option to choose whether you want a visualization report at the end of the analysis or not generating bar plot and pie plot demonstrating each class percentage from the video");
        }
        private void showTutorial(string head, string message)
        {
            MessageBox.Show(message, head, MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void full_action_detection_help_Click(object sender, EventArgs e)
        {
            showTutorial("Full Action Detection Tutorial", "1- Full action detection feature utilizes deep learning vision algorithm in order to retrieve all existing actions inside an input video with bounding boxes around them" +
                Environment.NewLine + Environment.NewLine + "2- You have to set the appropriate settings for your analysis by choosing whether the input video from a sports domain or every day actions domain");
        }

        private void face_enhancement_help_Click(object sender, EventArgs e)
        {
            showTutorial("Face Enhancement Tutorial", "1- Face enhancement feature utilizes a deep learning generative model in order to super resolute face images" +
                Environment.NewLine + Environment.NewLine + "2- This feature can be super critical in the security fields specially in the analysis of not easily visible face images from CCTV cams domain" + 
                Environment.NewLine + Environment.NewLine + "3- You have the option to upload a low resolution(low quality) face image and Gary will produce the output high resolution image and display the output on finishing its generation process");
        }

        private void pifuhd_help_Click(object sender, EventArgs e)
        {
            showTutorial("3-D Human Reconstruction Tutorial", "1- 3-D Human Reconstruction enables you to upload an image of a human then generates 3-D reconstruction for this human" +
                Environment.NewLine + Environment.NewLine + "2- The output is the displayed inside Blender 3-D engine which is an open source Python-built 3-D studio");
        }
        private void emotion_detection_help_Click(object sender, EventArgs e)
        {
            showTutorial("Video Summarization", "1- All you have to do is to run this feature which will summarize the video and also speak the output out load if you want.");
        }
        private void on_the_spot_help_Click(object sender, EventArgs e)
        {
            showTutorial("Detection On the Spot", "1- All you have to do is to click on the object of interest from the video" +
                Environment.NewLine + Environment.NewLine + "2- Provided with a new screen the used will choose one of three options to apply on the object" +
                Environment.NewLine + Environment.NewLine + "3- Output will be displayed on a user friendly window to enhance your experience");
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if(checkBox1.Checked == true)
            {
                darktheme = false;
                
                foreach (Control c in this.Controls)
                {
                    UiController.UpdateColorControls(this, c, darktheme);
                }
            }
            else
            {
                darktheme = true;
                checkBox1.Text = "Light Mode";

                foreach (Control c in this.Controls)
                {
                    UiController.UpdateColorControls(this, c, darktheme);
                }
            }
        }

        private void ontheSpot_Click(object sender, EventArgs e)
        {
            if (currentFile != "")
            {
                PythonConnect pc = new PythonConnect();
                ThreadStart thread_start = new ThreadStart(() => { pc.SummarizeVideo(currentFile); });
                Thread thread = new Thread(thread_start);
                thread.Start();
            }
            else
            {
                MessageBox.Show("Please, Load a video first", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        
    }
}

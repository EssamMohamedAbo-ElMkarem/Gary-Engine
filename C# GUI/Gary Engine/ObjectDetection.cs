using System;
using System.Drawing;
using System.Threading;
using System.Windows.Forms;
using System.Collections.Generic;

namespace Gary_Engine
{
    public partial class ObjectDetection : Form
    {
        string vid_path = "0";
        bool theme;
        Dictionary<string, string> Class2Index = new Dictionary<string, string>()
            {
                {"person", "0"},
                {"bicycle", "1"},
                {"car", "2"},
                {"motorcycle", "3"},
                {"airplane", "4"},
                {"bus", "5"},
                {"train", "6"},
                {"truck", "7"},
                {"boat", "8"},
                {"traffic light", "9"},
                {"fire hydrant", "10"},
                {"stop sign", "11"},
                {"parking meter", "12"},
                {"bench", "13"},
                {"bird", "14"},
                {"cat", "15"},
                {"dog", "16"},
                {"horse", "17"},
                {"sheep", "18"},
                {"cow", "19"},
                {"elephant", "20"},
                {"bear", "21"},
                {"zebra", "22"},
                {"giraffe", "23"},
                {"backpack", "24"},
                {"umbrella", "25"},
                {"handbag", "26"},
                {"tie", "27"},
                {"suitcase", "28"},
                {"frisbee", "29"},
                {"skis", "30"},
                {"snowboard", "31"},
                {"sports ball", "32"},
                {"kite", "33"},
                {"baseball bat", "34"},
                {"baseball glove", "35"},
                {"skateboard", "36"},
                {"surfboard", "37"},
                {"tennis racket", "38"},
                {"bottle", "39"},
                {"wine glass", "40"},
                {"cup", "41"},
                {"fork", "42"},
                {"knife", "43"},
                {"spoon", "44"},
                {"bowl", "45"},
                {"banana", "46"},
                {"apple", "47"},
                {"sandwich", "48"},
                {"orange", "49"},
                {"broccoli", "50"},
                {"carrot", "51"},
                {"hot dog", "52"},
                {"pizza", "53"},
                {"donut", "54"},
                {"cake", "55"},
                {"chair", "56"},
                {"couch", "57"},
                {"potted plant", "58"},
                {"bed", "59"},
                {"dining table", "60"},
                {"toilet", "61"},
                {"tv", "62"},
                {"laptop", "63"},
                {"mouse", "64"},
                {"remote", "65"},
                {"keyboard", "66"},
                {"cell phone", "67"},
                {"microwave", "68"},
                {"oven", "69"},
                {"toaster", "70"},
                {"sink", "71"},
                {"refrigerator", "72"},
                {"book", "73"},
                {"clock", "74"},
                {"vase", "75"},
                {"scissors", "76"},
                {"teddy bear", "77"},
                {"hair drier", "78"},
                {"toothbrush", "79"}
            };
        public ObjectDetection( string vid_path, bool theme)
        {
            InitializeComponent();
            
            foreach (Control c in this.Controls)
            {
                UiController.UpdateColorControls(this, c, theme);
            }
            this.theme = theme;
            this.vid_path = vid_path;
        }
        private void ObjectDetection_Load(object sender, EventArgs e)
        {
            string[] classes = new string[] {"person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light",
               "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
               "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee",
               "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
               "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
               "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch",
               "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard",
               "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase",
               "scissors", "teddy bear", "hair drier", "toothbrush"};

            


            int i = 1, j = 5;
            foreach(string _class in classes)
            {
                CheckBox checkBox = new CheckBox();
                checkBox.ForeColor = Color.White;
                checkBox.AutoSize = true;
                checkBox.Location = new Point(i * 100, j * 20);
                checkBox.Text = _class;
                this.Controls.Add(checkBox);
                i++;
                if (i % 8 == 0)
                {
                    j++;
                    i = 1;
                }
            }
            foreach (Control c in this.Controls)
            {
                UiController.UpdateColorControls(this, c, theme);
            }
        }

        private void selectAll_CheckedChanged(object sender, EventArgs e)
        {
            bool status;
            if(selectAll.Checked == true)
            {
                status = true;
            }
            else
            {
                status = false;
            }
            foreach (Control c in this.Controls)
            {
                if (c is CheckBox)
                {
                    ((CheckBox)c).Checked = status;
                }
            }
        }

        private void fullAreaSearch_Click(object sender, EventArgs e)
        {
            string video_path_curr = "";
            if (radioWeb.Checked)
            {
                video_path_curr = "0";
            }
            else if (radioLoaded.Checked)
            {
                video_path_curr = vid_path;
            }
      
            bool check_status = false;
            List <string> checked_classes = new List<string> { };
            string classes = "";
            string script_arg;
            foreach (Control c in this.Controls)
            {
                if (c is CheckBox)
                {
                    if (((CheckBox)c).Checked == true)
                    {
                        check_status = true;
                        break;
                    }
                    else
                    {
                        check_status = false;
                    }
                }
            }
            if (check_status)
            {
                if (selectAll.Checked == true)
                {
                    script_arg = "yolov7-main\\detect.py --weights yolov7-main\\yolov7-tiny.pt --conf 0.5 --img-size 640 --view-img --source \"" + video_path_curr + "\"";
                }
                else
                {
                    foreach (Control c_ck in this.Controls)
                    {
                        if (c_ck is CheckBox && ((CheckBox)c_ck).Text != "Select All Classes" && ((CheckBox)c_ck).Checked)
                        {
                          
                            classes += "\"" + Class2Index[(((CheckBox)c_ck).Text)] + "\"" +  " ";
                        }
                    }
                    script_arg = "yolov7-main\\detect.py --weights yolov7-main\\yolov7-tiny.pt --conf 0.5 --img-size 640 --view-img --source \"" + video_path_curr + "\" --classes " + classes;
                }
                Console.WriteLine(script_arg);
                
                FilesHandler.Empty(@"yolov7-main\runs\detect");
                PythonConnect pc = new PythonConnect();
                ThreadStart thread_start = new ThreadStart(() => { pc.FullObjectDetection(script_arg); });
                Thread thread = new Thread(thread_start);
                thread.Start();
                
            }
            else
            {
                MessageBox.Show("Please, Choose at least one class to search for", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }
    }
}

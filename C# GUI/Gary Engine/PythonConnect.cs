using System.Threading;
using System.IO;
using System;


namespace Gary_Engine
{
    class PythonConnect
    {
       
        public void FullObjectDetection(string path)
        {
            // Function to call yolo 7 for full object detection
            ProcessExec process;
            process = new ProcessExec(@"Python\python.exe", path);
            process.ProcessCmd(false);
        }

        public void StyleTransfer(string content, string style, ushort epochs)
        {
            // Function to call style transfer script
            ProcessExec process;
            process = new ProcessExec(@"Python\python.exe", "Scripts\\styletransfer.py --content \"" + content + "\" --style \"" + style + "\" --epochs \"" + epochs.ToString() + "\"");
            process.ProcessCmd(true);
        }

        public void RunPifuhd(string image_path)
        {
            // Function to call NeRF script
            ProcessExec process;
            process = new ProcessExec("Python\\python.exe", "pifuhd\\run_pifuhd.py --image_path \"" + image_path + "\" ");
            process.ProcessCmd(true);
        }
        public void EmotionDetection(string path)
        {
            // Function to call Face Expressions Classification script
            ProcessExec process;
            process = new ProcessExec("Python\\python.exe", "Scripts\\FEC.py --path \"" + path + "\"");
            process.ProcessCmd(true);
        }
        public void VSE(string path, string main_class, string sub_classes, string type, string scan_rate, string start, string end, string threshold)
        {
            // Function to call main video search engine script
            Console.WriteLine( "Scripts\\MAINv3.py --video_path \"" + path + "\" --main_class \"" + main_class + "\" --search_txt \"" + sub_classes + "\" --scan_rate \"" + scan_rate + "\" --search_type \"" + type + "\" --start \"" + start + "\" --end \"" + end + "\" --threshold \"" + threshold + "\"");
            ProcessExec process;
            process = new ProcessExec(@"Python\python.exe", "Scripts\\MAINv3.py --video_path \"" + path + "\" --main_class \"" + main_class + "\" --search_txt \"" + sub_classes + "\" --scan_rate \"" + scan_rate + "\" --search_type \"" + type + "\" --start \"" + start + "\" --end \"" + end + "\" --threshold \"" + threshold + "\"");
            process.ProcessCmd(true);
        }

        public void SMARTVSE(string path, string search_text, string scan_rate, string trim, string start, string end, string threshold, string crop = "False", string p1 = "0, 0", string p2 = "0, 0")
        {
            // Function to call main video search engine script
            Console.WriteLine("Scripts\\SMART_MAIN.py --video_path \"" + path + "\" --search_text \"" + search_text + "\" --scan_rate \"" + scan_rate + "\" --trim \"" + trim + "\" --start \"" + start + "\" --end \"" + end + "\" --threshold \"" + threshold + "\" --crop \"" + crop + "\" --p1 \"" + p1 + "\" --p2 \"" + p2 + "\"");
            ProcessExec process;
            process = new ProcessExec(@"Python\python.exe", "Scripts\\SMART_MAIN.py --video_path \"" + path + "\" --search_text \"" + search_text + "\" --scan_rate \"" + scan_rate + "\" --trim \"" + trim + "\" --start \"" + start + "\" --end \"" + end + "\" --threshold \"" + threshold + "\" --crop \"" + crop + "\" --p1 \"" + p1 + "\" --p2 \"" + p2 + "\"");
            process.ProcessCmd(true);
        }

        public void MainSearchAlgorithm(string path, string main_class, string sub_classes)
        {
            PythonConnect pc = new PythonConnect();

            ThreadStart thread1_start = new ThreadStart(() => { pc.THREAD_1("\"" + path + "\""); });
            Thread thread1 = new Thread(thread1_start);
            
            ThreadStart thread2_start = new ThreadStart(() => { pc.THREAD_2("\"" + main_class + "\""); });
            Thread thread2 = new Thread(thread2_start);

            ThreadStart thread3_start = new ThreadStart(() => { pc.THREAD_3("\"" + main_class + "\"", "\"" + sub_classes + "\""); });
            Thread thread3 = new Thread(thread3_start);

            ThreadStart thread4_start = new ThreadStart(() => { pc.THREAD_4(); });
            Thread thread4 = new Thread(thread4_start);

            thread1.Start();
            thread2.Start();
            thread3.Start();
            thread4.Start();
        }

        public void THREAD_1(string path)
        {
            ProcessExec process;
            process = new ProcessExec("Python\\python.exe", "Scripts\\THREAD_1.py --path \"" + path + "\"");
            process.ProcessCmd(true);
        }
        public void THREAD_2(string main_class)
        {
            ProcessExec process;
            process = new ProcessExec("Python\\python.exe", "Scripts\\THREAD_2.py --main_class \"" + main_class + "\"");
            process.ProcessCmd(true);
        }

        public void THREAD_3(string main_class, string sub_classes)
        {
            ProcessExec process;
            process = new ProcessExec("Python\\python.exe", "Scripts\\THREAD_3.py --main_class \"" + main_class + "\" --sub_classes \"" + sub_classes + "\"");
            process.ProcessCmd(true);
        }
        public void THREAD_4()
        {
            ProcessExec process;
            process = new ProcessExec(@"Python\python.exe", @"Scripts\THREAD_4.py");
            process.ProcessCmd(true);
        }
        public void YOWO(string path, bool sports)
        {
            string query = "yowo/YOWOv2/demo.py -d ava_v2.2 -v yowo_v2_tiny -size 224 --weight \"yowo/YOWOv2/yowo_v2_tiny_ava_k32.pth\" --video \"" + path + "\" --show";
            if (sports == true)
            {
                query = "yowo/YOWOv2/demo.py -d ucf24 -v yowo_v2_tiny -size 224 --weight \"yowo/YOWOv2/yowo_v2_tiny_ucf24_k32.pth\" --video \"" + path + "\" --show";
            }
            Console.WriteLine(query);
            ProcessExec process;
            process = new ProcessExec(@"Python\python.exe", query);
            process.ProcessCmd(true);
        }
        public void FaceRestoration(string path)
        {
            Console.WriteLine(Directory.GetCurrentDirectory() + @"\tmp_outputs\");
            ProcessExec process;
            process = new ProcessExec(@"Python\python.exe", "GFPGAN-master\\inference_gfpgan.py --i \"" + path + "\" -o \"" + Directory.GetCurrentDirectory() + "\"\\tmp_outputs\\ -v 1.3 -s 2");
            process.ProcessCmd(true);
        }

        public void Recommender(string feeling_message, string type, string duration)
        {
            ProcessExec process;
            process = new ProcessExec(@"Python\python.exe", "Scripts\\recommender.py --text \"" + feeling_message + "\" --type \"" + type + "\" --duration \"" + duration + "\"");
            process.ProcessCmd(true);
        }
        public void SummarizeVideo(string video_path)
        {
            ProcessExec process;
            process = new ProcessExec(@"Python\python.exe", "Scripts\\summarize_video.py --video_path \"" + video_path + "\"");
            process.ProcessCmd(true);
        }
        public void OnTheSpot(string video_path)
        {
            ProcessExec process;
            process = new ProcessExec(@"Python\python.exe", "Scripts\\LiveDetection.py --video_path \"" + video_path + "\"");
            process.ProcessCmd(true);
        }
    }
}

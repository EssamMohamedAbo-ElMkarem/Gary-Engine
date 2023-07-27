using System.Diagnostics;
using System;

namespace Gary_Engine
{
    class ProcessExec
    {
        // General parameters of the process
        public string prog_path;
        public string arguments;

        // Function to process the required program
        public void ProcessCmd(bool window)
        {
            ProcessStartInfo start_info = new ProcessStartInfo();
            start_info.FileName = prog_path;
            start_info.Arguments = arguments;
            start_info.CreateNoWindow = window;
            Process process = new Process();
            process.StartInfo = start_info;
            process.Start();
            process.WaitForExit();
        }

        // Constructor of the class to update the program and its arguments
        public ProcessExec(string program, string pro_arguments)
        {
            this.prog_path = program;
            this.arguments = pro_arguments;
        }
    }
}

/*
 
 ProcessStartInfo start_info = new ProcessStartInfo();
            start_info.FileName = prog_path;
            start_info.Arguments = arguments;
            start_info.UseShellExecute = false;
            start_info.RedirectStandardOutput = true;
            start_info.CreateNoWindow = window;
            var process = new Process();
            process.StartInfo = start_info;
            process.Start();
            while (!process.StandardOutput.EndOfStream)
            {
                Console.WriteLine(process.StandardOutput.ReadLine());
            }
            process.WaitForExit();
 
 */
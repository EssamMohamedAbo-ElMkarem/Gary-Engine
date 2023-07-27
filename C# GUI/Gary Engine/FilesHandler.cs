using Newtonsoft.Json;
using System.IO;
using System;
using System.Text.RegularExpressions;

namespace Gary_Engine
{
    class FilesHandler
    {
        // Write data in a specified file with a StreamWriter object
        public void WriteDate(string path, string data)
        {
            StreamWriter w1 = new StreamWriter(path);
            w1.Write(data);
            w1.Close();
        }

        // Read data from a specified file with a StreamReader object
        public string ReadDate(string path)
        {
            string data = "";
            var lines = File.ReadAllText(path);
            foreach (var line in lines)
            {
                data = data + "\n" + line;
            }
            return data;
        }

        // Remove all spection characters from string
        public string RemoveSpecialChars(string input)
        {
            return Regex.Replace(input, @"[^0-9a-zA-Z\._ ]", "");
        }

        // Remove all files and directories from a specific directory
        public static void Empty(string dir)
        {
            DirectoryInfo directory = new DirectoryInfo(dir);
            foreach (FileInfo file in directory.GetFiles()) file.Delete();
            foreach (DirectoryInfo subDirectory in directory.GetDirectories()) subDirectory.Delete(true);
        }
        public static dynamic returnFromJson(string jsonPath)
        {
            using (StreamReader r = new StreamReader(jsonPath))
            {
                string json = r.ReadToEnd();
                dynamic array = JsonConvert.DeserializeObject(json);
                return array;
            }
        }
    }
}

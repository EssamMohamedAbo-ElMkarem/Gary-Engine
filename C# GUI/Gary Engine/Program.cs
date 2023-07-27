using System;
using System.Windows.Forms;

namespace Gary_Engine
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            try
            {
                Application.EnableVisualStyles();
                Application.SetCompatibleTextRenderingDefault(false);
                Application.Run(new MainGary( true));
            }
            catch(Exception ex)
            {
                MessageBox.Show("Something went wrong please try again later and if you keep receiving the same error feel free to contact us!", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                Console.WriteLine(ex);
            }
        }
    }
}

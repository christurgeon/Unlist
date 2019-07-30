using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

/**
 * Unlist GUI - An application to unsubscribe from those pesky companies who won't leave you alone!
 *
 */
namespace UnlistGUI
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            Unsubscribe.Visible = false;
            Pass.UseSystemPasswordChar = true;
        }

        /**
         * Submit credentials and write to file for Python script to use.  Reads results of Python script back into checked list box.
         */
        private void Submit_Click(object sender, EventArgs e)
        {
            File.WriteAllText("credentials.txt",User.Text + ":" + Pass.Text);
            FileInfo emails = new FileInfo("emails.txt");
            if (IsFileLocked(emails)) {
            }
            int count = 0;
            parseStatus.Step = 1;
            parseStatus.Maximum = File.ReadLines("emails.txt").Count();
            using (StreamReader readtext = new StreamReader("emails.txt"))
            {
                while (!readtext.EndOfStream)
                {
                    string readMeText = readtext.ReadLine();
                    UnsubList.Items.Insert(count, readMeText);
                    count++;
                    parseStatus.PerformStep();
                }
            }
            Unsubscribe.Visible = true;
        }

        /**
         * Prevents file from being opened simultaneously by Python script and this GUI.
         * 
         */
        private bool IsFileLocked(FileInfo file)
        {
            FileStream stream = null;

            try
            {
                stream = file.Open(FileMode.Open, FileAccess.ReadWrite, FileShare.None);
            }
            catch (IOException)
            {
                return true;
            }
            finally
            {
                if (stream != null)
                    stream.Close();
            }

            return false;
        }
        private void UnsubList_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        /* 
         * Handles writing currently checked items to file for Python script to unsubscribe from.
         */
        private void Unsubscribe_Click(object sender, EventArgs e)
        {
            string checkedItems = string.Empty;
            foreach (object Item in UnsubList.CheckedItems)
            {
                checkedItems += (Item.ToString() + "\n");
            }
            System.IO.File.WriteAllText("selected_emails.txt",checkedItems);
        }
    }
}

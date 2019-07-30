namespace UnlistGUI
{
    partial class Form1
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
            this.User = new System.Windows.Forms.TextBox();
            this.Pass = new System.Windows.Forms.TextBox();
            this.Username = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.Submit = new System.Windows.Forms.Button();
            this.UnsubList = new System.Windows.Forms.CheckedListBox();
            this.Unsubscribe = new System.Windows.Forms.Button();
            this.parseStatus = new System.Windows.Forms.ProgressBar();
            this.SuspendLayout();
            // 
            // User
            // 
            this.User.Location = new System.Drawing.Point(33, 41);
            this.User.Name = "User";
            this.User.Size = new System.Drawing.Size(137, 20);
            this.User.TabIndex = 0;
            // 
            // Pass
            // 
            this.Pass.Location = new System.Drawing.Point(33, 94);
            this.Pass.Name = "Pass";
            this.Pass.Size = new System.Drawing.Size(137, 20);
            this.Pass.TabIndex = 1;
            // 
            // Username
            // 
            this.Username.AutoSize = true;
            this.Username.Location = new System.Drawing.Point(33, 22);
            this.Username.Name = "Username";
            this.Username.Size = new System.Drawing.Size(71, 13);
            this.Username.TabIndex = 2;
            this.Username.Text = "USERNAME:";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(33, 78);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(73, 13);
            this.label1.TabIndex = 3;
            this.label1.Text = "PASSWORD:";
            // 
            // Submit
            // 
            this.Submit.Location = new System.Drawing.Point(209, 27);
            this.Submit.Name = "Submit";
            this.Submit.Size = new System.Drawing.Size(141, 87);
            this.Submit.TabIndex = 4;
            this.Submit.Text = "SUBMIT";
            this.Submit.UseVisualStyleBackColor = true;
            this.Submit.Click += new System.EventHandler(this.Submit_Click);
            // 
            // UnsubList
            // 
            this.UnsubList.FormattingEnabled = true;
            this.UnsubList.Location = new System.Drawing.Point(33, 190);
            this.UnsubList.Name = "UnsubList";
            this.UnsubList.Size = new System.Drawing.Size(502, 304);
            this.UnsubList.TabIndex = 5;
            this.UnsubList.SelectedIndexChanged += new System.EventHandler(this.UnsubList_SelectedIndexChanged);
            // 
            // Unsubscribe
            // 
            this.Unsubscribe.Location = new System.Drawing.Point(404, 27);
            this.Unsubscribe.Name = "Unsubscribe";
            this.Unsubscribe.Size = new System.Drawing.Size(131, 87);
            this.Unsubscribe.TabIndex = 6;
            this.Unsubscribe.Text = "Unsubscribe from selection";
            this.Unsubscribe.UseVisualStyleBackColor = true;
            this.Unsubscribe.Click += new System.EventHandler(this.Unsubscribe_Click);
            // 
            // parseStatus
            // 
            this.parseStatus.Location = new System.Drawing.Point(33, 531);
            this.parseStatus.Name = "parseStatus";
            this.parseStatus.Size = new System.Drawing.Size(502, 23);
            this.parseStatus.TabIndex = 7;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(595, 648);
            this.Controls.Add(this.parseStatus);
            this.Controls.Add(this.Unsubscribe);
            this.Controls.Add(this.UnsubList);
            this.Controls.Add(this.Submit);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.Username);
            this.Controls.Add(this.Pass);
            this.Controls.Add(this.User);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "Form1";
            this.Text = "Unlist";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox User;
        private System.Windows.Forms.TextBox Pass;
        private System.Windows.Forms.Label Username;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button Submit;
        private System.Windows.Forms.CheckedListBox UnsubList;
        private System.Windows.Forms.Button Unsubscribe;
        private System.Windows.Forms.ProgressBar parseStatus;
    }
}


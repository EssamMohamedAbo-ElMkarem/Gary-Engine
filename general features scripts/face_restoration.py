import subprocess
''''


'''

class Face_Restoration():
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def run(self):
        # inference_gfpgan.py is the script in the Repo used to run the code
        # -i  --> where the script will get its data. The data can be either folder path or a single image
        # -o  --> where the script will output the results
        # -v  --> the version of the  pretrained model used let it be 1.3 always
        # -s  --> the upscale factor of the image
        subprocess.run(['cmd', '/c', 'python', 'inference_gfpgan.py', '-i',
                        self.input_path, '-o', self.output_path, '-v', '1.3', '-s', '2'])


inputt = r"C:\Users\Amr\Desktop\input"
output = r"C:\Users\Amr\Desktop\output"
Face_Restoration(inputt, output).run()
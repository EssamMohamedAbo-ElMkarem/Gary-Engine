# Gary-Engine
![Dot Net](https://img.shields.io/badge/.NET-512BD4?style=for-the-badge&logo=dotnet&logoColor=white)
![C Sharp](https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=c-sharp&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-FF0000?style=for-the-badge&logo=keras&logoColor=white)
![Blender](https://img.shields.io/badge/blender-%23F5792A.svg?style=for-the-badge&logo=blender&logoColor=white)
![Wix](https://img.shields.io/badge/Wix-000?style=for-the-badge&logo=wix&logoColor=white)

<img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/e1d33db1-c3bf-4558-8a74-fe43ec978e1f" width=800/>

Gary is a general-purpose AI based media solution built using state of the art deep learning algorithms to help enhance your experience by anabling the user to search within video content for people and objects(mainly cars) with specific charactristics just by entering natural language input search queries in Arabic or English making use of a vision search algorithm totally developed by the great team behind this project. Gary also offers other AI based features like selective & full object detection, full action detection, face restoration from images, 3-D reconstruction for human beings from a single image, on the spot analysis and video summarization.

# Installation 

This repository onlly contains some of the scripts and the required files for the solution to function due to size limitations so in order to make full use of Gary functionality all you have to do is to download the solution from this link and no requirements to be installed other than making sure you have Windows>=10 with .Net Framework>=4.7.2  <a href=""><b>Download and Enjoy!</b></a>

# Usage

When using the solution you will discover that we did our best to make to user friendly for anyone to use. Provided with Gary Tips every button you hover over will pop up a small window with some tips on how to use the tool. We have also added in the help section detailed tutorials for each feature within our solution.

<img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/2e77f489-83c8-48b4-86bf-23ebfd612eb4" width="45%"></img> <img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/e81d6834-c185-4adf-9249-82dc978c5649" width="45%"></img> <img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/0d809ea3-7961-4dd7-b79b-3eb69ce2ad90" width="45%"></img> <img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/d9de1107-a2ec-4687-8812-8f14cbb9ad2d" width="45%"></img> <img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/6899ec97-3f57-4647-9622-3415544091da" width="45%"></img> <img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/72f19e48-79d3-400f-aa3b-d8119e35946e" width="45%"></img> <img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/15d332fc-7f18-455e-b47c-e9f7bcfbc2e3" width="45%"></img> <img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/7b2bcc20-f488-4bd2-a4a6-cf55fb7b47f1" width="45%"></img> 

# The Main Search Algorithm YOSO (You Only Search Once) Motivation

Rapid growth of video content on the web has led to a growing demand for effective methods for searching in videos. Traditional text-based search engines are not well-suited for this task, as they cannot understand the visual content of videos. As a result, our algorithm came to the ground to solve this problem and enable us to search inside a video for objects with specific features using only natural text in Arabic and English. 

One approach is to extract the main objects and the features of interest from the input text using natural language processing techniques then extract the specific main object from the video frames using object detection and track this object in order to produce a final occurrences list with the output search result as a form of the object and the time it appears inside the video in seconds. After extracting the main object of interest then we pass it through a series of pre-trained vision models in order to filter the objects with the required traits. 

Our algorithm is based on three deep learning technologies first of all in order to extract the main object and the features from the input text, the input text is passed through a T5 model which we fine-tuned specially for this task. 

<img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/a904f97d-fde8-43e7-a6fd-1d24c5eefb37" width=700/>

T5, also known as Text-to-Text Transfer Transformer, is a neural network-based language model that was developed by Google AI. T5 is trained on a massive dataset of text and code, and it can be used for a variety of natural language processing tasks, including translation, summarization, question answering, and text generation. T5 is a transformer-based language model, which means that it uses a self-attention mechanism to learn long-range dependencies between words in a sentence. This allows T5 to better understand the context of a sentence, which is essential for many natural language processing tasks. T5 has been shown to be very effective at a variety of natural language processing tasks. For example, T5 has achieved state-of-the-art results on the GLUE benchmark, which is a suite of natural language processing tasks. T5 is also being used by Google Translate to improve the quality of translations.

Secondly, in order to fetch the main object of interest from the video frames we used "You Only Look Once" (YOLO) version-8 is a popular object detection algorithm that was first introduced in 2015 by Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali Farhadi. YOLO is a single-stage object detection algorithm, which means that it can detect objects in a single pass through an image or video. This makes YOLO much faster than two-stage object detection algorithms, such as R-CNN and Fast R-CNN.

<img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/0094d4f1-9c1f-49f0-8acf-f32552bf1e4a" width=700/>

<img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/8f1977f7-0375-406d-9b70-eb1b799b81ba" width=700/>

Finally, in order to filter the objects with the chosen features we fine-tuned several cnn based models specifically to match out task, we mainly used the following models for the features extraction: 
      
* Inception which is a type of convolutional neural network (CNN) that was developed by Google in 2014. It is designed to be more efficient than traditional CNNs. It does this by using a technique called "inception" to combine features from different layers of the network. This allows the network to learn more complex features without increasing the number of parameters or the amount of computation required.
* EfficientNet which is a convolutional neural network (CNN) architecture that was developed by researchers at Google AI in 2019. It is based on the idea that the accuracy of a CNN can be improved by scaling it up, but this comes at the cost of efficiency. EfficientNet addresses this by using a compound coefficient to scale up the width, depth, and resolution of the network in a coordinated way. This allows EfficientNet to achieve state-of-the-art accuracy while still being efficient.

<img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/923a5e10-47c9-4ff4-ac13-83beac12fd93" width=700/>

# GarySE Package YOSO Example

![image](https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/15527620-fa4b-45ca-90e5-4341a6a0a064)


# Third Party Features Citation
* For the object detection feature we used the network based on the works here <a href="https://github.com/ultralytics/ultralytics">YOLOv8 Repository</a>.
* For the action detection feature we used the network based on the works here <a href="https://github.com/wei-tim/YOWO">YOWO Repository</a>.
* For the 3-D human reconstruction feature we used the network based on the works here <a href="https://github.com/facebookresearch/pifuhd
">PIFUHD Repository</a>.

# Get to Know The Team

<img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/855ff415-0167-4f30-a53f-cb1a8089fbd7" width=45% />

<a href="https://www.linkedin.com/in/essam-el-tobgi-394a48179/"><b>Essam El-Tobgi</b></a>

<img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/f04b4fa5-940c-41f4-bf5a-26eeb946a84f" width=45% />

<a href="https://www.linkedin.com/in/mustafa-osama-164254232/"><b>Mustafa Ossama</b></a>

<img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/08f6423f-b328-4c64-89f0-a069b1483110" width=45% />

<a href="https://www.linkedin.com/in/youssef-barakat25/"><b>Youssef Barakat</b></a>
<img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/ea88ac9c-f421-41b4-8788-bde365210c60" width=45% />

<a href="https://www.linkedin.com/in/mohamed-sheded-50078920b/"><b>Muhammed Sheded</b></a>

<img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/48483a74-030a-43f7-bc9b-20551a11123d" width=45% />

<a href="https://www.linkedin.com/in/laura-abdulalem-75264621a/"><b>Laura Abdul-Allim</b></a>

<img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/167930a4-7461-4ede-beb7-23e7c6c21848" width=45% />

<a href="https://www.linkedin.com/in/karim-akmal-296a761aa/"><b>Karim Akmal</b></a>

<img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/1482b524-2e1b-4d10-b814-e60558a8d8d8" width=45% />

<a href="https://www.linkedin.com/in/mahmoud-khater-154154220/"><b>Mahmoud Khater</b></a>

<img src="https://github.com/EssamMohamedAbo-ElMkarem/Gary-Engine/assets/50668640/fd6147f0-967d-42b6-8308-03b6f766edfa" width=45% />

<a href="https://www.linkedin.com/in/abdelrahman-nabil-039069249/"><b>Abdulrahman Nabil</b></a>










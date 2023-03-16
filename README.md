# RockPaperScissors Convo-Net - A deep learning network for Rock Paper Scissors Classification

Rock Paper Scissors game is a popular game that can be played by people of all ages.

In this project, I aim to develop a deep learning model that can recognize the hand gestures for rock, paper, Scissors using CNN and transfer learning with the VGG16 architecture.

This Project has practical applications in gaming, gesture recognition and robotics.
## Dataset
The Training and Validation Dataset can be downloaded from Laurence Moroney's personal webpage

[Rock Paper Scissors Dataset](https://laurencemoroney.com/datasets.html).

Note that all of these pictures use a plain white background.Each image is 300 X 300 pixels in 24-bit color.
## Framework and Other Libraries

**Framework**: Tensorflow

**Libraries**: Numpy, Matplotlib, PIL

**Client**: Streamlit Cloud


## VGG-16

The VGG-16 architecture is composed of 16 layers, including 13 convolution layers and 3 fully connected layers.

Adding a few more layers on top of it to adapt it to the specific task of recognizing hand gestures. The added layers will include a pooling layers, a fully connected layer, and a softmax layer. 

## How to Run?

streamlit run app.py

## Screenshots

![Output](https://github.com/MuthuPalaniappan925/RockPaperScissor-Convo-NET/blob/master/Outputs/output_1.png "Output")

![Output](https://github.com/MuthuPalaniappan925/RockPaperScissor-Convo-NET/blob/master/Outputs/output_2.png "Output")

![Output](https://github.com/MuthuPalaniappan925/RockPaperScissor-Convo-NET/blob/master/Outputs/output_3.png "Output")

![Output](https://github.com/MuthuPalaniappan925/RockPaperScissor-Convo-NET/blob/master/Outputs/output_4.png "Output")

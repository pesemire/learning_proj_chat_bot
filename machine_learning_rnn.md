# Machine Learning and RNN model
**本文仅适用于Mac**
要点：了解基本的机器学习步骤和RNN模型（递归神经网络），使用模型进行文本模仿。参考https://medium.com/deep-writing/how-to-write-with-artificial-intelligence-45747ed073c#.qyihwpk0c 和聊天机器人第26-28章
## Step 0: Understanding the simple intuition
Here is a very crude approximation of what is involved in the Deep Writing process. More than anything, this is meant to give you enough intuition and appreciation to follow along with the rest of the tutorial.
You show a computer some sample text (for example, the Harry Potter books).

1. The computer identifies all the unique words in the sample text.
2. The computer groups words based on how often they appear together in the sample text (using a particular mathematical model). This is the “learning” portion of “Deep Learning”.
3. You pick a starting word (for example, “The”).
4. Using what it learned in Step 3, you ask the computer to guess the word most likely to come after the starting word (i.e. “The”). This is recorded as the second word.
5. Then, based on the first two words, you ask the computer to guess the third word. And so on.
6. Eventually, you tell the computer to stop guessing after many words, and you have successfully created your Deep Writing.

## Step 1: Download the code
We are going to use code written by Sung Kim (who teaches computer science at HKUST). https://github.com/hunkim/word-rnn-tensorflow/branches (Download the code in our repository because I have done some modification in order to make it compatible with our setting up)

## Step 2: Customize the text
Find word-rnn-tensorflow-master > data > tinyshakespeare > input.txt. Then, delete all the text in the file, and replace it with the sample text that you want to use.

The longer the sample text, the “better” the output will be. Of course, the longer the sample text, the longer it will take to train your model. 

Caution: don't make the sample text too long, it will take forever to run the program. 

## Step 3: Install Tensorflow
TensorFlow is a machine learning library made by Google. We need to download it in order to run our code. Be sure to download tensorflow 1.0. Otherwise, the code won't work. 

Use this link to finish the installation: https://www.tensorflow.org/install/install_mac

Caution: our code only work with MacOs, Be sure to satisfy all the requirements. 

FYI, I used native pip to download Tensorflow. 

## Step 4: Train the model
**This step will take huge amount time to accomplish. Don't try this unless you are not going to use your Mac for the next 12 hours. During the training, make sure your computer is plugged in. It is worth mentionning that your Mac will be extremely slow at multitasking while trainning**

```python
cd directory_location_word_cnn #switch the directory to the folder of rnn model
```



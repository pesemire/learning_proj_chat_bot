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


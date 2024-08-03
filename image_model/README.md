

## 1. Image-Classification
MNIST 데이터셋을 제외한 다른 공공 데이터셋 선택 후, <br>
해당 데이터셋에 대하여 MLP와 CNN으로 Image Classification 수행


### 🚀 목표  
MNIST 데이터셋을 제외한 다른 공공 데이터셋을 선택하여, 해당 데이터셋에 대해 MLP(Multi-Layer Perceptron)과 CNN(Convolutional Neural Network) 두 가지 딥러닝 모델을 이용한 이미지 분류 작업을 수행할 것입니다. 이를 통해 선택한 데이터셋에 대한 MLP와 CNN 모델의 성능을 비교하여, 각 모델의 장단점을 분석하고, 최적의 모델을 결정하려고 합니다. 또한, 이를 통해 딥러닝 모델의 이미지 분류 기술을 익히고, 다양한 데이터셋에 대한 분류 작업에 적용할 수 있는 기술력을 향상시키는 것이 목표입니다.

- [X] 공공데이터 활용
    - fishion -Mnist                       
    ![image](https://user-images.githubusercontent.com/86215536/232183077-e301d927-166c-4fc2-b828-45fea960f8da.png)                
    링크 : https://www.kaggle.com/datasets/zalando-research/fashionmnist

    - 캐글 cat & dog                                     
    ![image](https://user-images.githubusercontent.com/86215536/232183093-8f47592c-8002-428d-9ee8-e3f8fb463601.png)                 
     출처 : https://www.kaggle.com/c/dogs-vs-cats
    
- [X] 이미지 분류 모델 적용
    - MLP
    : 가장 기본적인 형태의 인공신경망(Artificial Neural Networks) 구조이며, 하나의 입력층(input layer), 하나 이상의 은닉층(hidden layer), 그리고 하나의 출력층(output layer)로 구성             
    ![image](https://user-images.githubusercontent.com/86215536/232182866-8511b119-a915-4e90-9dc0-7972d8f15943.png)

    - CNN        
    : MLP(완전연결신경망)와 CNN(합성곱 신경망)의 차이는 특징점 추출의 유무                              
    ![image](https://user-images.githubusercontent.com/86215536/232182902-b5f194e2-311b-4a5d-84d6-f43d9fe6150a.png)


> MLP는 이미지 행렬을 1차원 배열로 만들고 신경망에 입력으로 넣어 가중치를 계산해서 정보 손실이 큰 반면, CNN은 사람이 보는 것 처럼 이미지 행렬 2차원 배열에서 가로, 세로 축 전부 합성곱 연산과 풀링 연산으로 특징점을 추출하기에 정보 손실이 적은 점이 있음.

 <br>



## 이미치 처리 논문

chatGPT 검색 : 
다음은 컴퓨터 비전 분야에서 많이 읽히는 논문 중 일부입니다.
- "ImageNet Classification with Deep Convolutional Neural Networks" by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton. (2012)
- "Very Deep Convolutional Networks for Large-Scale Image Recognition" by Karen Simonyan and Andrew Zisserman. (2015)
- "Mask R-CNN" by Kaiming He, Georgia Gkioxari, Piotr Dollár, and Ross Girshick. (2018)
- "YOLOv4: Optimal Speed and Accuracy of Object Detection" by Alexey Bochkovskiy, Chien-Yao Wang, and Hong-Yuan Mark Liao. (2020)
- "Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks" by Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun. (2015)
- "Spatial Transformer Networks" by Max Jaderberg, Karen Simonyan, Andrew Zisserman, and Koray Kavukcuoglu. (2015)
- "Deep Residual Learning for Image Recognition" by Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. (2016)
- "U-Net: Convolutional Networks for Biomedical Image Segmentation" by Olaf Ronneberger, Philipp Fischer, and Thomas Brox. (2015)
- "Generative Adversarial Networks" by Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and Yoshua Bengio. (2014)
- "SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <1MB model size" by Forrest N. Iandola, Song Han, Matthew W. Moskewicz, Khalid Ashraf, William J. Dally, and Kurt Keutzer. (2016)                     
이 목록은 유명한 논문 중 일부일 뿐이며, 이 분야에서 연구를 진행하고 있는 다른 연구자들이나 논문도 매우 중요합니다. 따라서 다양한 논문들을 찾아보고 읽어보는 것이 좋습니다.




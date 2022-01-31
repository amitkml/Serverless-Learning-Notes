# RetinaNet

It is also a one-stage framework like YOLO and SSD, which trades speed for worse accuracy than the two-stage frameworks like the R-CNN variations. The RetinaNet uses a ResNet + FPN backbone to generate a 
rich, multi-scale convolutional feature pyramid. As usual, two subnetworks are attached on top, one for classifying anchor boxes, and another one for generating offset from the anchor boxes to the ground-truth object boxes.

![im](https://miro.medium.com/max/1400/1*13Mo0jyhs_9EqFSppw3ueQ.png)

mbalance of classes during training of dense detectors overwhelms the cross entropy loss. The innovative **focal loss**  improves accuracy focusing training on a sparse set of hard examples,  while limiting the number of easy negatives. This is done by reshaping  the loss function to not value easy examples as much as the hard ones.

![img](https://miro.medium.com/max/1400/1*f21RTmxGsEp1U-2BGJC4Tw.png)

Introducing the weighting factor α is a common method for addressing class imbalance introduce a weighting factor. The authors first experimented with α=0, but this yielded worse accuracy than the 
alpha-balanced form. You may also notice that when γ=0, the focal loss is equivalent to cross-entropy loss.



# Panoptic Segmentation

This is being achieved through Detectron2-. This is a task which segments both instances and background pixels; gives complete understanding of every pixel in image. Here backbone network is all about resnet, vggnet

![1592303582426](C:\Users\akayal\AppData\Roaming\Typora\typora-user-images\1592303582426.png)

## What?

![im](https://miro.medium.com/max/2000/1*vsA7_RcQMgflP7Q9GRcEIg.jpeg)

![img](https://miro.medium.com/max/1400/1*eKdEDqyvj7SCb9Pci7AyHA.gif)



# What is Detectron2?

[Detectron2](https://github.com/facebookresearch/detectron2) is the object detection and segmentation platform released by [Facebook AI Research](https://ai.facebook.com) (FAIR) as an open-source project.

# References

- https://medium.com/deepvisionguru/how-to-embed-detectron2-in-your-computer-vision-project-817f29149461
- <https://towardsdatascience.com/panoptic-segmentation-with-upsnet-12ecd871b2a3>
- 
# ImageProcessing2

OpenCVを用いてコンピュータに接続されたカメラから動画を取得し、フィルターをかけて表示する。<br>
フィルターはOpenCVでもともと用意されている「bilateralFilter」を用いる。<br>
その際、トラックバーの値を取得してbilateralFilterの引数の一つとする。<br>
この引数は注目画素をぼかすために使われる領域である。<br>
トラックバーの値が大きいほど、注目画素をぼかすために使われる領域も広くなる。<br>
qキーが入力されたらウインドウを閉じる。<br>

動画のURL<br>
https://youtu.be/_r5ZZ4Js0Mw<br>


参考にしたURL<br>
https://qiita.com/shim0mura/items/f222082b7ef08de3732e <br>
https://docs.opencv.org/3.0-last-rst/modules/imgproc/doc/filtering.html?highlight=laplacian#bilateralfilter <br>

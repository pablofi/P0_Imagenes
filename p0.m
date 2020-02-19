%Hernández López Axel Mauricio
%Martínez Téllez Pablo
%Rivera González Rubén
%Procesamiento Digital de Imágenes
%Dr. Boris Escalante Ramírez


%4: Leer la imagen del archivo .pcx
%   desplegarla usando el comando image
%   y el comando imshow
I=imread('C:\Users\Axel\Downloads\Macaw.pcx');
figure(1);image(I);
figure(2);imshow(I);

%5: Leer y desplegar la imagen abdomen.png
%   usando el comando image y el comando imagesc
K=imread('C:\Users\Axel\Downloads\abdomen.png');
figure(3);image(K);colormap(gray);
figure(4);imagesc(K);colormap(gray);

%7: Visualizar la imagen abdomen.png
%   con diferentes paletas de colores predefinidas
%   de Matlab
L=imread('C:\Users\Axel\Downloads\abdomen.png');
figure(5);imagesc(L);colormap(winter);

%10: Lea la imagen satelital. Enumere los componentes.
%    Despliegue dos de los componentes
X=imread('C:\Users\Axel\Downloads\S1A_EW_9E49_TN_Cal_dB_uint8.tif');
imageinfo('C:\Users\Axel\Downloads\S1A_EW_9E49_TN_Cal_dB_uint8.tif');
figure(6);imshow(X(:,:,1));
figure(7);imshow(X(:,:,2));

R=imresize(X,0.33);
figure(8);imshow(R(:,:,1));
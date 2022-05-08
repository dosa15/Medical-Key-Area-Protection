clc
clear all
img=imread('testimage.jpg');             %Read different images 
img=imresize(img, [512 512]);
if ( size ( img,3 ) ~= 1)
    img=rgb2gray(img);
end
%Taking histogram values into an array
[pixelCounts, grayLevels] = imhist(img);
m=max(pixelCounts);
a=find(pixelCounts==m)-1;   %Pixel value with Max Freq, Array Count starts from 1 
b=find(pixelCounts==0)-1;   %Pixel value(s) with 0 Freq

z=find(b>a);
b=b(z);                %Take the first amongst the zero freq pixels
embed=img;

[row, col]=size(embed);

%Shifting the histogram by 1 unit within the range [a,b]
for i=1:row
    for j=1:col
        if and(embed(i,j)>=a,embed(i,j)<b)
            embed(i,j)=embed(i,j)+1;
        end;
    end;
end;


%Message to be encoded of equal bits as the max frequency
message=randi([0 1],1,m);       %random message generated using 0,1

%Shift pixels within frequecy range by -1 unit if message bit is 0
ptr=1;
a=a+1;
for i=1:row
    for j=1:col
         if embed(i,j)==a
             if message(ptr)==0
                 embed(i,j)=embed(i,j)-1; 
                 ptr=ptr+1;
             else
                 ptr=ptr+1;
             end;
         end;
    end;
end;

%Displaying the Images
figure,
subplot(1,2,1);
imshow(img);
title('Original Image');
subplot(1,2,2);
imshow(embed);
title('Embedded Image');

%Displaying the Histograms
figure,
subplot(2,1,1);
imhist(img);
title('Histogram of Original Image');
subplot(2,1,2);
imhist(embed);
title('Histgram of Embedded Image');

% imwrite(embed,'embedded.jpg');  problems while storing in jpeg format.
% Histogram values get changed
imwrite(embed,'stego.png');

%Displaying the difference between Original and Embedded Image
X = gpuArray(img);
Y = gpuArray(embed);
Z = imabsdiff(X,Y);
figure
imshow(Z,[])
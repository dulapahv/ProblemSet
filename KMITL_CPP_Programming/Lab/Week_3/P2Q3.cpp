#include<iostream>


int main(){
    int h;
    bool even = false;
    std::cout <<"Enter size: ";
    std::cin >> h;
    if(h%2==0){
        h-=1;
        even = true;
    }
    int star = 1;
    for(int i=0;i<h/2;i++){
        for(int space = 0;space<(h-star)/2;space++){
            std::cout<<' ';
        }
        for(int k =0;k<star;k++){
            std::cout<<'*';
        }
        for(int space = 0;space<(h-star)/2;space++){
            std::cout<<' ';
        }
        star+=2;
        std::cout<<std::endl;
    }
    for(int z=0;z<h;z++){
        std::cout<<'*';
    }
    std::cout<<std::endl;
    star-=2;
    for(int i=0;i<h/2;i++){
        for(int space = (h-star)/2 ;space>0;space--){
            std::cout<<' ';
        }
        for(int k =0;k<star;k++){
            std::cout<<'*';
        }
        for(int space = (h-star)/2 ;space>0;space--){
            std::cout<<' ';
        }
        star-=2;
        std::cout<<std::endl;
    }
    if (even){
        std::cout<<std::endl;
    }
}
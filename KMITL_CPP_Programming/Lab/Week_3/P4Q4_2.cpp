#include<iostream>
using namespace std;

void print_checker(char c1,char c2, int w, int h,int size){
    int counth =0;
    int countw =0;
    for(int i=0; i<h;i++){
            counth%=(size*2);
            for(int j=0;j<w;j++){

                if(counth<size){
                    if(countw<size){
                        cout<<c1;
                        countw++;
                    }
                    else{
                        cout<<c2;
                        countw++;
                    }
                }
                else{
                    if(countw<size){
                        cout<<c2;
                        countw++;
                    }
                    else{
                        cout<<c1;
                        countw++;
                    }
                }
                countw%=(size*2);
        }
        countw=0;
        cout<<endl;
        counth+=1;
    }
}

int main(){
    int w,h,size;
    char c1,c2;
    cout << "Enter Width: ";
    cin >> w;
    cout << "Enter Height: ";
    cin >> h;
    cout << "Enter character 1: ";
    cin >> c1;
    cout << "Enter character 2: ";
    cin >> c2;
    cout <<"Enter Size: ";
    cin >> size;
    print_checker(c1,c2,w,h,size);
}
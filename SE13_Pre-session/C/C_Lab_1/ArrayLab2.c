#include <stdio.h>
#include <string.h>

int main(){
    char web[11], new_url[20] = "www.";
    gets(web);
    strcat(new_url,web);
    puts(new_url);
    strcat(new_url,".com");
    printf("%s\n",new_url);
    printf("%s\n",web);
    printf("Before\nLength: %d\n", strlen(web));
    printf("After\nLength: %d\n", strlen(new_url));
}

// #include <stdio.h>
// #include <string.h>

// int main() 
// {
//     char str1[] = "www.", str2[] = ".com", urlInput[11];
//     scanf("%s", &urlInput);
//     strcat(strcat(str1, urlInput), str2);
//     puts(str1); // ? 
//     return 0;
// }
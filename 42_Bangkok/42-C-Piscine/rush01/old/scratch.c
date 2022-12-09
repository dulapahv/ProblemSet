// #include <stdio.h>
// #include <stdlib.h>

// int main(int argc, char **argv) {
//     char input[] = "4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2";
//     // int *top = (int*) malloc(4 * sizeof(int));
//     // int *bottom = (int*) malloc(4 * sizeof(int));
//     // int *left = (int*) malloc(4 * sizeof(int));
//     // int *right = (int*) malloc(4 * sizeof(int));
//     int top[4];
//     int bottom[4];
//     int left[4];
//     int right[4];

//     int i;
//     int j;

//     i = 1;
//     while (i < 33) {
//         printf("%d", i);
//         i = (2 * i) + 1;
//     }

//     // print each array
//     // for (int i = 0; i < 4; i++)
//     // {
//     //     printf("%d ", top[i]);
//     // }
//     // printf("\n");
//     // for (int i = 0; i < 4; i++)
//     // {
//     //     printf("%d ", bottom[i]);
//     // }
//     // printf("\n");
//     // for (int i = 0; i < 4; i++)
//     // {
//     //     printf("%d ", left[i]);
//     // }
//     // printf("\n");
//     // for (int i = 0; i < 4; i++)
//     // {
//     //     printf("%d ", right[i]);
//     // }
//     // printf("\n");
// }

#include <stdio.h>

int ft_is_space(char c)
{
    if (c == ' ' || c == '\t' || c == '\n' || c == '\v' || c == '\f' || c == '\r')
        return (1);
    else
        return (0);
}

int ft_negative(char c)
{
    if (c == '-')
        return (-1);
    if (c == '+')
        return (1);
    else
        return (0);
}

int ft_atoi(char *str)
{
    int minus;
    int result;

    result = 0;
    minus = 1;
    while (ft_is_space(*str))
        str++;
    while (ft_negative(*str) == -1 || ft_negative(*str) == 1)
    {
        minus *= ft_negative(*str);
        str++;
    }
    while (*str != '\0')
    {
        if (*str >= '0' && *str <= '9')
        {
            result *= 10;
            result += ((int)(*str - '0'));
        }
        else
            break;
        str++;
    }
    return (result * minus);
}

int main(int argc, char **argv)
{
    char buf[] = "4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2";
    int nums[128], n = 0;

    char *p = buf;
    while (*p)
    {
        while (*p && (*p == ' ' || *p == '\t' || *p == '\n'))
            p++;

        if (*p)
        {
            nums[n++] = ft_atoi(p);
            while (*p && *p != ' ' && *p != '\t' && *p != '\n')
                p++;
        }
    }

    //separate nums into 4 arrays
    int top[4];
    int bottom[4];
    int left[4];
    int right[4];
    int i;
    int j;

    i = 0;
    while (i < 4)
    {
        top[i] = nums[i];
        i++;
    }
    i = 0;
    while (i < 4)
    {
        bottom[i] = nums[i + 4];
        i++;
    }
    i = 0;
    while (i < 4)
    {
        left[i] = nums[i + 8];
        i++;
    }
    i = 0;
    while (i < 4)
    {
        right[i] = nums[i + 12];
        i++;
    }
    // print each array
    for (int i = 0; i < 4; i++)
        printf("%d ", top[i]);
    printf("\n");
    for (int i = 0; i < 4; i++)
        printf("%d ", bottom[i]);
    printf("\n");
    for (int i = 0; i < 4; i++)
        printf("%d ", left[i]);
    printf("\n");
    for (int i = 0; i < 4; i++)
        printf("%d ", right[i]);
    printf("\n");

    // for (int i = 0; i < n; i++)
    //     printf("%d ", nums[i]);
    // printf("\n");

    return 0;
}
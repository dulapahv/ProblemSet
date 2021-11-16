#include <string.h>
#include <stdio.h>
#include <iostream>
# define MAXSEAT 50

using namespace std;

char const* count(int cc)
{
    switch(cc)
    {
        case 1: return "Tokyo, Japan";
        case 2: return "Moscow, Russia";
        case 3: return "Singapore, Singapore";
        case 4: return "Seoul, South Korea";
        case 5: return "London, England";
        case 6: return "Sydney, Australia";
        case 7: return "Manila, Philippines";
        case 8: return "Shanghai, China";
        case 9: return "New Delhi, India";
        case 10: return "Washington,D.C., America";
        default: return "";
    }
}

char const* pilot(int a,int timeset)
{
    if(timeset == 1)
    {
        switch(a)
        {
            case 1: return "John";
            case 2: return "Bob";
            case 3: return "Steve";
            case 4: return "Sam";
            case 5: return "Mark";
            case 6: return "Deen";
            case 7: return "Non";
            case 8: return "Alexander";
            case 9: return "Uki";
            case 10: return "Tik";
            default: return "There is only 10 planes";
        }
    }
    else if(timeset == 2)
    {
        switch(a)
        {
            case 1: return "Sam";
            case 2: return "Bob";
            case 3: return "Smith";
            case 4: return "Dech";
            case 5: return "Sea";
            case 6: return "Tar";
            case 7: return "Mu";
            case 8: return "Aom";
            case 9: return "Wuth";
            case 10: return "Wave";
            default: return "There is only 10 planes";
        }
    }
    else
    {
        return "";
    }
}

char const* departure_time(int a,int timeset)
{
    if(timeset == 1)
    {
        switch(a)
        {
            case 1: return "08:00:00";
            case 2: return "08:30:00";
            case 3: return "05:10:00";
            case 4: return "06:50:00";
            case 5: return "07:20:00";
            case 6: return "04:05:00";
            case 7: return "09:00:00";
            case 8: return "11:45:00";
            case 9: return "10:00:00";
            case 10: return "03:30:00";
            default: return "There is only 10 planes";
        }
    }
    else if(timeset == 2)
    {
        switch(a)
        {
            case 1: return "12:30:00";
            case 2: return "15:20:00";
            case 3: return "17:25:00";
            case 4: return "19:30:00";
            case 5: return "13:00:00";
            case 6: return "16:10:00";
            case 7: return "20:50:00";
            case 8: return "14:40:00";
            case 9: return "22:40:00";
            case 10: return "18:45:00";
            default: return "There is only 10 planes";
        }
    }
    else
    {
        return "";
    }
}

char const* arrival_time(int a,int timeset)
{
    if(timeset == 1)
    {
        switch(a)
        {
            case 1: return "13:45:00";
            case 2: return "18:50:00";
            case 3: return "07:40:00";
            case 4: return "12:10:00";
            case 5: return "20:25:00";
            case 6: return "13:25:00";
            case 7: return "12:10:00";
            case 8: return "15:00:00";
            case 9: return "14:10:00";
            case 10: return "23:50:00";
            default: return "There is only 10 planes";
        }
    }
    else if(timeset == 2)
    {
        switch(a)
        {
            case 1: return "18:15:00";
            case 2: return "01:40:00(Tomorrow)";
            case 3: return "19:55:00";
            case 4: return "00:50:00(Tomorrow)";
            case 5: return "02:05:00(Tomorrow)";
            case 6: return "01:30:00(Tomorrow)";
            case 7: return "00:00:00(Tomorrow)";
            case 8: return "18:35:00";
            case 9: return "02:50:00(Tomorrow)";
            case 10: return "15:05:00(Tomorrow)";
            default: return "There is only 10 planes";
        }
    }
    else
    {
        return "";
    }
}


struct Infor
{
    char passenger[30];
    char passport[13];
}ppp[MAXSEAT];


int main()
{
    for(int i=1;i<=MAXSEAT;i++)
    {
        ppp[i].passenger[30] = {};
        ppp[i].passport[13] = {};
    }
    FILE*input = fopen("/Users/USER/Desktop/beforetest.txt", "r");
    FILE*output = fopen("/Users/USER/Desktop/aftertest.txt", "w");
    int choice;
    char gender;
    char pass[30];
    char port[14];
    cout << "**************************Welcome to Smile Airport**************************\n";
    cout << "\t\tWe wish the passenger will enjoy with our service\n\n";
    cout << "Please enter your information" << endl;
    cout << "M or m: man" << endl;
    cout << "W or w: woman" << endl;
    cout << "Enter your gender:";
    cin >> gender;
    while(gender!='m' && gender!='M' && gender!='w' && gender!='W')
    {
        cout << "\nPlease enter the correct gender:";
        cin >> gender;
    }
    cout << "\nName:";
    fflush(stdin); // Remove trailing \n
    fgets(pass, 30, stdin);    //name

    cout << "ID card number:";
    fgets(port, 14, stdin);    //passport
    int error = 0;
    while(error == 0)
    {
        int a = strlen(port);
        if(a!=13)
        {
            cout << "invalid. Try again!" << endl;
            cin >> port;
        }
        else
        {
            for(int i=0;i<13;i++)
            {
                if (isalpha(port[i]))
                {
                    cout << "invalid. Try again!" << endl;
                    cin >> port;
                    break;
                }
                error=1;
            }
        }
    }
    if(gender=='m' || gender =='M')
        cout << "Welcome Mr." << pass << endl;
    else
        cout << "Welcome Mrs." << pass << endl;
        
    cout << "\n_______________1.Information of airplane____________________" << endl;
    cout << "_______________2.Reservation the seat_______________________" << endl;
    cout << "_______________3.Print tickets for all the seats_______________" << endl;
    cout << "_______________4.Clear_______________"<< endl;
    cout << "Enter the choice:";
    cin >> choice;
    
    while(choice!=5)
    {
        switch(choice)
        {
            case 1:
                    int n,timeset;
                    cout << "1:Morning" << endl;
                    cout << "2:Evening" << endl;
                    cin >> timeset;
                    cout << "\n";
                    while(timeset!=1 && timeset!=2)
                    {
                        cout << "Please choose only 1 or 2: ";
                        cin >> timeset;
                    }
                    for(int i=1;i<=10;i++)
                    {
                        cout << i << ":" << count(i) << endl;
                    }
                    cout << "\nPlease select airplane number(1-10):";
                    cin >> n;
                    cout << "Pilot name:" << pilot(n,timeset) << endl;
                    cout << "Departure time:" << departure_time(n,timeset) << endl;
                    cout << "Arrival time::" << arrival_time(n,timeset) << endl;
                    break;
        /////////////////////////////done////////////////////////////////////////
            case 2:
                    int x,seat,re;
                    cout << "Which airplane(1-10) you want to reserve:";
                    cin >> x;
                    //check from file
                    //show the seat
                    cout << "There is " << seat << " available seat in plane" << x << endl;
                    cout << "Which seat number do you want to choose:";
                    cin >> re;
                    if(strcpy(ppp[re].passenger,"NULL")) //******************************************************
                    {
                        ////////////////////
                        strcpy(ppp[re].passenger, pass);
                        cout << "Reserve successful";
                    }
                    else
                        cout << "We apologist, this seat has been reserved.";
                    break;
            case 3:
                    int flight;
                    cout << "1:return air tickets:One way" << endl;
                    cout << "2:round-trip tickets:Back and forth" << endl;
                    cin >> flight;
                    while(flight != 1 && flight != 2)
                    {
                        cout << "Do you want to 1 or 2:";
                        cin >> flight;
                    }
            default: cout << "There is only choice 1-5" << endl;
                    break;
        }
        cout << "\n\n";
        cout << "Do you want to choose other choices:";
        cin >> choice;
    }
}

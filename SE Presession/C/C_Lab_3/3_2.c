struct Clock
{
    struct Date Date_data;
    struct Time Time_data;
};

struct Date
{
    int day;
    int month;
    int year;
};

struct Time
{
    int seconds;
    int minds;
    int hours;
};

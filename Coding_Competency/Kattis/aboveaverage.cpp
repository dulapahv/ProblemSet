#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int student[cases];
    for (int i = 0; i < cases; i++) {
        cin >> student[i];

        int sum = 0, aboveavg = 0;
        float avg = 0, percentage = 0;
        
        int score[student[i]];
        for (int j = 0; j < student[i]; j++) {
            cin >> score[j];
        }

        for (int j = 0; j < student[i]; j++) {
            sum += score[j];
            avg = sum / student[i];
        }

        for (int j = 0; j < student[i]; j++) {
            if (score[j] > avg) {
                aboveavg++;
            }
        }

        percentage = (aboveavg * 100) / float(student[i]);
        cout << setprecision(3) << fixed << percentage << "%" << endl;
    }
}
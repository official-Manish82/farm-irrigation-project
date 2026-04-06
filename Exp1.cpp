#include <iostream>
#include <ctime>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <chrono>

using namespace std;

void quick_sort(int[], int, int);
int partition(int[], int, int);
void generateRandomArray(int[], int);

int main()
{
    int choice;
    cout << "==== QUICK SORT ANALYSIS ====" << endl;
    cout << "1. Quick Sort with User Input" << endl;
    cout << "2. Performance Analysis (Time vs n)" << endl;
    cout << "Enter your choice (1 or 2): ";
    cin >> choice;

    if (choice == 1)
    {
        // Manual input
        int a[50], n, i;
        cout << "How many elements? ";
        cin >> n;
        
        cout << "\nEnter array elements: ";
        for (i = 0; i < n; i++)
            cin >> a[i];
        
        quick_sort(a, 0, n - 1);
        
        cout << "\nArray after sorting: ";
        for (i = 0; i < n; i++)
            cout << a[i] << " ";
        cout << endl;
    }
    else if (choice == 2)
    {
        // Performance analysis
        ofstream outfile("quicksort_analysis.txt");
        outfile << "n\tTime(microseconds)" << endl;
        
        int testSizes[] = {100, 500, 1000, 2000, 5000, 10000, 15000, 20000};
        int numTests = sizeof(testSizes) / sizeof(testSizes[0]);
        
        cout << "\n==== PERFORMANCE ANALYSIS ====" << endl;
        cout << setw(10) << "n" << setw(20) << "Time (microseconds)" << endl;
        cout << "-----------------------------------" << endl;
        
        for (int t = 0; t < numTests; t++)
        {
            int n = testSizes[t];
            int *arr = new int[n];
            
            // Generate random array
            generateRandomArray(arr, n);
            
            // Measure time for sorting
            auto start = chrono::high_resolution_clock::now();
            quick_sort(arr, 0, n - 1);
            auto end = chrono::high_resolution_clock::now();
            
            // Calculate duration in microseconds
            long long duration = chrono::duration_cast<chrono::microseconds>(end - start).count();
            
            cout << setw(10) << n << setw(20) << duration << endl;
            outfile << n << "\t" << duration << endl;
            
            delete[] arr;
        }
        
        cout << "\nData saved to 'quicksort_analysis.txt'" << endl;
        cout << "Use Python to plot the graph from this data." << endl;
        outfile.close();
    }
    else
    {
        cout << "Invalid choice!" << endl;
    }

    return 0;
}

void quick_sort(int a[], int l, int u)
{
    int j;
    if (l < u)
    {
        j = partition(a, l, u);
        quick_sort(a, l, j - 1);
        quick_sort(a, j + 1, u);
    }
}

int partition(int a[], int l, int u)
{
    int v, i, j, temp;
    v = a[l];
    i = l;
    j = u + 1;
    
    do
    {
        do
            i++;
        while (a[i] < v && i <= u);
        do
            j--;
        while (v < a[j]);
        if (i < j)
        {
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }
    } while (i < j);
    
    a[l] = a[j];
    a[j] = v;
    return (j);
}

void generateRandomArray(int arr[], int n)
{
    srand(time(0));
    for (int i = 0; i < n; i++)
        arr[i] = rand() % 10000;
}
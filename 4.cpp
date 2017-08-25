#include <iostream>
#include <cstdlib>
#include <iomanip>
 
using namespace std;
 
void evaluapoli(int n, double *f, double x, double &p);
double factorial(int n);
 
int main()
{
    int i, n, prod = -1;
    cout << "Aproximacion polinomica para el e^x (grado)= ";
    cin >> n; 
    double *f;  
    f = new double [n+1];
    for (i = 0; i <= n; i++)
    {       
        f[i] = (1/factorial(i));
    }
    cout << "\n";
    cout << "e^x, x= ";
    double x, p=0;
    cin >> x;
    cout << endl;
    evaluapoli (n, f, x, p);
    cout << "e(" << x << ") = ";
    cout.setf(ios::fixed);
    cout.precision(9);
    cout << p << endl;
    cout << endl;
    return 0;
}
void evaluapoli(int n, double *f, double x, double &p){
    int i;  
    double *a;
    a = new double [n];
    for (i = 0; i <= n; i++)
    {
        a[i] = f[i];                   
    }   
    for (i = n; i > 0; i--)
    {
        p = a[i] * x + a[i - 1];
        a[i - 1] = p;
    }
}
double factorial(int n)
{
    int i;
    double factor = 1;
    for (i = n; i >= 1; i--)
        factor *= i;
    return factor;  
}
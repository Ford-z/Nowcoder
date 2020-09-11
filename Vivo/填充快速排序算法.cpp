inline void swap(int &a, int &b) {
    int t = a; 
    a = b; 
    b = t;
    }
    
int partition(int *a, int p, int r) {
    int x = a[r-1];
    int i = p - 1;
    for(int j = p; j < r - 1; ++j) {
        if (a[j] <= x) {/*当末尾元素较大时*/
        i++;
        swap(a[i],a[j]);
        }
    }
    swap(a[i+1],a[r-1]);
    return i + 1;
    } 

void quicksort(int *a, int p, int r) {
    if (p < r - 1) {
        int q = partition(a, p, r);
        quicksort(a, p, q);
        quicksort(a, q+1, r);
    }
}

int main( ) {
    const int N = 100;
    int a[N]; // Initialized
    quicksort(a, 0, N);
    return 0; 
    }/*https://www.cnblogs.com/banyu/p/6660276.html*/

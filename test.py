from APIcomparatorlib import APIComparator

def api_comparison():
    file1 = 'file1.txt'
    file2 = 'file2.txt'

    api_comparator = APIComparator(file1, file2)
    api_comparator.compare_responses()

    

if __name__ == '__main__':
    api_comparison()

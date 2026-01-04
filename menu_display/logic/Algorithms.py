def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_obj = arr[len(arr) // 2]
    pivot_val = pivot_obj.stok 
    
    kiri = [x for x in arr if x.stok < pivot_val]
    tengah = [x for x in arr if x.stok == pivot_val]
    kanan = [x for x in arr if x.stok > pivot_val]
    return quicksort(kiri) + tengah + quicksort(kanan)
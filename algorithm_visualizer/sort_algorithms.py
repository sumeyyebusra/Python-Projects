import time

def bubble_sort(veri,grafik_olustur):
    for i in range(len(veri)-1):
        for j in range(len(veri)-1):
            if veri[j] > veri[j+1]:
                veri[j], veri[j+1] = veri[j+1], veri[j]
                grafik_olustur(veri)
                time.sleep(0.3)

def selection_sort(veri,grafik_olustur):
    for i in range(len(veri)):
        index = i
        for j in range(i+1,len(veri)):
            if veri[j] < veri[index]:
                index = j
        veri[i], veri[index] = veri[index], veri[i]
        grafik_olustur(veri)
        time.sleep(0.3)

def insertion_sort(veri,grafik_olustur):
    for i in range(1, len(veri)):
        item = veri[i]
        j = i - 1
        while j >= 0 and veri[j] > item:
            veri[j + 1] = veri[j]
            j -= 1
        veri[j + 1] = item
        grafik_olustur(veri)
        time.sleep(0.3)

def partition(veri,bas,son,grafik_olustur):
    b = bas
    pivot = veri[son]

    grafik_olustur(veri)
    time.sleep(0.1)

    for i in range(bas,son):
        if veri[i] < pivot:
            grafik_olustur(veri)
            time.sleep(0.1)

            veri[b], veri[i] = veri[i], veri[b]
            b += 1

        grafik_olustur(veri)
        time.sleep(0.1)

    grafik_olustur(veri)
    time.sleep(0.1)
    veri[b], veri[son] = veri[son], veri[b]

    return b

def quick_sort(veri,bas,son,grafik_olustur):
    if bas < son:
        index = partition(veri,bas,son,grafik_olustur)
        quick_sort(veri,bas,index-1,grafik_olustur)
        quick_sort(veri,index+1,son,grafik_olustur)

def merge_sort(veri,grafik_olustur):
    merge_sort_alg(veri,0,len(veri)-1,grafik_olustur)


def merge_sort_alg(veri,left,right,grafik_olustur):
    if left < right:
        middle = (left+right) //2
        merge_sort_alg(veri,left,middle,grafik_olustur)
        merge_sort_alg(veri, middle+1, right, grafik_olustur)
        merge(veri,left,middle,right,grafik_olustur)

def merge(veri,left,middle,right,grafik_olustur):
    grafik_olustur(veri)
    time.sleep(0.2)
    leftPart = veri[left:middle+1]
    rightPart = veri[middle+1:right+1]

    leftIdx = rightIdx = 0

    for veriIdx in range(left,right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                veri[veriIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                veri[veriIdx] = rightPart[rightIdx]
                rightIdx += 1
        elif leftIdx < len(leftPart):
            veri[veriIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            veri[veriIdx] = rightPart[rightIdx]
            rightIdx += 1
    grafik_olustur(veri)
    time.sleep(0.2)



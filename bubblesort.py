def bubblesort():
    do  
        swapped = false
        for i = 1 to indexofLastUnsortedElement -1
        if leftEl > rightEl:
            swap(leftEl, rightEl)
            swapped = True
    while swapped #notice scope of this & do 
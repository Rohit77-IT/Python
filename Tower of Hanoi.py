def TOH(n,fromrod,torod,auxrod):
    if(n==1):
        print(f"The disk 1 has been moved from {fromrod} rod to {torod} rod\n")
        return
    TOH(n-1,fromrod,auxrod,torod)
    print(f"The disk {n} has been moved from {fromrod} rod to {torod} rod\n")
    TOH(n-1,auxrod,torod,fromrod)
num = int(input("Enter the number of disks: "))
TOH(num,'A','B','C')
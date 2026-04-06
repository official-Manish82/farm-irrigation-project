#include <stdio.h>
#include <conio.h>
void merge(int a[8], int s, int e)
{
     int mid=(s+e)/2;

  int i=s;
  int j=mid+1;
  int k=s;
  int temp[10];

  while(i<=mid && j<=e)
  {
      if(a[i]<a[j])
      {
          temp[k]=a[i];
          i++;
          k++;
      }
      else
      {
          temp[k]=a[j];
          j++;
          k++;
      }
  }
  while(i<=mid)
  {
      temp[k]=a[i];
      i++;
      k++;
  }
  while(j<=e)
  {
      temp[k]=a[j];
      j++;
      k++;
  }
  for(int p=s; p<=e; p++)
  {
      a[p]=temp[p];
  }
  
}
#include "stdio.h"
#include<stdlib.h>
#define n 10
#define m 4
void main()
{
int ym[n],i,j,q,mem[m]={0},table[m][n];
char flag,f[n];
	printf("������ҳ���������\n");
	for(i=0;i<n;i++)                    
	scanf("%d",&ym[i]);
	printf("\n");
	for(i=0;i<n;i++)                    //��ҳ�����Ƿ�ȱҳ
 {  
q=0;
 	while((ym[i]!=mem[q])&&(q!=m)) q++;
 	if(q==m)  flag='*';                 //ȱҳ�����ñ�־flagΪ'*'
 	else flag=' ';
 		if(flag=='*')
 		{
for(j=m-1;j>0;j--)              //��̭���ȵ����ҳ����뵱ǰ���ʵ�
 		mem[j]=mem[j-1];
 		mem[0]=ym[i];
 		}
 		for(j=0;j<m;j++)               
 		table[j][i]=mem[j];
 		f[i]=flag;
 }
 printf("������Ϊ�±�0����Ϊ�գ�*������ȱҳ����\n");
 for(i=0;i<m;i++)
 {
 	for(j=0;j<n;j++)
printf("%3d",table[i][j]);
printf("\n");
 }
 for(i=0;i<n;i++)
 printf("%3c",f[i]);
 system("pause");
}

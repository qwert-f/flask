#include "stdio.h"
#include<stdlib.h>
#define n 10
#define m 4
void main()
{
int ym[n],i,j,q,mem[m]={0},table[m][n];
char flag,f[n];
	printf("请输入页面访问序列\n");
	for(i=0;i<n;i++)                    
	scanf("%d",&ym[i]);
	printf("\n");
	for(i=0;i<n;i++)                    //查页表，看是否缺页
 {  
q=0;
 	while((ym[i]!=mem[q])&&(q!=m)) q++;
 	if(q==m)  flag='*';                 //缺页，则置标志flag为'*'
 	else flag=' ';
 		if(flag=='*')
 		{
for(j=m-1;j>0;j--)              //淘汰最先调入的页面调入当前访问的
 		mem[j]=mem[j-1];
 		mem[0]=ym[i];
 		}
 		for(j=0;j<m;j++)               
 		table[j][i]=mem[j];
 		f[i]=flag;
 }
 printf("输出结果为下表（0代表为空，*代表有缺页）：\n");
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

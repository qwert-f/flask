#include<stdio.h>
#include<stdlib.h>
#include<conio.h> //getch()
#include<iostream.h>
#include<string.h>
#include<iomanip.h> 

const int MAXJOB=20;      //���������ҵ�� 

typedef struct node
{     //�ṹ��
   int start; 
   int length; 
   char tag[20]; 
}job; 

job frees[MAXJOB];//����������� 
int free_quantity; 

job occupys[MAXJOB];//�����ѷ������� 
int occupy_quantity; 

//��ʼ������ 
void initial() 
{ 
    int i; 

    for(i=0;i<MAXJOB;i++)
	{ 
       frees[i].start=0; 
       frees[i].length=1024; 
       strcpy(frees[i].tag,"free"); //��ʶ������"free"

       occupys[i].start=0; 
       occupys[i].length=0; 
       strcpy(occupys[i].tag,""); //��ʶ�ѷ�����
	} 
       free_quantity++; 
       //occupy_quantity=0; 
} 

//��ʾ 
void print() 
{ 
   int i; 

   cout<<endl<<"----------------------------------------------------------"<<endl; 
   cout<<"��ǰ���б�:"<<endl; 
   cout<<"��ʼ��ַ    ����     ״̬"<<endl; 
   for(i=0;i<free_quantity;i++)
   { 
   cout.setf(2); 
   cout.width(12); 
   cout<<frees[i].start; 
   cout.width(10); 
   cout<<frees[i].length; 
   cout.width(8); 
   cout<<frees[i].tag<<endl; 
   } 

   cout<<endl<<"----------------------------------------------------------"<<endl; 
   cout<<"��ǰ�ѷ����:"<<endl; 
   cout<<"��ʼ��ַ    ����     ��ҵ��"<<endl; 
   for(i=0;i<occupy_quantity;i++)
   { 
      cout.setf(2); 
      cout.width(12); 
      cout<<occupys[i].start; 
      cout.width(10); 
      cout<<occupys[i].length; 
      cout.width(8); 
      cout<<occupys[i].tag<<endl; 
   } 
} 

void excellent() //�����ڴ棬������ҵ������ѷ����㷨����xk��С�Ŀռ�(OPT)
{ 
char job_name[20]; 
int job_length; 
int i,flag; 

cout<<"�������������ڴ�ռ����ҵ���Ϳռ��С:"; 
cin>>job_name>>job_length; 

flag=0; //�������ռ��Ƿ�ɹ�,"0"�ɹ�,"1"ʧ��
for(i=0;i<free_quantity;i++)
{ 
   if(frees[i].length>=job_length)
   { //���Ҫ������ڴ�ռ�С�ڵ�ǰ��������С,����flag=1��ʾ����ռ�ɹ�
     flag=1; 
   } 
} 
if(flag==0)//����Ƿ���������Ҫ��
{ 
  cout<<endl<<"�Բ���,��ǰû�������������볤�ȵĿ����ڴ�,���Ժ�����"<<endl; 
} 
else
{ 
  i--; 
  for(int j=0;j<free_quantity;j++)
  { 
   if((frees[j].length>=job_length)&&(frees[j].length<frees[i].length))
   //Ѱ������ʿ�����,���ҵ�����������������С��
   { 
   i=j; //jΪ�ֲ�����;
   } 
  } 

  occupys[occupy_quantity].start=frees[i].start; //�����ڴ�,��ʼ��ַ
  strcpy(occupys[occupy_quantity].tag,job_name); //������ҵ��
  occupys[occupy_quantity].length=job_length;    //ռ�е��ڴ��С(����)
  occupy_quantity++; 

  if(frees[i].length>job_length)//����������Ҫ����Ŀռ��С
  { 
    frees[i].start+=job_length; //�޸Ŀ���������ʼ��ַ������
    frees[i].length-=job_length; 
  } 
  else                          //���
  { 
    for(j=i;j<free_quantity-1;j++)
	{ 
    frees[j]=frees[j+1]; 
	} 
    free_quantity--; 
     
  } 
cout<<"��ϲ��!�ڴ�ռ�ɹ�:)"<<endl<<endl;
} 
} 
 

//������ҵ 
void mfree() 
{ 
  char job_name[20]; 
  int i,j,flag,p=0; 
  int start; 
  int length; 

  cout<<"������Ҫ��������ҵ��:"; 
  cin>>job_name; 

   flag=-1; //��ʶ�Ƿ����Ҫ��������ҵ��,"-1"��ʾû��
   for(i=0;i<occupy_quantity;i++)
   { 
     if(!strcmp(occupys[i].tag,job_name))//�ҵ�Ҫ��������ҵ(ƥ��)
	 { 
      flag=i; //�ҵ�ƥ����ҵ���±�
      start=occupys[i].start; 
      length=occupys[i].length; 
	 } 
   } 
   if(flag==-1){ 
   cout<<"û�������ҵ��"<<endl; 
} 
else
{ //�ҵ���ҵ��;
//������б� 
  for(i=0;i<free_quantity;i++)
  { 
    if((frees[i].start+frees[i].length)==start)  // Ѱ�һ��շ���,���ڿ����������ڿ�����������ϲ�(0 1 0)
	{ 
       if(((i+1)<free_quantity)&&(frees[i+1].start==start+length))
	   { 
         frees[i].length=frees[i].length+frees[i+1].length+length; 
         for(j=i+1;j<free_quantity;j++)
		 { 
           frees[j]=frees[j+1]; 
		 } 
           free_quantity--; 
           p=1; 
	   } 
       else //���ڿ����������ڷǿ������������ںϲ�(0 1 1)
	   { 
        frees[i].length+=length; 
        p=1; 
	   } 
	} 
    if(frees[i].start==(start+length)){ // ���ڷǿ�����������Ϊ�������������ںϲ�(1 1 0) or 1 0 1
    frees[i].start=start; 
    frees[i].length+=length; 
    p=1; 
	} 
  } 

  if(p==0)
  { 
    frees[free_quantity].start=start; 
    frees[free_quantity].length=length; 
    free_quantity++; 
  } 

//ɾ��������еĸ���ҵ 

   for(i=flag;i<occupy_quantity;i++)
   { 
    occupys[i]=occupys[i+1]; 
   } 
   occupy_quantity--; 
} 
} 

void main() 
{ 

int flag=0; 
int t=1; 
int chioce=0; 

initial(); 

while(1)
{ 
cout<<"========================================================="<<endl; 
cout<<"=                      �洢����ģ��ϵͳ                 ="<<endl; 
cout<<"========================================================="<<endl; 
cout<<"=                              1.����ռ�(�������䷨)   ="<<endl; 
cout<<"=                              2.������ҵ               ="<<endl;
cout<<"=                              3.��ʾ���б�ͷ����     ="<<endl; 
cout<<"=                              0.�˳�                   ="<<endl;
cout<<"========================================================="<<endl; 
cout<<"====����ѡ�����(0~3):"; 
cin>>chioce; 

switch(chioce)
{ 
  case 1: 
    excellent();  //���������㷨�����ڴ�
    break; 
  case 2: 
    mfree();     //�ͷ���ҵռ�е��ڴ�
    break; 
  case 3: 
    print();    //��ʾ�ڴ�������
    break;  
  case 0: 
    exit(0);
  default: 
cout<<"��ѡ��Ĳ������������䣡"<<endl; 
} 
} 
}

#include <windows.h>
#include <stdio.h>
float t,d; /*��������ȫ�ֱ���*/
struct /*����һ���ṹ�����飬�������̵���Ϣ*/
{
	int id;
	float ArriveTime;
	float RequestTime;
	float StartTime;
	float EndTime;
	float RunTime;
	float DQRunTime;
	int Status;
}arrayTask[4]; /*�����ʼ���Ľṹ������*/

void GetTask()/*���ṹ�����鸳ֵ�����뵽�����ʱ��*/
{ 
	int i;
	float a;
	for(i=0;i<4;i++)
	{
		arrayTask[i].id=i+1;
		printf("input the number\n");
		printf("input the the ArriveTime of arrayTask[%d]:",i); /*�û�������̵�ʱ�䣬��ʼΪ�� */
		scanf("%f",&a);
		arrayTask[i].ArriveTime=a;
		printf("\n");
		printf("input the RequestTime of arrayTask[%d]:",i);
		scanf("%f",&a);
		arrayTask[i].RequestTime=a;
		arrayTask[i].StartTime=0;
		arrayTask[i].EndTime=0;
		arrayTask[i].RunTime=0;
		arrayTask[i].Status=0; /*��ʼĬ�ϵı�־λ��*/
	}
}

int fcfs() /*����FCFS��Ѱ��δִ�еĽ��̵����ȵ���ʱ��*/
{ 
	int i,w=0; /*�ڽṹ���������ҵ�һ��δִ�еĽ���*/ 
	for(i=0;i<4;i++) 
	{ 
		if(arrayTask[i].Status==0) 
		{ 
			t=arrayTask[i].ArriveTime; 
			w=1; 
		} 
		if(w==1) 
			break; 
	} 

	for(i=0;i<4;i++) /*���������е���ʱ����Сδִ�еĽ���*/
	{ 
		if(arrayTask[i].ArriveTime<t&&arrayTask[i].Status==0) 
			t=arrayTask[i].ArriveTime; 
	} /*������С����ʱ���������±�*/ 
	
	for(i=0;i<4;i++)
	{ 
		if (arrayTask[i].ArriveTime==t) 
			return i; 
	} 
} 


int sjf() /*����FCFS��Ѱ��δִ�еĽ��̵����ȵ���ʱ��*/
{
	int i,x=0,a=0,b=0; /*�ж��ǲ��ǵ�һ��ִ�еĽ���*/
	float g;
	for(i=0;i<4;i++)
	{
		if(arrayTask[i].Status==1)
		{
			g=arrayTask[i].EndTime;
			x=1;
		}
	}
	
	if(x==0) /*��һ��ִ�еĽ��̰�FCFS*/
	{
		t=arrayTask[0].ArriveTime;
		for(i=0;i<4;i++)
		{
			if(arrayTask[i].ArriveTime<t)
			{
				t=arrayTask[i].ArriveTime;
				a=i;
			}
		}
		return a;
	}
	else
	{
		for(i=0;i<4;i++)
		{
			if(arrayTask[i].EndTime>g)
				g=arrayTask[i].EndTime;
		}
		for(i=0;i<4;i++)
		{
			if(arrayTask[i].Status==0&& arrayTask[i].ArriveTime<=g)
			{
				t=arrayTask[i].RequestTime;
				a=i;
				b=1;
			} /*�ж���û�н�����ǰ���������ǰ����*/
		}
		
		if(b!=0) /*�н��̵�����SJF*/
		{
			for(i=0;i<4;i++)
			{
				if(arrayTask[i].Status==0&&arrayTask[i].ArriveTime<=g&&arrayTask[i].RequestTime<t)
				{
					t=arrayTask[i].RequestTime;
					a=i;
				}
			}
			return a;
		}
		else
		{ /*����FCFS*/
			for(i=0;i<4;i++)
			{
				if(arrayTask[i].Status==0)
					t=arrayTask[i].ArriveTime;
			}
			for(i=0;i<4;i++)
			{
				if(arrayTask[i].Status==0&&arrayTask[i].ArriveTime<t)
				{
					t=arrayTask[i].ArriveTime;
					a=i;
				}
			}
			return a;
		}
	}
}


void neww(int s) /*����ִ�н��̺�������ݵ��޸�*/
{ 
	int i,g=0;
	for(i=0;i<4;i++)
	{
		if(arrayTask[i].Status==0)
			continue;
		else
		{
			g=1;
			break;
		}
	}
	
	if(g==0) /*��������ǵ�һ��δִ�еĽ���ʱִ��*/
	{
		arrayTask[s].StartTime=arrayTask[s].ArriveTime;
		arrayTask[s].EndTime=arrayTask[s].RequestTime+arrayTask[s].ArriveTime;
		arrayTask[s].RunTime=arrayTask[s].RequestTime;
		arrayTask[s].Status=1;
		g=2;
	}
	
	if(g==1) /*������Ĳ��ǵ�һ��δִ�еĽ���ʱִ��*/
	{
		arrayTask[s].Status=1;
		for(i=0;i<4;i++)
		{
			if(arrayTask[i].Status==1)
				d=arrayTask[i].EndTime;
		}

		for(i=0;i<4;i++) /*�������ִ�еĽ��̵����ʱ��*/
		{
			if(arrayTask[i].EndTime>d&&arrayTask[i].Status==1)
				d=arrayTask[i].EndTime;
		}

		if(arrayTask[s].ArriveTime<d) /*�ж��޸ĵĽ��̵ĵ���ʱ���Ƿ���ǰһ��ִ�еĽ��̵����ʱ��ǰ��*/
			arrayTask[s].StartTime=d;
		else
			arrayTask[s].StartTime=arrayTask[s].ArriveTime;
		arrayTask[s].EndTime=arrayTask[s].StartTime+arrayTask[s].RequestTime;
		arrayTask[s].RunTime=arrayTask[s].EndTime-arrayTask[s].ArriveTime;
	}
	arrayTask[s].DQRunTime=arrayTask[s].RunTime/arrayTask[s].RequestTime;
}

void Printresult(int j) /*�����ӡ����*/
{
	printf("%d\t",arrayTask[j].id);
	printf("%5.2f\t",arrayTask[j].ArriveTime);
	printf("%5.2f\t",arrayTask[j].RequestTime);
	printf("%5.2f\t",arrayTask[j].StartTime);
	printf("%5.2f\t",arrayTask[j].EndTime);
	printf("%5.2f\t",arrayTask[j].RunTime);
	printf("%5.2f\n",arrayTask[j].DQRunTime);
}

void main()
{ 
	int i,b,k,c=0;
	char a;
	int d[4];
	//clrscr();
	printf("\t F. FCFS \n");
	printf("\t S. SFJ  \n");
	printf("\t Q. EXIT \n");
	for(i=0;;i++)
	{
		if(c)
			break;
		printf("please input the number a:\n");
		scanf("%c",&a);
		switch(a)
		{
		case 'Q': 
			c=1;
			break;
		case 'F':
			printf("please input the different-ArriveTime of arrayTasks\n");
			GetTask();
			printf("*****************************the result of fcfs\n");
			printf("Number\tArrive\tServer\tStart\tFinish\tTurnove\tTake power turnover time\n");
			for(b=0;b<4;b++) /*�������������ı�ṹ������ֵ*/
			{
				k=fcfs();
				d[b]=k;
				neww(k);
			}
			for(b=0;b<4;b++)
				Printresult(d[b]);/*���ô�ӡ����������*/
			continue;
		case 'S': 
			printf("please input the different-RequestTime of arrayTasks\n");
			GetTask();
			printf("******************************the result of sjf\n");
			printf("Number\tArrive\tRequest\tStart\tEnd\tRun\tDQRun time\n");
			for(b=0;b<4;b++)
			{
				k=sjf();
				d[b]=k;
				neww(k);
			}
			for(b=0;b<4;b++)
				Printresult(d[b]);
			continue;
		default:
			printf("the number Error.please input another number!\n");
		}
	}
}



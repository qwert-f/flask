#include <windows.h>
#include <stdio.h>
float t,d; /*定义两个全局变量*/
struct /*定义一个结构体数组，包括进程的信息*/
{
	int id;
	float ArriveTime;
	float RequestTime;
	float StartTime;
	float EndTime;
	float RunTime;
	float DQRunTime;
	int Status;
}arrayTask[4]; /*定义初始化的结构体数组*/

void GetTask()/*给结构体数组赋值，输入到达，服务时间*/
{ 
	int i;
	float a;
	for(i=0;i<4;i++)
	{
		arrayTask[i].id=i+1;
		printf("input the number\n");
		printf("input the the ArriveTime of arrayTask[%d]:",i); /*用户输入进程的时间，初始为零 */
		scanf("%f",&a);
		arrayTask[i].ArriveTime=a;
		printf("\n");
		printf("input the RequestTime of arrayTask[%d]:",i);
		scanf("%f",&a);
		arrayTask[i].RequestTime=a;
		arrayTask[i].StartTime=0;
		arrayTask[i].EndTime=0;
		arrayTask[i].RunTime=0;
		arrayTask[i].Status=0; /*开始默认的标志位零*/
	}
}

int fcfs() /*定义FCFS中寻找未执行的进程的最先到达时间*/
{ 
	int i,w=0; /*在结构体数组中找到一个未执行的进程*/ 
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

	for(i=0;i<4;i++) /*查找数组中到达时间最小未执行的进程*/
	{ 
		if(arrayTask[i].ArriveTime<t&&arrayTask[i].Status==0) 
			t=arrayTask[i].ArriveTime; 
	} /*返回最小到达时间的数组的下标*/ 
	
	for(i=0;i<4;i++)
	{ 
		if (arrayTask[i].ArriveTime==t) 
			return i; 
	} 
} 


int sjf() /*定义FCFS中寻找未执行的进程的最先到达时间*/
{
	int i,x=0,a=0,b=0; /*判断是不是第一个执行的进程*/
	float g;
	for(i=0;i<4;i++)
	{
		if(arrayTask[i].Status==1)
		{
			g=arrayTask[i].EndTime;
			x=1;
		}
	}
	
	if(x==0) /*第一个执行的进程按FCFS*/
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
			} /*判断有没有进程在前个进程完成前到达*/
		}
		
		if(b!=0) /*有进程到达则按SJF*/
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
		{ /*否则按FCFS*/
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


void neww(int s) /*定义执行进程后相关数据的修改*/
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
	
	if(g==0) /*当处理的是第一个未执行的进程时执行*/
	{
		arrayTask[s].StartTime=arrayTask[s].ArriveTime;
		arrayTask[s].EndTime=arrayTask[s].RequestTime+arrayTask[s].ArriveTime;
		arrayTask[s].RunTime=arrayTask[s].RequestTime;
		arrayTask[s].Status=1;
		g=2;
	}
	
	if(g==1) /*当处理的不是第一个未执行的进程时执行*/
	{
		arrayTask[s].Status=1;
		for(i=0;i<4;i++)
		{
			if(arrayTask[i].Status==1)
				d=arrayTask[i].EndTime;
		}

		for(i=0;i<4;i++) /*查找最后执行的进程的完成时间*/
		{
			if(arrayTask[i].EndTime>d&&arrayTask[i].Status==1)
				d=arrayTask[i].EndTime;
		}

		if(arrayTask[s].ArriveTime<d) /*判断修改的进程的到达时间是否在前一个执行的进程的完成时间前面*/
			arrayTask[s].StartTime=d;
		else
			arrayTask[s].StartTime=arrayTask[s].ArriveTime;
		arrayTask[s].EndTime=arrayTask[s].StartTime+arrayTask[s].RequestTime;
		arrayTask[s].RunTime=arrayTask[s].EndTime-arrayTask[s].ArriveTime;
	}
	arrayTask[s].DQRunTime=arrayTask[s].RunTime/arrayTask[s].RequestTime;
}

void Printresult(int j) /*定义打印函数*/
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
			for(b=0;b<4;b++) /*调用两个函数改变结构体数的值*/
			{
				k=fcfs();
				d[b]=k;
				neww(k);
			}
			for(b=0;b<4;b++)
				Printresult(d[b]);/*调用打印函数打出结果*/
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



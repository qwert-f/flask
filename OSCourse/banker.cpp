#include <iostream.h>
#include <vector> 
#include <iomanip>
using namespace std; 
#define TRUE 1         //���� TRUE =1
#define FALSE 0        //���� FLASE=0
void bank(vector<int>,vector<vector<int> >,vector<vector<int> >,int ,int );                             //����bank��Ӧ�м��㷨��
int  safe(vector<int> Available,vector<vector<int> > Need,vector<vector<int> > Allocation,int n,int m);//����safe������ȫ���㷨
void init();
/*************************************������main()**************************************************************/
void main()
{
	init();
	int safe(vector<int> Available,vector<vector<int> > Need,vector<vector<int> > Allocation,int n,int m);
}
/**************************************��ʼ������init()*********************************************************/
void init()
{
	int m;  //m��Դ����
	int n;  //������
	cout<<"������Դ����"<<endl;
	cin>>m;
	vector<int>  Available(m); //��̬��������Available������Դ���� 
	cout<<"���������Դ����:"<<endl;
	/************************************************************************/
	            /* ����ı��յ���Ϊ��DOS��������Դ����*/
	            /*δ���յ����Ǵ�Available.txt�ļ��ж�������*/
	/************************************************************************/
	/*
	for (int i=0;i<m;i++)
	{
		cout<<"����R"<<i<<"����Դ����:";
		cin>>Available[i];
	}*/
	FILE *fp;
	fp=fopen("Available.txt","r+");
	cout<<"��Available.txt�ļ��ж������ݣ������"<<endl;
	for(int i=0;i<m;i++)
	{
		fscanf(fp,"%d",&Available[i]);
		cout<<Available[i]<<'\t';
	}
	fclose(fp);
	cout<<"\n���������"<<endl;
	cin>>n;
	vector<vector<int> >  Max(n, vector<int>(m));
	/************************************************************************/
	/* ����ı��յ���Ϊ��DOS��������Դ����*/
	/*δ���յ����Ǵ�Max.txt�ļ��ж�������*/
	/************************************************************************/
	/*
	for (  i=0;i<n;i++)
	{
		cout<<"�������"<<i<<"�������������";
		for (int j=0;j<m;j++)
		{
			cout<<"           ������ҪR"<<j<<"����Դ�������Ŀ";
			cin>>Max[i][j];
			while (Max[i][j]>Available[j])
			{
				cout<<j<<"����Դ������󳬹�������Դ��������������";
				cin>>Max[i][j];
			}
		}
	}//*/
	fp=fopen("Max.txt","r+");
	cout<<"��Max.txt�ļ��ж������ݣ������"<<endl;
	for(i=0;i<n;i++) 
	{
		for (int j=0;j<m;j++)
		{
			fscanf(fp,"%d",&Max[i][j]);
			cout<<Max[i][j]<<"  ";
		}
		cout<<endl;
	}
	fclose(fp);
	cout<<"�����ѷ����Allocation"<<endl;
	vector<vector<int> >  Allocation(n, vector<int>(m));
	vector<vector<int> >  Need(n, vector<int>(m));
	/************************************************************************/
	/* ����ı��յ���Ϊ��DOS��������Դ����*/
	/*δ���յ����Ǵ�Allocation.txt�ļ��ж�������*/
	/************************************************************************/
	/*
	for ( i=0;i<n;i++)
	{
		cout<<"����Ϊ����"<<i<<"�ķ�������";
		for (int j=0;j<m;j++)
		{
			cout<<"     �������R"<<j<<"����Դ����Ŀ";
			cin>>Allocation[i][j];
			while(Allocation[i][j]>Max[i][j])
			{
				cout<<j+1<<"����Դ������󳬹�����������Դ��������������";
				cin>>Allocation[i][j];
			}
			Need[i][j]=Max[i][j]-Allocation[i][j];
			Available[j] =Available[j]-Allocation[i][j];
		}
	}//*/
	fp=fopen("Allocation.txt","r+");
	cout<<"Allocation.txt���ļ��ж������ݣ������"<<endl;
	
	for(i=0;i<n;i++)
	{
		for (int j=0;j<m;j++)
		{
			fscanf(fp,"%d",&Allocation[i][j]);
			Need[i][j]=Max[i][j]-Allocation[i][j];               //�ڳ�ʼ��Maxʱ��ͬʱ��ʼ��Need����
			Available[j] =Available[j]-Allocation[i][j];         //�ڳ�ʼ��Maxʱ��ͬʱ�޸�Available����
			cout<<Allocation[i][j]<<' ';
		}
		cout<<endl;
		
	}
	fclose(fp);
	int safe(vector<int> Available,vector<vector<int> > Need,vector<vector<int> > Allocation,int n,int m);
	cout<<"��״̬��ȫ!"<<endl;
	
	bank(Available,Need,Allocation,n,m);//�������м��㷨bank()����
}

/**************************************���м��㷨bank()����*********************************************************/
void bank(vector<int> Available,vector<vector<int> > Need,vector<vector<int> > Allocation,int n,int m)
{
	vector<int> Request(m);
	int all=0;
	//�������all�����all==0����ʾ�����Ѿ������꣬���all>=1����ʾ���н���û��������
	for (int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			all +=Need[i][j];
	if (0==all)
	{
		cout<<"���н����Ѿ������꣬����"<<endl;
		exit(0);
	} 
	int jc;//��ѡһ������
	char again;
	all=0;//���³�ʼ��all��
	while (1)
	{
		while (all==0)
		{
			all=0;
			//���all==0����ʾ�����Ѿ������꣬���all>=1����ʾ���н���û��������
			//ѭ��ֱ��all>0,���ҵ�һ��δ������Ľ���
			cout<<"��ѡһ��������Ϊ��ǰ����0--"<<n-1<<endl;
			cin>>jc;
			for (int j=0;j<m;j++)
			{
				all += Need[jc][j];
			}
			if (0==all)
			{
				cout<<"�˽����Ѿ����У���������"<<endl;
			}
		}
		cout<<"����ý��̵���������"<<endl;
		for (i=0;i<m;i++)
		{
			cin>>Request[i];
			while(Request[i]>Need[jc][i]||Request[i]>Available[i])
			{
				
				cout<<"���������޷�����"<<endl;
						break;
        
			  }
		
		}
		//////////////////////////////////////////////////////////////////////////
		//ϵͳ��̽�Ű���Դ������ý���///////////////////////////////////////////
		for (i=0;i<m;i++)
		{
			Available[i]=Available[i]-Request[i];
			Allocation[jc][i]=Allocation[jc][i]+Request[i];
			Need[jc][i]=Need[jc][i]-Request[i];
		}
		int bb=0;
		bb=safe(Available,Need,Allocation,n,m);//���ð�ȫ���㷨���жϴ˴���Դ�����ϵͳ�Ƿ񴦰�ȫ״̬
		if (1==bb)
		{
			cout<<"ϵͳ�ɹ�������Դ"<<endl;
		}
		else
		{
			cout<<"ϵͳδ�ܳɷ�����Դ,�ջ�Ԥ������Դ"<<endl;
			for (i=0;i<m;i++)
			{
				Available[i]=Available[i]+Request[i];
				Allocation[jc][i]=Allocation[jc][i]-Request[i];
				Need[jc][i]=Need[jc][i]+Request[i];
			}
		}
		cout<<"�������ٴ����������?���밴y/Y,���밴������"<<endl;
		cin>>again;
        if(again=='y'||again=='Y')
        {
            all=0;
			continue;
        }
        break;
	}
}
/**************************************��ȫ���㷨safe()����*********************************************************/
int safe(vector<int> Available,vector<vector<int> > Need,vector<vector<int> > Allocation,int n,int m)
{
	vector<int> Work(m),Finish(n);//���빤������work��finish
	Work=Available;
	vector<int> count(n);         //��¼��ȫ����
	int len=-1;                   //��¼��ȫ���еĽ��̸��������len==n������ʾ���е�finish��i��=true�����ڰ�ȫ״̬
	for(int i=0;i<m;i++)Finish[i]=FALSE;
    for (i=0;i<n;i++)
    {
		int needed=1;
		for (int j=0;j<m;j++)
		{
			if(Need[i][j]<=Work[j])
			{
				needed=needed*TRUE;
			}
			else needed=needed*FALSE;
		}
		if ((Finish[i]==FALSE)&&needed==1)
		{
			for (j=0;j<m;j++)
			{
				Work[j]=Work[j]+Allocation[i][j];
			}
			Finish[i]=TRUE;
			len=len+1;
			count[len]=i;
			i=-1;
		}
	}
	if (len==n-1)
	{
		cout<<"ϵͳ�ǰ�ȫ��"<<endl;
		cout<<"��ȫ����"<<endl;
		for (i=0;i<=len;i++)
		{
			cout<<count[i];
			if (i!=len)
			{
				cout<<"-->";
			}
		}
		cout<<endl;
		return TRUE;
	}
	else
	{
		cout<<"ϵͳ�ǲ���ȫ��"<<endl; 	
		return FALSE;
	}
}
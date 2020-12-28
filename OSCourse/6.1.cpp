#include "stdio.h"     
#include "windows.h"

void MemoryStatus(void)                             //ͳ���ڴ��״̬
{  
	MEMORYSTATUS lpmemory;
	
	GlobalMemoryStatus(&lpmemory);//�˺���������õ�ǰ���õ�����������ڴ���Ϣ

	printf("��ǰ���ڴ�״̬��:\n");
    
	printf("\tMEMORYSTAT���ݽṹ�Ĵ�С��:%d\n",lpmemory.dwLength/(1024*1024));

	printf("\t �ڴ���������: %d%% \n",lpmemory.dwMemoryLoad);

	printf("\t �����ڴ��С��: %dMB\n",lpmemory.dwTotalPhys/(1024*1024));

	printf("\t ���������ڴ���: %dMB\n",lpmemory.dwAvailPhys/(1024*1024));

	printf("\t ҳ�ļ���С��: %dMB\n",lpmemory.dwTotalPageFile/(1024*1024));

	printf("\t ����ҳ�ļ���С��: %dMB\n",lpmemory.dwAvailPageFile/(1024*1024));

	printf("\t�����ַ�ռ��С��: %dMB\n",lpmemory.dwTotalVirtual/(1024*1024));

	printf("\t���������ַ�ռ��С��:%dMB\n\n",lpmemory.dwAvailVirtual/(1024*1024));

}
void main()
{

	LPVOID  Virtualbase;//LPVOID��һ��û�����͵�ָ�룬Ҳ����˵����Խ��������͵�ָ�븳ֵ��LPVOID���͵ı�����һ����Ϊ�������ݣ���Ȼ����ʹ�õ�ʱ����ת��������
	
	char *string;
	
	MemoryStatus();//��ȡ��ǰ���ڴ�״̬
	
	printf("���ڿ�ʼ����32MB�����ڴ��2MB�����ڴ�\n\n");
	
	Virtualbase=VirtualAlloc(NULL, 1024*1024*32, MEM_COMMIT, PAGE_READWRITE);             //���������ڴ�
	
	if (Virtualbase==NULL)	printf("�����ڴ����ʧ��\n");
	
	string=(char *)malloc(2*1024*1024); //�����ڴ�
	printf("\n������֮����ڴ�״̬����:");
	
	MemoryStatus();
	
	printf("���ڿ�ʼ�ͷ�32MB�����ڴ��2MB�����ڴ�!!\n\n");

	if(VirtualFree(Virtualbase,0,MEM_RELEASE)) //�ͷ������ڴ�                           
	
		printf("�ͷ������ڴ�ʧ��!!\n");
	
	free(string);  //�ͷ��ڴ�
	printf("\n�ͷź���ڴ�״̬:");

	MemoryStatus();
	
}

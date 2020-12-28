# include <windows.h>
# include <iostream.h>
# include <stdlib.h>
void FileRW_Nobuffer(const char * source,const char * destination);
void main()
{
	cout<<"Now read a txt file to another file!"<<endl;
	FileRW_Nobuffer("sourcee.txt","nobuffer.txt");
}
void FileRW_Nobuffer(const char * source,const char * destination)//�޻����д
{
    HANDLE hsource;
	HANDLE hDest;
	DWORD dwRead;
	DWORD dwWrite;
	char buf[1024];
    hsource=CreateFile("sourcee.txt",//��sourcee.txt����ļ�
		GENERIC_READ,//��
		0,
		NULL,
		OPEN_EXISTING,
        FILE_FLAG_NO_BUFFERING,//�ļ�����
		NULL);
	if(INVALID_HANDLE_VALUE==hsource)
	{
	 cout<<"Could not open the source file!"<<endl;
	  system("pause");
		return;
}
hDest=CreateFile("nobuffer.txt",//����nobuffer.txt����ļ�
		GENERIC_WRITE,//д
		0,
		NULL,
		CREATE_ALWAYS,
		NULL,
		NULL);
	if(INVALID_HANDLE_VALUE==hDest)//hDest�Ǵ����ļ��ľ��,����ɹ�,hDest��������ļ��ľ��,���ʧ��,����ֵ������INVALID_HANDLE_VALUE
	{
		cout<<"Could not create the destination file!"<<endl;
		return;
	}
	if(!ReadFile(hsource,buf,1024,&dwRead,NULL))
	{
		cout<<"Read source file error!"<<endl;
		return;
	}
	else
		cout<<"Read file success!"<<endl;
	if(dwRead==1024)
	{
		cout<<"����ļ����ܱ��ضϣ������ӻ������Ĵ�С!"<<endl;
	}
   if(!WriteFile(hDest,buf,dwRead,&dwWrite,NULL))
   {
	   cout<<"Read source file error!"<<endl;
	   return;
   }
   else
	   cout<<"Write file success!"<<endl;
   CloseHandle(hsource);
   CloseHandle(hDest);
}

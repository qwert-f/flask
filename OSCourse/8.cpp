# include <windows.h>
# include <iostream.h>
# include <stdlib.h>
void FileRW_Nobuffer(const char * source,const char * destination);
void main()
{
	cout<<"Now read a txt file to another file!"<<endl;
	FileRW_Nobuffer("sourcee.txt","nobuffer.txt");
}
void FileRW_Nobuffer(const char * source,const char * destination)//无缓冲读写
{
    HANDLE hsource;
	HANDLE hDest;
	DWORD dwRead;
	DWORD dwWrite;
	char buf[1024];
    hsource=CreateFile("sourcee.txt",//打开sourcee.txt这个文件
		GENERIC_READ,//读
		0,
		NULL,
		OPEN_EXISTING,
        FILE_FLAG_NO_BUFFERING,//文件属性
		NULL);
	if(INVALID_HANDLE_VALUE==hsource)
	{
	 cout<<"Could not open the source file!"<<endl;
	  system("pause");
		return;
}
hDest=CreateFile("nobuffer.txt",//创建nobuffer.txt这个文件
		GENERIC_WRITE,//写
		0,
		NULL,
		CREATE_ALWAYS,
		NULL,
		NULL);
	if(INVALID_HANDLE_VALUE==hDest)//hDest是创建文件的句柄,如果成功,hDest就是这个文件的句柄,如果失败,返回值就是是INVALID_HANDLE_VALUE
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
		cout<<"你的文件可能被截断，请增加缓冲区的大小!"<<endl;
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

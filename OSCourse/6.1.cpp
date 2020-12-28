#include "stdio.h"     
#include "windows.h"

void MemoryStatus(void)                             //统计内存的状态
{  
	MEMORYSTATUS lpmemory;
	
	GlobalMemoryStatus(&lpmemory);//此函数用来获得当前可用的物理和虚拟内存信息

	printf("当前的内存状态是:\n");
    
	printf("\tMEMORYSTAT数据结构的大小是:%d\n",lpmemory.dwLength/(1024*1024));

	printf("\t 内存利用率是: %d%% \n",lpmemory.dwMemoryLoad);

	printf("\t 物理内存大小是: %dMB\n",lpmemory.dwTotalPhys/(1024*1024));

	printf("\t 空闲物理内存是: %dMB\n",lpmemory.dwAvailPhys/(1024*1024));

	printf("\t 页文件大小是: %dMB\n",lpmemory.dwTotalPageFile/(1024*1024));

	printf("\t 空闲页文件大小是: %dMB\n",lpmemory.dwAvailPageFile/(1024*1024));

	printf("\t虚拟地址空间大小是: %dMB\n",lpmemory.dwTotalVirtual/(1024*1024));

	printf("\t空闲虚拟地址空间大小是:%dMB\n\n",lpmemory.dwAvailVirtual/(1024*1024));

}
void main()
{

	LPVOID  Virtualbase;//LPVOID是一个没有类型的指针，也就是说你可以将任意类型的指针赋值给LPVOID类型的变量（一般作为参数传递），然后在使用的时候再转换回来。
	
	char *string;
	
	MemoryStatus();//获取当前的内存状态
	
	printf("现在开始分配32MB虚拟内存和2MB物理内存\n\n");
	
	Virtualbase=VirtualAlloc(NULL, 1024*1024*32, MEM_COMMIT, PAGE_READWRITE);             //分配虚拟内存
	
	if (Virtualbase==NULL)	printf("虚拟内存分配失败\n");
	
	string=(char *)malloc(2*1024*1024); //分配内存
	printf("\n分配完之后的内存状态如下:");
	
	MemoryStatus();
	
	printf("现在开始释放32MB虚拟内存和2MB物理内存!!\n\n");

	if(VirtualFree(Virtualbase,0,MEM_RELEASE)) //释放虚拟内存                           
	
		printf("释放虚拟内存失败!!\n");
	
	free(string);  //释放内存
	printf("\n释放后的内存状态:");

	MemoryStatus();
	
}

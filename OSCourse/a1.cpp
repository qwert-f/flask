#include<stdio.h>
#include<windows.h>
#include <tchar.h>
// 头文件不可以空格
int main(void)
{
  STARTUPINFO si;
  PROCESS_INFORMATION pi;
  ZeroMemory(&si, sizeof(si));
  si.cb = sizeof(si); 
  ZeroMemory(&pi, sizeof(pi));
  if (!CreateProcess(NULL,
    /* "const char *" 类型的实参与 "LPWSTR" 类型的形参不兼容C/C++(167)
     * 报错原因代码是vc6.0写的，采用ANSII编码方式，而vscode采用unicode编码
     * 解决方法：引入头文件tchar.h
     * "c:\\WINDOWS\\system32\\mspaint.exe" --->_T("c:\\WINDOWS\\system32\\mspaint.exe")
    */
                     _T("c:\\WINDOWS\\system32\\mspaint.exe"),
                     NULL,
                     NULL,
                     FALSE,
                     0,
                     NULL,
                     NULL,
                     &si, &pi))
                     /* LPSTR被定义成是一个指向以NULL(‘\0’)结尾的32位ANSI字符数组指针
                      * 而LPWSTR是一个指向以NULL结尾的64位双字节字符数组指针。*/
  {
    fprintf(stderr, "Creat Process Failed");
    return -1;
  }
  WaitForSingleObject(pi.hProcess, INFINITE);
  printf("child Complete");
  CloseHandle(pi.hProcess);
  CloseHandle(pi.hThread);
}

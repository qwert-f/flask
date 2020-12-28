#include <windows.h>
#include <iostream.h>
#include <stdio.h>
// using namespace std;
static LPCTSTR g_szMutexName = "w2kdg.ProcTerm.mutex.Suicide";

//创建当前进程的克隆进程的简单方法
void StartClone()
{
  //提取当前可执行文件的文件名
  TCHAR szFilename[MAX_PATH];
  ::GetModuleFileName(NULL, szFilename, MAX_PATH);

  //格式化用于子进程的命令行，指明它是一个EXE文件和子进程
  TCHAR szCmdLine[MAX_PATH];
  ::sprintf(szCmdLine, "\"%s\"child", szFilename);

  //子进程的启动信息结构
  STARTUPINFO si;
  ::ZeroMemory(reinterpret_cast<void *>(&si), sizeof(si));
  si.cb = sizeof(si); //应当是此结构的大小

  //返回的用于子进程的进程信息
  PROCESS_INFORMATION pi;

  //用同样的可执行文件名和命令行创建进程，并指明它是一个子进程
  BOOL bCreateOK = ::CreateProcess(
      szFilename,         //产生的应用程序名称（本EXE文件）
      szCmdLine,          //告诉人们这是一个子进程的标志
      NULL,               //用于进程的默认的安全性
      NULL,               //用于线程的默认安全性
      FALSE,              //不继承句柄
      CREATE_NEW_CONSOLE, //创建新窗口，使输出更直观
      NULL,               //新环境
      NULL,               //当前目录
      &si,                //启动信息结构
      &pi);               //返回的进程的信息

  //释放指向子进程的引用
  if (bCreateOK)
  {
    ::CloseHandle(pi.hProcess);
    ::CloseHandle(pi.hThread);
  }
}
void Parent()
{
  //创建“自杀”互斥程序体
  HANDLE hMutexSuicide = ::CreateMutex(
      NULL,           //默认的安全性
      TRUE,           //最初拥有的
      g_szMutexName); //为其命名
  if (hMutexSuicide != NULL)
  {
    //创建子进程
    cout << "Creating the child process." << endl;
    ::StartClone();

    //暂停
    ::Sleep(5000);

    //指令子进程“杀”掉自身
    cout << "Telling the child process to quit." << endl;
    ::ReleaseMutex(hMutexSuicide);

    //消除句柄
    ::CloseHandle(hMutexSuicide);
  }
}

void Child()
{
  //打开“自杀”互斥体
  HANDLE hMutexSuicide = ::OpenMutex(
      SYNCHRONIZE,    //打开用于同步
      FALSE,          //不需要向下传递
      g_szMutexName); //名称
  if (hMutexSuicide != NULL)
  {
    //报告正在等待指令
    cout << "Child waiting for suicide instructions." << endl;
    ::WaitForSingleObject(hMutexSuicide, INFINITE);

    //报告准备好终止，消除句柄
    cout << "Child quiting." << endl;
    ::CloseHandle(hMutexSuicide);
    ::Sleep(1000);
  }
}

int main(int argc, char *argv[])
{
  //决定其行为是父进程还是子进程
  if (argc > 1 && ::strcmp(argv[1], "child") == 0)
  {
    Child();
  }
  else
  {
    Parent();
  }
  return 0;
}

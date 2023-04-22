#include <windows.h>
#include <stdio.h>
typedef void (*MYPROC)(LPTSTR);
int main()
{ 
        HINSTANCE LibHandle;
        MYPROC ProcAdd;
        LibHandle = LoadLibrary("msvcrt");
        //获取msvcrt.dll的地址
        printf("msvcrt = 0x%x\n", LibHandle);
        //获取system的地址
        ProcAdd=(MYPROC)GetProcAddress(LibHandle,"system");
        printf("system = 0x%x", ProcAdd);
        getchar();
        return 0;
}

#include <windows.h>
#include <stdio.h>
typedef void (*MYPROC)(LPTSTR);
int main()
{ 
        HINSTANCE LibHandle;
        MYPROC ProcAdd;
        LibHandle = LoadLibrary("msvcrt");
        //��ȡmsvcrt.dll�ĵ�ַ
        printf("msvcrt = 0x%x\n", LibHandle);
        //��ȡsystem�ĵ�ַ
        ProcAdd=(MYPROC)GetProcAddress(LibHandle,"system");
        printf("system = 0x%x", ProcAdd);
        getchar();
        return 0;
}

#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    BYTE *ptr;
    int position;
    int done_flag;
    HINSTANCE handle;
    handle = LoadLibrary("user32.dll");
    if(!handle)
    {
       printf("load dll error!");
       exit(0);
    }
    ptr = (BYTE*)handle;
    
    for(position = 0,done_flag = 10; done_flag > 0; position++)
    {
      try
      {
          if(ptr[position]==0xFF && ptr[position+1]==0xE4)
          {
            int address = (int)ptr + position;
            printf("OPCODE found at 0x%x\n", address);
            done_flag --;
          }             
      }
      catch(...)
      {
        int address = (int)ptr + position;
        printf("END OF 0x%x\n", address);
        done_flag = 0;
      }
    }
    system("pause");
    return 0;
}

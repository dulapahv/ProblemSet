	.file	"scratch.c"
 # GNU C17 (Rev6, Built by MSYS2 project) version 12.2.0 (x86_64-w64-mingw32)
 #	compiled by GNU C version 12.2.0, GMP version 6.2.1, MPFR version 4.1.0-p13, MPC version 1.2.1, isl version isl-0.25-GMP

 # GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
 # options passed: -mtune=generic -march=x86-64 -O2
	.text
	.section .rdata,"dr"
.LC0:
	.ascii "Hello, World!\0"
	.text
	.p2align 4
	.def	printf.constprop.0;	.scl	3;	.type	32;	.endef
	.seh_proc	printf.constprop.0
printf.constprop.0:
	pushq	%rbx	 #
	.seh_pushreg	%rbx
	subq	$48, %rsp	 #,
	.seh_stackalloc	48
	.seh_endprologue
 # C:/msys64/mingw64/include/stdio.h:372:   __retval = __mingw_vfprintf( stdout, __format, __local_argv );
	movl	$1, %ecx	 #,
 # C:/msys64/mingw64/include/stdio.h:371:   __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
	leaq	72(%rsp), %rbx	 #, tmp86
 # C:/msys64/mingw64/include/stdio.h:368: int printf (const char *__format, ...)
	movq	%rdx, 72(%rsp)	 #,
	movq	%r8, 80(%rsp)	 #,
	movq	%r9, 88(%rsp)	 #,
 # C:/msys64/mingw64/include/stdio.h:371:   __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
	movq	%rbx, 40(%rsp)	 # tmp86, MEM[(char * *)&__local_argv]
 # C:/msys64/mingw64/include/stdio.h:372:   __retval = __mingw_vfprintf( stdout, __format, __local_argv );
	call	*__imp___acrt_iob_func(%rip)	 #
	movq	%rbx, %r8	 # tmp86,
	leaq	.LC0(%rip), %rdx	 #, tmp88
	movq	%rax, %rcx	 # tmp90, _2
	call	__mingw_vfprintf	 #
 # C:/msys64/mingw64/include/stdio.h:375: }
	addq	$48, %rsp	 #,
	popq	%rbx	 #
	ret	
	.seh_endproc
	.def	__main;	.scl	2;	.type	32;	.endef
	.section	.text.startup,"x"
	.p2align 4
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	subq	$40, %rsp	 #,
	.seh_stackalloc	40
	.seh_endprologue
 # scratch.c:3: int main() {
	call	__main	 #
 # scratch.c:4:     printf("Hello, World!");
	leaq	.LC0(%rip), %rcx	 #, tmp83
	call	printf.constprop.0	 #
 # scratch.c:6: }
	xorl	%eax, %eax	 #
	addq	$40, %rsp	 #,
	ret	
	.seh_endproc
	.ident	"GCC: (Rev6, Built by MSYS2 project) 12.2.0"
	.def	__mingw_vfprintf;	.scl	2;	.type	32;	.endef

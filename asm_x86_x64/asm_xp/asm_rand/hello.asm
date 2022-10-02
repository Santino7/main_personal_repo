;This is a asm file used for random things.
;By Santino .J. Tomasi


section .data
	a_char db ' '

section .text
	global _start

_start:
	mov rax, 0
	mov rdi, 0
	mov rsi, a_char
	mov rdx, 2
	syscall

	mov rax, 1
	mov rdi, 1
	add rsi, a_char
	mov rdx, 1
	syscall

	mov rax,60
	mov rdi, 0
	syscall

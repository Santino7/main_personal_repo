;This is a asm file used for random things.
;By Santino .J. Tomasi


section .data
	a_char db "ow",0
	a_thing db "hi"

section .text
	global _start

_start:
	mov rax, 1
	mov rdi, 1
	mov rsi, a_char
	mov rdx, 3
	syscall

	mov rax, 1
	mov rdi, 1
	mov rsi, a_thing
	mov rdx, 2
	syscall
	
	mov rax,60
	mov rdi, 0
	syscall

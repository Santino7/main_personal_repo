
;By Santino .J. Tomasi
;This file is subject to change. 
;This is a asm file used for random things.
;Current program: Increases or decreases exit code to wanted value. 

section .text
	global _start
_start:
	mov rcx, 3	
	mov rdi, 55
	cmp rdi, rcx
	je end
	jl less_loop
	jg great_loop
less_loop:
	cmp rdi,rcx
	je end
	add rdi, 1
	jmp less_loop
great_loop:
	cmp rdi,rcx
	je end
	sub rdi, 1
	jmp great_loop
end:	
	mov rax,60
	syscall


;;;  This program is to search for a pattern of characters
;;; in a text string.  If the pattern occurs in the text,
;;; then your program should output the position in the
;;; text of the beginning of the first match.  If the
;;; pattern does not occur, your program should output
;;; No match.
;;; I have given you the part that
;;; reads in the pattern and text from the user
;;; into buffers called patbuf and txtbuf respectively.
;;; I have also given you output code assuming you can
;;; get the correct position into R0 just before the
;;; 	jsr	BinarytoASCII   that appears below.
;;; if there is no match you should branch to nomtch.

	.orig	x3000
;;; read in pattern
	lea	r0, patprm	; output pattern prompt
	puts
	lea     r2, patbuf      ; r2 is base for storing chars read
			;; make it point to the pattern buffer now
cntnext trap    x20             ; read next char into r0
        trap    x21             ; echo it out
        str     r0,r2,x0        ; store it into memloc pted by r2
        add     r0,r0,x-d       ; sets zero CC if r0 equals <cr>
        brz     exit            ; get out of loop
        add     r2,r2,x1        ; increment buffer ptr
        br      cntnext         ; get next char
exit	and	r1,r1,x0	; write the x0000 to
	str	r1,r2,x0	; terminate prompt string
;;; read in text
	lea	r0, txtprm	; output text prompt
	puts
	lea     r2, txtbuf      ; r2 is base for storing chars read
			;; make it point to the text buffer
txnext  trap    x20             ; read next char into r0
        trap    x21             ; echo it out
        str     r0,r2,x0        ; store it into memloc pted by r2
        add     r0,r0,x-d       ; sets zero CC if r0 equals <cr>
        brz     exit2           ; get out of loop
        add     r2,r2,x1        ; increment buffer ptr
        br      txnext          ; get next char
exit2	and	r1,r1,x0	; write the x0000 to
	str	r1,r2,x0	; terminate text string

;;; now patbuf has the pattern and txtbuf has the text
;;; start the search for a match in text

        and     r6, r6, #0      ; clear r6 for use as a pattern counter
        and     r0, r0, #0      ; clear r0 for use as a text counter (temporary)
        lea     r1, txtbuf      ; load txtbuf address into r1
        lea     r2, patbuf      ; load patbuf address into r2

compare ldr     r3, r1, #0      ; load contents of memory at txtbuf address into r3
        ldr     r4, r2, #0      ; load contents of memory at patbuf address into r4
        add     r0, r0, #1      ; increment text counter after load contents of txtbuf

        add     r4, r4, #0
        brz     found           ; if reach end of patbuf, pattern found in text

        add     r3, r3, #0
        brz     nomtch          ; if reach end of txtbuf and pattern hasn't been found,
                                ; there is no match

        not     r5, r4
        add     r5, r5, #1      ; make r4 (patbuf character) negative
        add     r5, r5, r3      ; subtract r4 from r3 (txtbug character)
        brz     equal           ; if sum = 0, characters same

        ;; if patbuf character != txtbuf character
        and     r6, r6, #0      ; clear pattern counter
        add     r1, r1, #1      ; increment txtbuf address to move on to next character
        lea     r2, patbuf      ; reset/reload original pattern into r2
        brnzp   compare         ; unconditionally branch to top to check/compare
                                ; txtbuf and patbuf characters

        ;; if patbuf character == txtbuf character
equal   add     r1, r1, #1      ; increment txtbuf address to move on to next character
        add     r2, r2, #1      ; increment patbuf address to move on to next character
        add     r6, r6, #1      ; increment pattern counter
        brnzp   compare         ; unconditionally branch to top to check/compare
                                ; txtbuf and patbuf characters

found   not     r6, r6
        add     r6, r6, #1      ; make pattern counter negative
        add     r0, r0, r6      ; subtract pattern counter from text counter and store
                                ; in r0 --> position of pattern in text string

	;; in text string; so convert to ASCII and print
	jsr	BinarytoASCII
	lea	r0, posann	; match message
	puts
	lea	r2,ASCIIBUFF	; send address of characters
	and	r4,r4,x0
	add	r4, r4,x4	; send count
	jsr	output
	halt

nomtch	lea	r0,nomsg		; no match possible
	puts
	halt

patneg	.blkw	11		; negative of chars in patbuf
				;; nul terminated

patbuf	.blkw	11		; the pattern buffer
txtbuf	.blkw	81		; the text buffer
nomsg	.stringz	"No match."
posann	.stringz  "\nThe first occurance of the pattern starts at pos: "
patprm	.stringz  "\nEnter pattern\n"
txtprm	.stringz  "\nEnter text\n"

;  This algorithm takes the 2's complement representation of a signed
;  integer, within the range -999 to +999, and converts it into an ASCII
;  string consisting of a sign digit, followed by three decimal digits.
;  R0 contains the initial value being converted.  The ASCII string
;  begins at ASCIIBUFF.
;
BinarytoASCII  st    r0,saver0	; save registers used in this subroutine
	       st    r1,saver1
	       st    r2,saver2
	       st    r3,saver3
	       LEA   R1,ASCIIBUFF  ; R1 points to string being generated
               ADD   R0,R0,#0      ; R0 contains the binary value
               BRn   NegSign       ;
               LD    R2,ASCIIplus  ; First store the ASCII plus sign
               STR   R2,R1,#0
               BRnzp Begin100
NegSign        LD    R2,ASCIIminus ; First store ASCII minus sign
               STR   R2,R1,#0
               NOT   R0,R0         ; Convert the number to absolute
               ADD   R0,R0,#1      ; value; it is easier to work with.
;
Begin100       LD    R2,ASCIIoffset ; Prepare for "hundreds" digit
;
               LD    R3,Neg100     ; Determine the hundreds digit
Loop100        ADD   R0,R0,R3
               BRn   End100
               ADD   R2,R2,#1
               BRnzp Loop100
;
End100         STR    R2,R1,#1   ; Store ASCII code for hundreds digit
               LD     R3,Pos100
               ADD    R0,R0,R3   ; Correct R0 for one-too-many subtracts
;
               LD     R2,ASCIIoffset ; Prepare for "tens" digit
;
Begin10        LD     R3,Neg10   ; Determine the tens digit
Loop10         ADD    R0,R0,R3
               BRn    End10
               ADD    R2,R2,#1
               BRnzp  Loop10
;
End10          STR    R2,R1,#2   ; Store ASCII code for tens digit
               ADD    R0,R0,#10  ; Correct R0 for one-too-many subtracts
Begin1         LD     R2,ASCIIoffset ; Prepare for "ones" digit
               ADD    R2,R2,R0
               STR    R2,R1,#3
	       ld     r0,saver0	; restore registers used
	       ld     r1,saver1
	       ld     r2,saver2
	       ld     r3,saver3
               RET
;
ASCIIplus      .FILL  x002B
ASCIIminus     .FILL  x002D
ASCIIoffset    .FILL  x0030
Neg100         .FILL  xFF9C
Pos100         .FILL  x0064
Neg10          .FILL  xFFF6
ASCIIBUFF	.blkw	4
saver0		.blkw	1
saver1		.blkw	1
saver2		.blkw	1
saver3		.blkw	1


	;; begin output part
	;; r2 holds the address of the output buffer
	;; r4 starts with the count of howmany characters to be output


output	st	r7, outret	;  store return address
	st	r0,outr0	; save registers used
	st	r2,outr2
	st	r4,outr4
outtest	brz	outexit		; branch out if done
	ldr	r0,r2,x0	; load next char for output f.memloc pted by r2
	trap	x21		; output it
	add	r2,r2,x1	; increment out buffer ptr
	add	r4,r4,x-1	; decrement counter
	br	outtest		; branch to count test

outexit	ld	r0,charret	; load r0 with ascii <cr>
	trap	x21		; output the <cr>
	ld	r7, outret	;  restore return address to r7
	ld	r0, outr0	; and other registers used
	ld	r2, outr2
	ld	r4, outr4
	ret

outret	.blkw	1		; to store return address from r7
outr0   .blkw	1		; save other registers used
outr2   .blkw	1
outr4   .blkw	1
charret	.fill	x000d		; ascii for <cr>
	.end

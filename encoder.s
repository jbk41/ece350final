.text
# put message into $r1
addi $r1, $r0, 1365
# num bits = $r6
addi $r6, $r0, 28

#max num bits is 27
addi $r2, $r0, 27
blt $r2, $r6, too_big_error

# amt to shift to start
addi $r10, $r0, 32
sub  $r28, $r10, $r6
sllr  $r1, $r1, $r28


lw $r2, 0($r0) #r2 = and_1
lw $r3, 1($r0) #r3 = and_2
lw $r4, 2($r0) #r4 = and_3
lw $r5, 3($r0) #r5 = and_4

# shift 1
and $r11, $r1, $r2 
sra $r11, $r11, 2
lw  $r10, 9($r0) # special case for rsa
and $r11, $r11, $r10 #r12  = shift 1


# shift 2
and $r12, $r1, $r3 
sra $r12, $r12, 3


# shift 3
and $r13, $r1, $r4
sra $r13, $r13, 4

# shift 4
and $r14, $r1, $r5 
sra $r14, $r14, 5

#message w parity = $r20
lw $r21, 4($r0) #r21 = p1
lw $r22, 5($r0) #r22 = p2
lw $r23, 6($r0) #r23 = p3
lw $r24, 7($r0) #r24 = p4
lw $r25, 8($r0) #r25 = p5

or $r20, $r11, $r12
or $r20, $r20, $r13
or $r20, $r20, $r14

# find num parity bits
addi $r7,  $r7, 2 # Start with 2 parity bits
addi $r15, $r15, 2
blt  $r6,  $r15, k_done # if ur bits is less than 2 (aka 1 bit) then ur done

addi $r7,  $r7, 1 # 3 parity bits
addi $r16, $r16, 5
blt  $r6,  $r16, k_done

addi $r7,  $r7, 1 # 4 parity bits
addi $r17, $r17, 12
blt  $r6,  $r17, k_done

addi $r7,  $r7, 1 # 5 parity bits


k_done:

addi $r8, $r0, 1 # holds a 1

addi $r27, $r0, 1 
blt $r7, $r27, fully_done
and $r21, $r21, $r20
xor $r26, $r21, $r21
bne $r26, $r8, skip_p1
lw  $r21, 10($r0)
or $r20, $r20, $r21


skip_p1:

addi $r27, $r27, 1 
blt $r7, $r27, fully_done
and $r22, $r22, $r20
xor $r26, $r22, $r22
bne $r26, $r8, skip_p2
lw  $r22, 11($r0)
or $r20, $r20, $r22

skip_p2:

addi $r27, $r27, 1 
blt $r7, $r27, fully_done
and $r23, $r23, $r20
xor $r26, $r23, $r23
bne $r26, $r8, skip_p3
lw  $r23, 12($r0)
or $r20, $r20, $r23

skip_p3:

addi $r27, $r27, 1 
blt $r7, $r27, fully_done
and $r24, $r24, $r20
xor $r26, $r24, $r24
bne $r26, $r8, skip_p4
lw  $r24, 13($r0)
or $r20, $r20, $r24

skip_p4:

addi $r27, $r27, 1 
blt $r7, $r27, fully_done
and $r25, $r20, $r25
xor $r26, $r25, $r25
bne $r26, $r8, skip_p5
lw  $r25, 14($r0)
or $r20, $r20, $r25

skip_p5:


fully_done:
add $r29, $r20, $r0
addi $r30, $r0, 1
j end


too_big_error:
addi $r30, $r0, 3
j end


end:

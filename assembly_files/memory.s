.text 

###
### ### ECE350: Processor Checkpoint
### ### Basic Memory Test
### ### MIPS
###

add     $r0, $r0, $r0
add     $r0, $r0, $r0
add     $r0, $r0, $r0

addi    $r1, $r1, 100
addi    $r2, $r2, 200
addi    $r3, $r3, 300
addi    $r4, $r4, 400
addi    $r5, $r5, 500

sw		$r1, 5($r2)
lw		$r6, 0($r2)
lw		$r7, 5($r2)
sw		$r3, 10($r2)
lw		$r8, 10($r2)

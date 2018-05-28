# 通道说明

# 1 Angle : 功角
psspy.chsb(0, 1, [-1, -1, -1, 1, 1, 0])  # Angel -- machine relative rotor angle (degrees).

# 2~6
psspy.chsb(0, 1, [-1, -1, -1, 1, 2, 0])  # Pelec -- machine electrical power (pu on SBASE)
psspy.chsb(0, 1, [-1, -1, -1, 1, 3, 0])  # QELEC -- machine reactive power
psspy.chsb(0, 1, [-1, -1, -1, 1, 4, 0])  # ETERM --machine terminal voltage (pu).
psspy.chsb(0, 1, [-1, -1, -1, 1, 5, 0])  # EFD -- generator main field voltage (pu)
psspy.chsb(0, 1, [-1, -1, -1, 1, 6, 0])  # PMECH -- turbine mechanical power (pu on MBASE).

# 7 Speed : 发电机转速（偏移）
psspy.chsb(0, 1, [-1, -1, -1, 1, 7, 0])  # Speed -- machine speed deviation（偏移） from nominal (pu)

# 8~11
psspy.chsb(0, 1, [-1, -1, -1, 1, 8, 0])  # XADIFD -- machine field current (pu).
psspy.chsb(0, 1, [-1, -1, -1, 1, 9, 0])  # ECOMP -- voltage regulator compensated voltage (pu).

psspy.chsb(0, 1, [-1, -1, -1, 1, 10, 0])  # Vothsg -- stabilizer output signal (pu)
psspy.chsb(0, 1, [-1, -1, -1, 1, 11, 0])  # Vref -- voltage regulator voltage setpoint(pu).

# 12 BSFreq : 母线频率（偏移）
psspy.chsb(0, 1, [-1, -1, -1, 1, 12, 0])  # BSFreq -- bus pu frequency deviations（偏移）.

# 13 Volt (Complex) ：母线电压（复数）
psspy.chsb(0, 1, [-1, -1, -1, 1, 13, 0])  # VOLT -- bus pu voltages (complex).

# 14 Volt & Angle ：电压 & 相角
psspy.chsb(0, 1, [-1, -1, -1, 1, 14, 0])  # voltage and angle

# 15~17 Flow ( P / P&Q / MVA) ：支路潮流
psspy.chsb(0, 1, [-1, -1, -1, 1, 15, 0])  # Flow(P)
psspy.chsb(0, 1, [-1, -1, -1, 1, 16, 0])  # Flow(P&Q)
psspy.chsb(0, 1, [-1, -1, -1, 1, 17, 0])  # Flow(MVA)

# 18 视在阻抗
psspy.chsb(0, 1, [-1, -1, -1, 1, 18, 0])  # Relay2(R&X) - apparent impedance (R and X)

# 19~20 : no data

# 21~24
psspy.chsb(0, 1, [-1, -1, -1, 1, 21, 0])  # ITERM - 迭代数
psspy.chsb(0, 1, [-1, -1, -1, 1, 22, 0])  # machine apparent impedance
psspy.chsb(0, 1, [-1, -1, -1, 1, 23, 0])  # VUEL, minimum excitation limiter output signal (pu).
psspy.chsb(0, 1, [-1, -1, -1, 1, 24, 0])  # VOEL, maximum excitation limiter output signal (pu).

# 25~26 Pload & Qload ：负荷有功 & 负荷无功
psspy.chsb(0, 1, [-1, -1, -1, 1, 25, 0])  # Pload
psspy.chsb(0, 1, [-1, -1, -1, 1, 26, 0])  # Qload

# 27~28
psspy.chsb(0, 1, [-1, -1, -1, 1, 27, 0])  # GREF, turbine governor reference
psspy.chsb(0, 1, [-1, -1, -1, 1, 28, 0])  # LCREF, turbine load control reference

# 29~37 关于风机的相关参数（略）







# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:28:01 2019

@author: MAHI7102
"""
class SteelPipe:
    def __init__(self, carrier_dia:int, segment1_length:float, segment2_length:float, service_temp:int = 80, buried_depth:float = 1, insulation:str = 'Standard', steel_marking:str = 'St 37.0', assembly_temp:float = 8):
        self.carrier_dia = carrier_dia
        self.service_temp = service_temp
        self.segment1_length = segment1_length
        self.segment2_length = segment2_length
        self.buried_depth = buried_depth
        self.insulation = insulation
        self.steel_marking = steel_marking
        self.assembly_temp = assembly_temp
        self.data_dict = {20: {'Dz': 26.9, 'g_welded': 2.6, 'g _seamless': 2.9, 'Dzp_standard_insulaion': 75, 'gp_standard_insulation': 3, 'Dzp_insulation_plus': 90, 'gp_insulation_puls': 3, 'E': 205, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850, 150: 20.2, 130: 17.3, 110: 14.5, 90: 11.7, 70: '8.8.', 50: 6, 'St37.0_g': 2.6, 'St37.0_A': 198, 'St37.0_W_si': 0.0158, 'St37.0_W_ip': 0.0193, 'St37.0_Rm ': 350, 'St37.0_Dzp': 75, 'St37.0_F': 1410, 'St37.0_Lmax': 22, 'R35_g ': 2.9, 'R35_A ': 219, 'R35_W _si': 0.0144, 'R35_W _ip': 0.0176, 'R35_Re ': 235, 'R35_A5 ': 25, 'R35_fd´ ': 210, 'R35_Rm ': 345, 'R35_Dz': 26.9, 'R35_Dzp': 75, 'R35_F': 1410, 'R35_Lmax': 24}, \
             25: {'Dz': 33.7, 'g_welded': 2.6, 'g _seamless': 2.9, 'Dzp_standard_insulaion': 90.0, 'gp_standard_insulation': 3.0, 'Dzp_insulation_plus': 110.0, 'gp_insulation_puls': 3.0, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 24.7, 130: 21.2, 110: 17.7, 90: 14.3, 70: 10.8, 50: 7.3, 'St37.0_g': 2.6, 'St37.0_A': 254.0, 'St37.0_W_si': 0.0124, 'St37.0_W_ip': 0.0151, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 90.0, 'St37.0_F': 1410.0, 'St37.0_Lmax': 28.0, 'R35_g ': 2.9, 'R35_A ': 281.0, 'R35_W _si': 0.0112, 'R35_W _ip': 0.0137, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 33.7, 'R35_Dzp': 90.0, 'R35_F': 1410.0, 'R35_Lmax': 31.0}, \
             32: {'Dz': 42.4, 'g_welded': 2.6, 'g _seamless': 2.9, 'Dzp_standard_insulaion': 110.0, 'gp_standard_insulation': 3.0, 'Dzp_insulation_plus': 125.0, 'gp_insulation_puls': 3.0, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 25.5, 130: 21.9, 110: 18.3, 90: 14.7, 70: 11.1, 50: 7.5, 'St37.0_g': 2.6, 'St37.0_A': 325.0, 'St37.0_W_si': 0.0118, 'St37.0_W_ip': 0.0134, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 110.0, 'St37.0_F': 1723.0, 'St37.0_Lmax': 29.0, 'R35_g ': 2.9, 'R35_A ': 360.0, 'R35_W _si': 0.0107, 'R35_W _ip': 0.0121, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 42.4, 'R35_Dzp': 110.0, 'R35_F': 1723.0, 'R35_Lmax': 32.0}, \
             40: {'Dz': 48.3, 'g_welded': 2.6, 'g _seamless': 2.9, 'Dzp_standard_insulaion': 110.0, 'gp_standard_insulation': 3.0, 'Dzp_insulation_plus': 125.0, 'gp_insulation_puls': 3.0, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 29.3, 130: 25.2, 110: 21.1, 90: 16.9, 70: 12.8, 50: 8.7, 'St37.0_g': 2.6, 'St37.0_A': 373.0, 'St37.0_W_si': 0.0103, 'St37.0_W_ip': 0.0117, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 110.0, 'St37.0_F': 1723.0, 'St37.0_Lmax': 34.0, 'R35_g ': 2.9, 'R35_A ': 414.0, 'R35_W _si': 0.0093, 'R35_W _ip': 0.0105, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 48.3, 'R35_Dzp': 110.0, 'R35_F': 1723.0, 'R35_Lmax': 38.0}, \
             50: {'Dz': 60.3, 'g_welded': 2.9, 'g _seamless': 3.2, 'Dzp_standard_insulaion': 125.0, 'gp_standard_insulation': 3.0, 'Dzp_insulation_plus': 140.0, 'gp_insulation_puls': 3.0, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 33.0, 130: 28.3, 110: 23.7, 90: 19.0, 70: 14.4, 50: 9.8, 'St37.0_g': 2.9, 'St37.0_A': 523.0, 'St37.0_W_si': 0.0083, 'St37.0_W_ip': 0.0093, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 125.0, 'St37.0_F': 1958.0, 'St37.0_Lmax': 42.0, 'R35_g ': 3.2, 'R35_A ': 574.0, 'R35_W _si': 0.0076, 'R35_W _ip': 0.0085, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 60.3, 'R35_Dzp': 125.0, 'R35_F': 1958.0, 'R35_Lmax': 46.0}, \
             65: {'Dz': 76.1, 'g_welded': 2.9, 'g _seamless': 3.2, 'Dzp_standard_insulaion': 140.0, 'gp_standard_insulation': 3.0, 'Dzp_insulation_plus': 160.0, 'gp_insulation_puls': 3.0, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 39.3, 130: 33.8, 110: 28.2, 90: 22.7, 70: 17.2, 50: 11.6, 'St37.0_g': 2.9, 'St37.0_A': 667.0, 'St37.0_W_si': 0.0073, 'St37.0_W_ip': 0.0084, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 140.0, 'St37.0_F': 2193.0, 'St37.0_Lmax': 49.0, 'R35_g ': 3.2, 'R35_A ': 733.0, 'R35_W _si': 0.0067, 'R35_W _ip': 0.0076, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 76.1, 'R35_Dzp': 140.0, 'R35_F': 2193.0, 'R35_Lmax': 53.0}, \
             80: {'Dz': 88.9, 'g_welded': 3.2, 'g _seamless': 3.6, 'Dzp_standard_insulaion': 160.0, 'gp_standard_insulation': 3.0, 'Dzp_insulation_plus': 200.0, 'gp_insulation_puls': 3.2, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 40.7, 130: 35.0, 110: 29.2, 90: 23.5, 70: 17.8, 50: 12.0, 'St37.0_g': 3.2, 'St37.0_A': 862.0, 'St37.0_W_si': 0.0065, 'St37.0_W_ip': 0.0081, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 160.0, 'St37.0_F': 2506.0, 'St37.0_Lmax': 55.0, 'R35_g ': 3.6, 'R35_A ': 965.0, 'R35_W _si': 0.0058, 'R35_W _ip': 0.0072, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 88.9, 'R35_Dzp': 160.0, 'R35_F': 2506.0, 'R35_Lmax': 61.0}, \
             100: {'Dz': 114.3, 'g_welded': 3.6, 'g _seamless': 4.0, 'Dzp_standard_insulaion': 200.0, 'gp_standard_insulation': 3.2, 'Dzp_insulation_plus': 225.0, 'gp_insulation_puls': 3.4, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 42.7, 130: 36.7, 110: 30.7, 90: 24.7, 70: 18.6, 50: 12.6, 'St37.0_g': 3.6, 'St37.0_A': 1252.0, 'St37.0_W_si': 0.0056, 'St37.0_W_ip': 0.0063, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 200.0, 'St37.0_F': 3132.0, 'St37.0_Lmax': 65.0, 'R35_g ': 4.0, 'R35_A ': 1386.0, 'R35_W _si': 0.005, 'R35_W _ip': 0.0057, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 114.3, 'R35_Dzp': 200.0, 'R35_F': 3132.0, 'R35_Lmax': 71.0}, \
             125: {'Dz': 139.7, 'g_welded': 3.6, 'g _seamless': 4.0, 'Dzp_standard_insulaion': 225.0, 'gp_standard_insulation': 3.4, 'Dzp_insulation_plus': 250.0, 'gp_insulation_puls': 3.6, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 49.9, 130: 42.8, 110: 35.8, 90: 28.8, 70: 21.8, 50: 14.7, 'St37.0_g': 3.6, 'St37.0_A': 1539.0, 'St37.0_W_si': 0.0051, 'St37.0_W_ip': 0.0057, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 225.0, 'St37.0_F': 3524.0, 'St37.0_Lmax': 72.0, 'R35_g ': 4.0, 'R35_A ': 1705.0, 'R35_W _si': 0.0046, 'R35_W _ip': 0.0051, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 139.7, 'R35_Dzp': 225.0, 'R35_F': 3524.0, 'R35_Lmax': 79.0}, \
             150: {'Dz': 168.3, 'g_welded': 4.0, 'g _seamless': 4.5, 'Dzp_standard_insulaion': 250.0, 'gp_standard_insulation': 3.6, 'Dzp_insulation_plus': 315.0, 'gp_insulation_puls': 4.1, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 59.6, 130: 51.2, 110: 42.8, 90: 34.4, 70: 26.0, 50: 17.6, 'St37.0_g': 4.0, 'St37.0_A': 2065.0, 'St37.0_W_si': 0.0042, 'St37.0_W_ip': 0.0053, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 250.0, 'St37.0_F': 3916.0, 'St37.0_Lmax': 88.0, 'R35_g ': 4.5, 'R35_A ': 2316.0, 'R35_W _si': 0.0038, 'R35_W _ip': 0.0047, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 168.3, 'R35_Dzp': 250.0, 'R35_F': 3916.0, 'R35_Lmax': 97.0}, \
             200: {'Dz': 219.1, 'g_welded': 4.5, 'g _seamless': 6.3, 'Dzp_standard_insulaion': 315.0, 'gp_standard_insulation': 4.1, 'Dzp_insulation_plus': 355.0, 'gp_insulation_puls': 4.5, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 65.1, 130: 56.0, 110: 46.8, 90: 37.6, 70: 28.4, 50: 19.3, 'St37.0_g': 4.5, 'St37.0_A': 3034.0, 'St37.0_W_si': 0.0036, 'St37.0_W_ip': 0.0041, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 315.0, 'St37.0_F': 4934.0, 'St37.0_Lmax': 104.0, 'R35_g ': 6.3, 'R35_A ': 4212.0, 'R35_W _si': 0.0026, 'R35_W _ip': 0.0029, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 219.1, 'R35_Dzp': 315.0, 'R35_F': 4934.0, 'R35_Lmax': 140.0}, \
             250: {'Dz': 273.0, 'g_welded': 5.0, 'g _seamless': 7.1, 'Dzp_standard_insulaion': 400.0, 'gp_standard_insulation': 4.8, 'Dzp_insulation_plus': 450.0, 'gp_insulation_puls': 5.2, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 62.5, 130: 53.7, 110: 44.9, 90: 36.1, 70: 27.3, 50: 18.5, 'St37.0_g': 5.0, 'St37.0_A': 4210.0, 'St37.0_W_si': 0.0033, 'St37.0_W_ip': 0.0037, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 400.0, 'St37.0_F': 6265.0, 'St37.0_Lmax': 115.0, 'R35_g ': 7.1, 'R35_A ': 5931.0, 'R35_W _si': 0.0024, 'R35_W _ip': 0.0026, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 273.0, 'R35_Dzp': 400.0, 'R35_F': 6265.0, 'R35_Lmax': 156.0}, \
             300: {'Dz': 323.9, 'g_welded': 5.6, 'g _seamless': 7.1, 'Dzp_standard_insulaion': 450.0, 'gp_standard_insulation': 5.2, 'Dzp_insulation_plus': 500.0, 'gp_insulation_puls': 5.6, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 72.3, 130: 62.1, 110: 52.0, 90: 41.8, 70: 31.6, 50: 21.4, 'St37.0_g': 5.6, 'St37.0_A': 5600.0, 'St37.0_W_si': 0.0028, 'St37.0_W_ip': 0.031, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 450.0, 'St37.0_F': 7048.0, 'St37.0_Lmax': 137.0, 'R35_g ': 7.1, 'R35_A ': 7066.0, 'R35_W _si': 0.0022, 'R35_W _ip': 0.0025, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 323.9, 'R35_Dzp': 450.0, 'R35_F': 7048.0, 'R35_Lmax': 168.0}, \
             350: {'Dz': 355.6, 'g_welded': 5.6, 'g _seamless': 8.0, 'Dzp_standard_insulaion': 500.0, 'gp_standard_insulation': 5.6, 'Dzp_insulation_plus': 560.0, 'gp_insulation_puls': 6.0, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 70.1, 130: 60.2, 110: 50.4, 90: 40.5, 70: 30.6, 50: 20.7, 'St37.0_g': 5.6, 'St37.0_A': 6158.0, 'St37.0_W_si': 0.0028, 'St37.0_W_ip': 0.0029, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 500.0, 'St37.0_F': 7831.0, 'St37.0_Lmax': 138.0, 'R35_g ': 8.0, 'R35_A ': 8736.0, 'R35_W _si': 0.002, 'R35_W _ip': 0.0021, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 355.6, 'R35_Dzp': 500.0, 'R35_F': 7831.0, 'R35_Lmax': 187.0}, \
             400: {'Dz': 406.4, 'g_welded': 6.3, 'g _seamless': 8.8, 'Dzp_standard_insulaion': 560.0, 'gp_standard_insulation': 6.0, 'Dzp_insulation_plus': 630.0, 'gp_insulation_puls': 6.6, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 74.6, 130: 64.1, 110: 53.6, 90: 43.1, 70: 32.6, 50: 22.1, 'St37.0_g': 6.3, 'St37.0_A': 7919.0, 'St37.0_W_si': 0.0023, 'St37.0_W_ip': 0.0025, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 560.0, 'St37.0_F': 8144.0, 'St37.0_Lmax': 158.0, 'R35_g ': 8.8, 'R35_A ': 10992.0, 'R35_W _si': 0.0017, 'R35_W _ip': 0.0018, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 406.4, 'R35_Dzp': 560.0, 'R35_F': 8144.0, 'R35_Lmax': 211.0}, \
             450: {'Dz': 457.0, 'g_welded': 6.3, 'g _seamless': 10.0, 'Dzp_standard_insulaion': 560.0, 'gp_standard_insulation': 6.0, 'Dzp_insulation_plus': 630.0, 'gp_insulation_puls': 6.6, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 74.7, 130: 64.2, 110: 53.7, 90: 43.2, 70: 32.6, 50: 22.1, 'St37.0_g': 6.3, 'St37.0_A': 8920.0, 'St37.0_W_si': 0.0022, 'St37.0_W_ip': 0.0025, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 630.0, 'St37.0_F': 8771.0, 'St37.0_Lmax': 161.0, 'R35_g ': 10.0, 'R35_A ': 14043.0, 'R35_W _si': 0.0014, 'R35_W _ip': 0.0016, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 457.0, 'R35_Dzp': 630.0, 'R35_F': 8771.0, 'R35_Lmax': 239.0}, \
             500: {'Dz': 508.0, 'g_welded': 6.3, 'g _seamless': 11.0, 'Dzp_standard_insulaion': 630.0, 'gp_standard_insulation': 6.6, 'Dzp_insulation_plus': 710.0, 'gp_insulation_puls': 7.2, 'E': 205.0, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850.0, 150: 72.0, 130: 61.9, 110: 51.8, 90: 41.6, 70: 31.5, 50: 21.3, 'St37.0_g': 6.3, 'St37.0_A': 9930.0, 'St37.0_W_si': 0.0022, 'St37.0_W_ip': 0.0025, 'St37.0_Rm ': 350.0, 'St37.0_Dzp': 710.0, 'St37.0_F': 9867.0, 'St37.0_Lmax': 162.0, 'R35_g ': 11.0, 'R35_A ': 17175.0, 'R35_W _si': 0.0013, 'R35_W _ip': 0.0014, 'R35_Re ': 235.0, 'R35_A5 ': 25.0, 'R35_fd´ ': 210.0, 'R35_Rm ': 345.0, 'R35_Dz': 508.0, 'R35_Dzp': 710.0, 'R35_F': 9867.0, 'R35_Lmax': 260.0}, \
             600: {'Dz': 610, 'g_welded': 7.1, 'g _seamless': '-', 'Dzp_standard_insulaion': 800, 'gp_standard_insulation': 7.9, 'Dzp_insulation_plus': 900, 'gp_insulation_puls': 8.7, 'E': 205, 'ν': 0.3, 'α (for T <100)': 1.2, 'α (for T >100)': 1.22, 'ρS': 7850, 150: 88.6, 130: 76.1, 110: 63.6, 90: 51.2, 70: 38.7, 50: 26.2, 'St37.0_g': 7.1, 'St37.0_A': 13448, 'St37.0_W_si': 0.0021, 'St37.0_W_ip': 0, 'St37.0_Rm ': '', 'St37.0_Dzp': 800, 'St37.0_F': 12530, 'St37.0_Lmax': 197, 'R35_g ': '', 'R35_A ': '', 'R35_W _si': '', 'R35_W _ip': '', 'R35_Re ': 235, 'R35_A5 ': 25, 'R35_fd´ ': 210, 'R35_Rm ': 345, 'R35_Dz': '', 'R35_Dzp': '', 'R35_F': '', 'R35_Lmax': 197.0}}
        self.E_dict = {150:(205.429,1.26), 140:(206,1.25), 130:(206.571,1.24), 120:(207.143,1.23), 110:(207.714,1.23), 105:(208,1.22), 100:(208.286,1.22), 95:(208.571,1.21), 90:(208.857,1.21), 85:(209.143,1.21), 80:(209.429,1.2), 75:(209.714,1.2), 70:(210,1.19), 65:(210.286,1.19), 60:(210.571,1.19), 55:(210.857,1.18)}

    def expansion(self):
        αT = self.E_dict[self.service_temp][1]
        if self.steel_marking == 'St 37.0'and self.insulation == 'Standard':
            W = self.data_dict[self.carrier_dia]['St37.0_W_si']
        elif self.steel_marking == 'St 37.0'and self.insulation == 'Plus':
            W = self.data_dict[self.carrier_dia]['St37.0_W_ip']
        elif self.steel_marking == 'R-35'and self.insulation == 'Standard':
            W = self.data_dict[self.carrier_dia]['R35_W _si']
        elif self.steel_marking == 'R-35'and self.insulation == 'Plus':
            W = self.data_dict[self.carrier_dia]['R35_W _ip']
        expansion_1 = round((αT*(self.service_temp-self.assembly_temp)*self.segment1_length/100) - (W*self.buried_depth*self.segment1_length**2),2)
        expansion_2 = round((αT*(self.service_temp-self.assembly_temp)*self.segment2_length/100) - (W*self.buried_depth*self.segment2_length**2),2)
        if expansion_1<0:
            expansion_1 = 0.0
        if expansion_2<0:
            expansion_2 = 0.0
        return expansion_1, expansion_2

    def data(self):
        data = self.data_dict[self.carrier_dia]
        return data

    def z_shape(self):
        ex_1 = self.expansion()
        dL1 = ex_1[0]
        dL2 = ex_1[1]
        dl = (dL1 + dL2)/1000
        if dl<0.03:
            dl = 0.03
        dz = (self.data()['Dz'])/1000
        fd = 150
        ET = self.E_dict[self.service_temp][0]*1000
        compenstaion_arm = round(((1.5*ET/fd)**0.5)*((dz*dl)**0.5),1)
        return compenstaion_arm, dL1, dL2

    def u_shape(self):
        ex_1 = self.expansion()
        dL1 = ex_1[0]
        dL2 = ex_1[1]
        dl = (dL1 + dL2)/1000
        if dl<0.03:
            dl = 0.03
        dz = (self.data()['Dz'])/1000
        fd = 150
        ET = self.E_dict[self.service_temp][0]*1000
        compenstaion_arm = round(0.7*((1.5*ET/fd)**0.5)*((dz*dl)**0.5),1)
        return compenstaion_arm, dL1, dL2
#
def main():
    sp_1 = SteelPipe(carrier_dia=600, segment1_length=197, segment2_length=197, service_temp=90, buried_depth=3, insulation='Standard', steel_marking='St 37.0')
    ex_1 = sp_1.expansion()
    print('ex_1 -',ex_1)
    c_z = sp_1.z_shape()
    print('z_shape -', c_z[0])
    c_u = sp_1.u_shape()
    print('u_shape -', c_u)


if __name__=='__main__':main()


# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 21:44:36 2019

@author: MAHI7102
"""

class Images:
    
    def __init__(self):
#        self.icon = ''''''
        self.u_shape = """R0lGODlhvABiAHAAACH5BAEAAPwALAAAAAC8AGIAhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwAr
                        ZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
                        mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMA
                        zDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
                        /zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YA
                        AGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaA
                        M2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/
                        Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplV
                        mZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnV
                        zJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr
                        /8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zV
                        AMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
                        M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+q
                        Zv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAA
                        AAj/APcJHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuX
                        MGPKnEmzps2bOHPq3Mmzp8+fQIMKHUq0qNGjSE/Si5FJ5LAYoE4uEyhJRrSOaMQkDRPqowo7AlWg
                        BCBQWA6Pk9Ik1TK1IzF6KwTGOKlsGI59884KrKcx06SB9IqGaZuJmEZl+8Js2gdj4CRoTveRbad3
                        n7K/GDNJEhhNmdqhMNoSi4pRmaZ9mdDsiytwEmKQyqL2+iFPr7J6ry9m+qxvn+GhNzQpk2Q647xJ
                        wzKJUYZDGbFMTUNKIqZpGJpMOfRNijaM9EVJrl0L/zf5m6O+tn33XSUYXeTp3gSHdTy/l2Pug8qU
                        ZYoBoDxFvhrxt5xW9fXWCDRocEHWRjHEsFx7BKWRjBg3LDiRPgAK1Fs08FVEDAA3DONaQsRkRSF0
                        mWgiiSZ+QTcJiyu2CB0lmrEo4yQt4qhjjjzuqMkNFKKRBjFv9AIdi2IoB2SLblCUiS9uKCMGDmFM
                        kuSOOKLRCA5L4niji2Dy6BeLO35pppdohgkdhWkQiBAxkOkE4UBvkDSnQHfiNEycONFzQ1IFzQXo
                        RvTA8JkmpyEFwxgCJTcoR4MJFFhSiyQaTYaPYsRVpmjAkalHW3i3TwzrFbUiQfSgkShO95UUmmVU
                        If+1iKfQvIYpXQpl8hoxrY40XBrKtdZrUGKkMQyjeKXBJ13ROWeQJtDw+tEwiDk3rELW7qPaTKot
                        U5dEulrmn0fKLENPnvuIMe5GnoVxAAD9pTgMi/NmUm919ioDbwBiMEJTGpLwF29yBNvLIr44JtMI
                        vEB+MtJuCCUD3a0a8VrPeb1huE890QTGscbLfLyMPhyiy9Jf1e4zFccCjbzxyirvAw1f9UgrEiP0
                        rDrQaYZlsqxGy/xM0bouXSuR0RjpowkxnbUaGJywfip1Q4jtGXVBmlA89dZvai1QMkJzLTZB0CaU
                        9dhoGzTMpAdBnfbb++hsGYqfMILi3XjnrffefPf/vbeXeH/mnt7A+m344WoijrckRx4k902YFWTy
                        RslQHDlJglL0OEG37XT5QER7tO7kHVk4EbUJoS6nQaQf1uvnIWViukRMk1gqTrDb/LBBsIM0yewR
                        ZcI25771hvRLsB/PLusntY4QYsRM1aFAvIJCDyXKt3Rn6KK32rvvFCktn7MFXbY5TXPmZ5L67J20
                        7UT1uFEYQmjIp1Py6/N+0vcO+YVQnezDHfrc5yHE3CkTAAoXTpy3vwZORD97OR9PPuc12BSEfx55
                        n0WmB5Q5NYku92FgRjA4tsvhJiUQEiFGSCi2FKoEQizcSAy3JjjUqORyMxwh3AzSi/appDwqvIgG
                        TXe4D8HpDiXtyeEKL1g7tLUnex/JTRAt8r6ldGwL6OHaFEWyRYpELgwSnJoSSTJGKg5EC2GUWhlF
                        skYvDkRVO4xOtFhisy5OpD36SFIA/1sokD2ipFZ4cuBAlDE8sWGGHlD8yG82Y5I2Agoz3CtJdNLI
                        kSHGMZDai5VJ7JiU6HCyNIhxpEQsCbe/zOwlPRMkEfchSo98EiKkfNsrOVLDkbTyKLfkSA8buUrH
                        7MNhMFFGnXjZy328gR4VBGEuHbJMogyjiS/5lkk+2MtMWC8mlzFJPdy0SkwkEyXLGCZJ0AA8uI0h
                        bCtRhr8kWc63jUgmsfxIO9MWz5UwsiTcJOJl3gAegKWlnwD9p0D9SdCAFnSgAZ0E4yLJLi99s5gQ
                        jahEJ3oQFQCslhTd2nL2sQVKZhQpaNCSDz46to2CkaRcCwNicOBRlKZzhdBJZEJk6mrSh7yPpuxa
                        TzNrOhAlwctg8wqqvKpD1OQ8pzDVIYZRC8NUpj7nqdAhBn9igIN68nQiksANMdSSMsSMrB4zg8bI
                        ppIyegSNY/ToDKy6Gla0RgMTvKLHTq+axWBe9a54zate98rXvvo1IgEBADs="""
        
        self.z_shape = """R0lGODlhvABiAAAAACH/C05FVFNDQVBFMi4wAwEBAAAh+QQBAAD8ACwAAAAAvABiAIcAAAAAADMA
                        AGYAAJkAAMwAAP8AKwAAKzMAK2YAK5kAK8wAK/8AVQAAVTMAVWYAVZkAVcwAVf8AgAAAgDMAgGYA
                        gJkAgMwAgP8AqgAAqjMAqmYAqpkAqswAqv8A1QAA1TMA1WYA1ZkA1cwA1f8A/wAA/zMA/2YA/5kA
                        /8wA//8zAAAzADMzAGYzAJkzAMwzAP8zKwAzKzMzK2YzK5kzK8wzK/8zVQAzVTMzVWYzVZkzVcwz
                        Vf8zgAAzgDMzgGYzgJkzgMwzgP8zqgAzqjMzqmYzqpkzqswzqv8z1QAz1TMz1WYz1Zkz1cwz1f8z
                        /wAz/zMz/2Yz/5kz/8wz//9mAABmADNmAGZmAJlmAMxmAP9mKwBmKzNmK2ZmK5lmK8xmK/9mVQBm
                        VTNmVWZmVZlmVcxmVf9mgABmgDNmgGZmgJlmgMxmgP9mqgBmqjNmqmZmqplmqsxmqv9m1QBm1TNm
                        1WZm1Zlm1cxm1f9m/wBm/zNm/2Zm/5lm/8xm//+ZAACZADOZAGaZAJmZAMyZAP+ZKwCZKzOZK2aZ
                        K5mZK8yZK/+ZVQCZVTOZVWaZVZmZVcyZVf+ZgACZgDOZgGaZgJmZgMyZgP+ZqgCZqjOZqmaZqpmZ
                        qsyZqv+Z1QCZ1TOZ1WaZ1ZmZ1cyZ1f+Z/wCZ/zOZ/2aZ/5mZ/8yZ///MAADMADPMAGbMAJnMAMzM
                        AP/MKwDMKzPMK2bMK5nMK8zMK//MVQDMVTPMVWbMVZnMVczMVf/MgADMgDPMgGbMgJnMgMzMgP/M
                        qgDMqjPMqmbMqpnMqszMqv/M1QDM1TPM1WbM1ZnM1czM1f/M/wDM/zPM/2bM/5nM/8zM////AAD/
                        ADP/AGb/AJn/AMz/AP//KwD/KzP/K2b/K5n/K8z/K///VQD/VTP/VWb/VZn/Vcz/Vf//gAD/gDP/
                        gGb/gJn/gMz/gP//qgD/qjP/qmb/qpn/qsz/qv//1QD/1TP/1Wb/1Zn/1cz/1f///wD//zP//2b/
                        /5n//8z///8AAAAAAAAAAAAAAAAI/wD3CRxIsKDBgwgTKlzIsKHDhxAjSpxIsaLFixgzatzIsaPH
                        jyBDihxJEc0+ZQA0kVzJsiVIaDGU7TPpsqbNmxAzETMpZtnJNzZvSMJJlCgxYvsA7AsjU1+affpc
                        DqNUtGrNTMqIudE0iVimqTbdPD1Jz6pZkdCsRh02aV80Yiqjnp1LV+ONMcNwKBtWt29FaEgTKpPp
                        12Omwh+VoWEUAEamNJIyAYhxI5OMLQbEoJmUaXNnzp49c56EJhNp05FPT5rk5jRk0284p4ltOlPn
                        nbVHY6KEKc2wNLXd+KLNWZKmyMRiUCaN2GNWfZluEN63Quc+rJ0dpm1eEA0apG25b/8crBBww0kq
                        lwYWX/Awe7qV3U5/T9+vmPkC5dbfb/X+QM78BWjVDSo1sk8y6Qmo4Eb14HeQPsQok0labzXk4IIY
                        FqSMGJmIIcZROkkIYoTEJHNUhJoMo4lXLO4UBmhmKRMeGhdmOBGHYkg32DBZgUJiVkBqYqIyQ/4o
                        CQ6ZaHJYPVYBhpWNGWUVEl/7bFcUc1BmOdJhjbin5ZcapSWlSUyCaeZGNJ1ZGJNltrlPmQX55OZA
                        cBLkE536DSSGmgNFQ+dZfvYpKJx1CipQoG8eFCiiArnBJ0H1MOqTT/REZaWhUB2aqaZuYbpoWfll
                        mpY+UVlapVulRmNpqfVEJRM0+kT/U1asoApUT517PkrQZm4wgolA7sSWxiQcblZaZBxOMiwmyn42
                        iSSTMNtaa6SR1gsayQ4b22joDZubaZNsCy5X4dZmGleZiJtJapkwy1qH8Hr5JZzEMGqQvBxtSFd4
                        ug6EL0F7gZRJDHTl2q9AUh60TIIdSUaXowcPNJZBAQt8Vlp71nhmxRr+uxG/RdXTVleXRmwQdCF5
                        jJMyN5i8kIQhgYyTn/XYVujBMu+zzHqGVSUXVvUA5fJJ+MFssVXk7UOPxnymKRA9KmcUdVF5HkwP
                        z0Z/lHNN9g5NUCaILjP1RWN7TdQwVkLt0Z3hVW02XdCUXZHcbxfFcc919xXYwh9FqEV33i5JmTWD
                        ArV1M+BFIaX20V0jjhPYi3/kntuO4+RGzR4Fii9SJVfeEooxD0SMGNCs4DlR9DC8kd8DKXW63X9L
                        xK/rob4e+OSEXzdQDH4uw7TtH9VjsEf86vPd78A794mBjZOdfFVXK0M5RX7G2svzsO8zfEZMCo39
                        TXxDo3pGVH5vE8ogeW9+4OXjvf7t/1V5OESx7tPW9O8n5mWE3AsUe/4YwVz8Pv8WIORlaHAVM+BC
                        /keX+UFpcPsYX0XC0zy6PGkmDnyg6nh0Ec3V5xPvYGCA0Ce5+ujDP5va2NYuUqYVFkZFT6qgjRJW
                        EJ5NhHX4syB5RLgfZUiQf/q400Tax571ZDBDkSOIPtKTQ4SURRkysNV7MtHEB6pMEzI5YkImoRQZ
                        1kUTdaJHoAhTFjG66mlv2g4ZdQaVaKxxGVFxIxqj0So5Kk1nUVkGNOqRlrTw0S1luRNh5iM2hJAQ
                        IZSC40k0lZxEcQeOy0iGW5jkp7L4cVGUfFOg9niqSGWqVp6ECpOi4kl9tIpOgTJlpthERynW75SJ
                        khXCbGgllVQwjprM5HVcSBf/RmCrM43ojRigtZkxSCINOHoWGhohCTSkgRFuaARpGgGZMURzM8gk
                        zTKjmYZlQqab1cqmdxpxzWEZS5m+fOYbGPHNZToTWq9Bwxgw4R8ZLfNZC1wMZCRhTHZCayhenIsC
                        ASgeGxJ0hDyEnr8A6Kd67QcyfopM7b6XBn3IZHtEMSAa0mNQhQz0UTA6C0YPggmeTcyjCQXTFgp2
                        HlB8TYsQfNsY9jGGKrJkKAwRwxYygQM+kk4gnaMTEc2WppRyhCZBbWNEBmnUgzokR2IAwHdsY5th
                        JMmqX7GNV6iKVaqiZDlMC6JTI+K2SWRlSUHko1r9JMs90pGOnCwLk+7TIC/V/0mIY12IJACwjOZ9
                        VCIyoQkAxiKXgI41ijYFyQ3aEoa6JTUkBNPZSEdiVhwsJVCSAAUs+8XLj0R2Hw5liTLSUBYa9ZSN
                        9JjsmfhnK/2UaiCvha1sMyWXkkVndMr4VUtOqKQwaCIMVJ3QSR9FQrYK5E5lWlSnAuXJCm5Hl3gV
                        VPU4dTKEHK6QfxIiTg92lKjyCEiDCa94IzQYd4h3MOQFr3rPu7TwgkIZ0Qtves+73vkqAzAymQwa
                        6AGtG4ihvZhYwXc6+6U3NDMNXlGRVVOkpF4w2KoJVpKCGayTq1Y4RUdRcFUz0QsIV1VJCa7wVyQs
                        4Q9TVUk6weZOqpUVr3hGtRJmeiyYmPbXvNr4xsfFsY4zEhAAOw=="""
        
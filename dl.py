import sys, os
from skillshare import Skillshare
from magic import cookie

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


def info():
    print(r"""	 

BBBBBBBBBBBBBBBBB   EEEEEEEEEEEEEEEEEEEEEENNNNNNNN        NNNNNNNNLLLLLLLLLLL                  OOOOOOOOO     TTTTTTTTTTTTTTTTTTTTTTTUUUUUUUU     UUUUUUUU   SSSSSSSSSSSSSSS 
B::::::::::::::::B  E::::::::::::::::::::EN:::::::N       N::::::NL:::::::::L                OO:::::::::OO   T:::::::::::::::::::::TU::::::U     U::::::U SS:::::::::::::::S
B::::::BBBBBB:::::B E::::::::::::::::::::EN::::::::N      N::::::NL:::::::::L              OO:::::::::::::OO T:::::::::::::::::::::TU::::::U     U::::::US:::::SSSSSS::::::S
BB:::::B     B:::::BEE::::::EEEEEEEEE::::EN:::::::::N     N::::::NLL:::::::LL             O:::::::OOO:::::::OT:::::TT:::::::TT:::::TUU:::::U     U:::::UUS:::::S     SSSSSSS
  B::::B     B:::::B  E:::::E       EEEEEEN::::::::::N    N::::::N  L:::::L               O::::::O   O::::::OTTTTTT  T:::::T  TTTTTT U:::::U     U:::::U S:::::S            
  B::::B     B:::::B  E:::::E             N:::::::::::N   N::::::N  L:::::L               O:::::O     O:::::O        T:::::T         U:::::D     D:::::U S:::::S            
  B::::BBBBBB:::::B   E::::::EEEEEEEEEE   N:::::::N::::N  N::::::N  L:::::L               O:::::O     O:::::O        T:::::T         U:::::D     D:::::U  S::::SSSS         
  B:::::::::::::BB    E:::::::::::::::E   N::::::N N::::N N::::::N  L:::::L               O:::::O     O:::::O        T:::::T         U:::::D     D:::::U   SS::::::SSSSS    
  B::::BBBBBB:::::B   E:::::::::::::::E   N::::::N  N::::N:::::::N  L:::::L               O:::::O     O:::::O        T:::::T         U:::::D     D:::::U     SSS::::::::SS  
  B::::B     B:::::B  E::::::EEEEEEEEEE   N::::::N   N:::::::::::N  L:::::L               O:::::O     O:::::O        T:::::T         U:::::D     D:::::U        SSSSSS::::S 
  B::::B     B:::::B  E:::::E             N::::::N    N::::::::::N  L:::::L               O:::::O     O:::::O        T:::::T         U:::::D     D:::::U             S:::::S
  B::::B     B:::::B  E:::::E       EEEEEEN::::::N     N:::::::::N  L:::::L         LLLLLLO::::::O   O::::::O        T:::::T         U::::::U   U::::::U             S:::::S
BB:::::BBBBBB::::::BEE::::::EEEEEEEE:::::EN::::::N      N::::::::NLL:::::::LLLLLLLLL:::::LO:::::::OOO:::::::O      TT:::::::TT       U:::::::UUU:::::::U SSSSSSS     S:::::S
B:::::::::::::::::B E::::::::::::::::::::EN::::::N       N:::::::NL::::::::::::::::::::::L OO:::::::::::::OO       T:::::::::T        UU:::::::::::::UU  S::::::SSSSSS:::::S
B::::::::::::::::B  E::::::::::::::::::::EN::::::N        N::::::NL::::::::::::::::::::::L   OO:::::::::OO         T:::::::::T          UU:::::::::UU    S:::::::::::::::SS 
BBBBBBBBBBBBBBBBB   EEEEEEEEEEEEEEEEEEEEEENNNNNNNN         NNNNNNNLLLLLLLLLLLLLLLLLLLLLLLL     OOOOOOOOO           TTTTTTTTTTT            UUUUUUUUU       SSSSSSSSSSSSSSS   
                                                                                                                                                                    


				Visit Us for more Cool Stuff: https://forums.benlotus.com/

                """)


if __name__ == "__main__":
    info()
    main()

# PKU IAAA #

    <User>                        <Docklet>                     <PKU IAAA>
    ----------------------------------------------------------------------

    login ------request:/login/------>
                                     |
     <----response:redirect to PKU----
     |
     -----------request:/login/-------------------------------------->
                                                                     |
                                                                  username
                                                                  password
                                                                     |
     <----response:token & redirect to Docklet------------------------
     |
     -----request:/login/ & token---->
                                     |
                                     -----request:validate token----->
                                                                     |
                                     <------response:user info--------
                                     |
     <---response:dashboard of user---

import React from 'react'
import { Router, Scene } from 'react-native-router-flux'











const RouterComponent = () => {







    return (







    <Root>







      <Router hideNavBar="true">







        <Scene key="root" hideNavBar="true">



           <Scene key="holaComponent" component={ holaComponent } title=" holaComponent "/>
        	//kukuriwi
        </Scene>







      </Router>







    </Root>







    );







  };















export default RouterComponent;




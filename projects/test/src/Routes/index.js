import { StackNavigator, DrawerNavigator } from 'react-navigation';
import mainComponent from '../Components/mainComponent';
import com1Component from "../Components/com1"
import com2Component from "../Components/com2"
import com3Component from "../Components/com3"
import com10Component from "../Components/com10"
import usuariosComponent from "../Components/usuarios"


const Router = StackNavigator({
	mainComponent: { screen: mainComponent, navigationOptions: { header:null, headerTitle: null }},
           com1Component: { screen: com1Component, navigationOptions: { header:null, headerTitle: null }},
           com2Component: { screen: com2Component, navigationOptions: { header:null, headerTitle: null }},
           com3Component: { screen: com3Component, navigationOptions: { header:null, headerTitle: null }},
           com10Component: { screen: com10Component, navigationOptions: { header:null, headerTitle: null }},
           usuariosComponent: { screen: usuariosComponent, navigationOptions: { header:null, headerTitle: null }},
          //kukuriwi
}  );
export default Router;

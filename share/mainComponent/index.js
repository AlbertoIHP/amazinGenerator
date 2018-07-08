import React, { Component } from 'react';
import { Drawer } from 'native-base';
import SideBar from './SideBar';
import { Container, Header, Title, Content, Footer, FooterTab, Button, Left, Right, Body, Icon, Text } from 'native-base';


import tab1 from './tab1Component'
// kukuriwiNewTabImport

export default class mainComponent extends Component {

  constructor(props)
  {
    super(props)
    this.state = 
    {
      title: 'mainComponent works',
      tabs: 
      [ 
        { name: 'tab1', active: true, jsx: <tab1 /> },  
        //kukuriwiNewTabStore
      ] 
    }
  }


  async activeTab( tabToActive )
  {
    let newTab = tabs.map( (tab) => {
      tab.active = tab.name === tabToActive ?  true : false
        return tab
     } )
  }


  closeDrawer = () => {
    this.drawer._root.close()
  };
  
  openDrawer = () => {
    this.drawer._root.open()
  };

  renderActiveTab()
  {
    return this.state.tabs.map( (tab) => (tab.active ? tab.jsx : null) )
  }

  render() 
  {



    return (
      <Drawer
        ref={(ref) => { this.drawer = ref; }}
        content={<SideBar navigation={this.props.navigation} />}
        onClose={() => this.closeDrawer()} >

          <Container>
            <Header>
              <Left>
                <Button transparent onPress={ () => this.openDrawer() }>
                  <Icon name='menu' />
                </Button>
              </Left>
              <Body>
                <Title>Header</Title>
              </Body>
              <Right />
            </Header>
            <Content>
                { this.renderActiveTab() }
            </Content>
              <Footer>
                <FooterTab>
                  <Button active={this.state.tab1} onPress={() => this.activeTab('tab1')}>
                    <Icon active={this.state.tab1} name="apps" />
                   <Text>tab1</Text>
                  </Button>
                {/* kukuriwiNewTabButton */}
                </FooterTab>
              </Footer>
          </Container>
      </Drawer>
    );
  }
}
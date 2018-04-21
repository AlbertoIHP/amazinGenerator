import React, { Component } from 'react';
import { Drawer } from 'native-base';
import SideBar from './SideBar';
import { Container, Header, Title, Content, Footer, FooterTab, Button, Left, Right, Body, Icon, Text } from 'native-base';

export default class mainComponent extends Component {

  constructor(props)
  {
    super(props)
    this.state = 
    {
      title: 'mainComponent works'
    }
  }



  closeDrawer = () => {
    this.drawer._root.close()
  };
  
  openDrawer = () => {
    this.drawer._root.open()
  };

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
              <Text>
                { this.state.title }
              </Text>
            </Content>
            <Footer>
              <FooterTab>
                <Button full>
                  <Text>Footer</Text>
                </Button>
              </FooterTab>
            </Footer>
          </Container>
      </Drawer>
    );
  }
}
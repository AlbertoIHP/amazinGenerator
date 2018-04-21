import React, { Component } from 'react';

import { Container, Header, Title, Content, Footer, FooterTab, Button, Left, Right, Body, Icon, Text } from 'native-base';

import styles  from './styles'



export default class usuariosComponent extends Component
{



  constructor( props )

  {

    super( props )

    this.state = 

    {

tittle: ' usuariosComponent works'
    }

  }



  render() 

  {

    return (

      <Container style={ styles.container } >

        <Header>

          <Left>

            <Button transparent onPress={ () => this.props.navigation.pop() }>

              <Icon name='ios-arrow-dropleft-outline' />

            </Button>

          </Left>

          <Body>

            <Title>Header</Title>

          </Body>

          <Right />

        </Header>

        <Content>

          <Text>

              { this.state.tittle }

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

    );

  }

}

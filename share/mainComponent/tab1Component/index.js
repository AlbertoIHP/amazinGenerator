import React, { Component } from 'react';
import { Container, Header, Title, Content, Footer, FooterTab, Button, Left, Right, Body, Icon, Text } from 'native-base';
import styles  from './styles'

export default class tab1 extends Component 
{

  constructor( props )
  {
    super( props )
    this.state = 
    {
      tittle: 'Tab tab1 works'
    }
  }

  render() 
  {
    return (
      <Container style={ styles.container } >
        <Content>
          <Text>
              { this.state.tittle }
          </Text>
        </Content>
      </Container>
    );
  }
}
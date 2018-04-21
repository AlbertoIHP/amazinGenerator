import React, { Component } from "react";
import { Image } from "react-native";
import {
  Content,
  Text,
  List,
  ListItem,
  Icon,
  Container,
  Left,
  Right,
  Badge
} from "native-base";
import styles from "./styles";


const drawerCover = require("./img/kikiriwi.png");
const drawerImage = require("./img/kikiriwi.png");
const datas = [
           { name: "com1Component",  route: "com1Component",  icon: "easel", bg: "#C5F442"},
           { name: "com2Component",  route: "com2Component",  icon: "easel", bg: "#C5F442"},
           { name: "com3Component",  route: "com3Component",  icon: "easel", bg: "#C5F442"},
           { name: "com10Component",  route: "com10Component",  icon: "easel", bg: "#C5F442"},
           { name: "usuariosComponent",  route: "usuariosComponent",  icon: "easel", bg: "#C5F442"},
          //kukuriwi
];
class SideBar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      shadowOffsetWidth: 1,
      shadowRadius: 4
    };
  }
  render() {
    return (
      <Container>
        <Content
          bounces={false}
          style={{ flex: 1, backgroundColor: "#fff", top: -1 }}  >
          <Image source={drawerCover} style={styles.drawerCover} />
          <Image square style={styles.drawerImage} source={drawerImage} />
          <List
            dataArray={datas}
            renderRow={data =>
              <ListItem
                button
                noBorder
                onPress={() => this.props.navigation.navigate(data.route)}
              >
                <Left>
                  <Icon
                    active
                    name={data.icon}
                    style={{ color: "#777", fontSize: 26, width: 30 }}
                  />
                  <Text style={styles.text}>
                    {data.name}
                  </Text>
                </Left>
                {data.types &&
                  <Right style={{ flex: 1 }}>
                    <Badge
                      style={{
                        borderRadius: 3,
                        height: 25,
                        width: 72,
                        backgroundColor: data.bg
                      }}
                    >
                      <Text
                        style={styles.badgeText}
                      >{`${data.types} Types`}</Text>
                    </Badge>
                  </Right>}
              </ListItem>}
          />
        </Content>
      </Container>
    );
  }
}
export default SideBar;
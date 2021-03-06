import React from 'react';
import * as $ from 'jquery';
import Cookies from 'js-cookie';


class PlatformName extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            result: null
        }
    }

    componentDidMount() {
        var x = this;
        const token = Cookies.get('auth');
        $.ajax({
            url: `${process.env.BASEURL}clients/${this.props.pk}/platforms/${this.props.plat}/`,
            type: 'get',
            headers: {'Authorization': `Token ${token}`}
        })
        .done((res) => {
            x.setState({result: res.name});
        })
        .fail((res) => {console.log(res.responseJSON);})
    }

    render() {return this.state.result}
}

export default PlatformName
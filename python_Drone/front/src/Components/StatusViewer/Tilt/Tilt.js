import React from 'react';
import styles from './Tilt.scss';
import classNames from 'classnames/bind';
import styled from 'styled-components';
import img from '../../../static/drone.png';
const cx = classNames.bind(styles);

const TiltStyles = styled.div`
  background-image: url('${img}');
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  width:300px;
  height: 200px;
  /* transition: all 0.2s; */
  color: white;
  position: relative;
  transform: rotateX(${props => props.pitch}deg) 
        rotate(${props => props.yaw * -1}deg) 
        rotateY(${props => props.roll * -1}deg);
  grid-column: 1 / -1;
`;

const Tilt = ({pitch, roll, yaw, height}) => {
    return(
            <div className={cx('tilt-wrap')}>
                <div className={cx('content')}>
                    PITCH: {pitch}
                </div>
                <div className={cx('content')}>
                    ROLL: {roll}
                </div>
                <div className={cx('content')}>
                    YAW: {yaw}
                </div>
                <div className={cx('content')}>
                    HEIGHT: {height/100}M
                </div>
                <TiltStyles pitch={pitch} roll={roll} yaw={yaw} />
            </div>
    );
};

Tilt.defaultProps = {
    pitch: 0,
    roll: 0,
    yaw: 0,
    height: 0
};

export default Tilt;
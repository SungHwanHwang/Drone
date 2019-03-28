// 차 후 소켓이 아닌, 파이썬으로 오는 데이터를 받아야 함
import React from 'react'
import styles from './StatusViewer.scss'
import classNames from 'classnames/bind';
import Tilt from './Tilt';
import Battery from './Battery';
import {useState, useEffect} from 'react';
import socket from '../../state/socket';

const cx = classNames.bind(styles);
const status = "Disconnect";

function useDroneState() {
    const [droneState, updateDroneState] = useState({});
    useEffect(() => {
        socket.on('dronestate', updateDroneState);
        return () => socket.removeListener('dronestate');
    }, []);
    return droneState;
}

function useSocket() {
    const [status, updateStatus] = useState('DISCONNECTED');
    useEffect(() => {
        socket.on('status', updateStatus);
        return () => socket.removeListener('status');
    }, []);
    return status;
}

const StatusViewer = () => {
    const status = useSocket();
    const droneState = useDroneState([]);
    return(
        <div className={cx('sv-session')}>
            <div>
                <Battery battery = {droneState.bat} />
            </div>
            <div>
                <Tilt
                    pitch = {droneState.pitch} 
                    roll = {droneState.roll}
                    yaw = {droneState.yaw}
                    height = {droneState.h}    
                />
            </div>
            <div className= {cx('status')}>STATUS: {status}</div>
        </div>
    );
};

export default StatusViewer;
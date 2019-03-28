import React from 'react';
import styles from './ControllSession.scss';
import classNames from 'classnames/bind';

//첫째줄
import {IoIosUndo, IoIosArrowDropup, IoIosRedo} from 'react-icons/io';

//둘째줄
import { IoIosArrowDropleft, IoMdAirplane, IoMdRemoveCircle,
         IoIosRemoveCircleOutline, IoIosArrowDropright } from 'react-icons/io';

//셋째줄
import {IoMdCloudUpload, IoIosArrowDropdown, IoMdCloudDownload} from 'react-icons/io';

const cx = classNames.bind(styles);
const ControllSession = ( { rotate9, rotate5, forward, left, 
                            right, takeoff, land, emergency,
                            up, back, down, flipL, flipR} ) => {
    return(
        <div className={cx('controll-session')}>
            <div className={cx('button')}>
                <div className = {cx('circle', 'rotate9')} onClick={rotate9}>
                    <IoIosUndo />
                </div>
            </div>
            <div className={cx('button')}>
                <div className = {cx('circle', 'forward')} onClick={forward}>
                    <IoIosArrowDropup />
                </div>
            </div>
            <div className={cx('button')}>
                <div className = {cx('circle', 'rotate5')} onClick={rotate5}>
                    <IoIosRedo />
                </div>
            </div>

            <div className={cx('button')}>
                <div className = {cx('circle', 'left')} onClick={left}>
                    <IoIosArrowDropleft />
                </div>
            </div>
            <div className={cx('center')}>
                <div className={cx('button')}>
                    <div className = {cx('circle', 'takeoff')} onClick={takeoff}>
                        <IoMdAirplane />
                    </div>
                </div>
                <div className={cx('button')}>
                    <div className = {cx('circle', 'land')} onClick={land}>
                        <IoIosRemoveCircleOutline />
                    </div>
                </div>
                <div className={cx('button')}>
                    <div className = {cx('circle', 'emergency')} onClick={emergency}>
                        <IoMdRemoveCircle />
                    </div>
                </div>
            </div>
            <div className={cx('button')}>
                <div className = {cx('circle', 'right')} onClick={right}>
                    <IoIosArrowDropright />
                </div>
            </div>

            <div className={cx('button')}>
                <div className = {cx('circle', 'up')} onClick={up}>
                    <IoMdCloudUpload />
                </div>
            </div>
            <div className={cx('button')}>
                <div className = {cx('circle', 'back')} onClick={back}>
                    <IoIosArrowDropdown />
                </div>
            </div>
            <div className={cx('button')}>
                <div className = {cx('circle', 'down')} onClick={down}>
                    <IoMdCloudDownload />
                </div>
            </div>
            <div className={cx('button')}>
                <div className = {cx('circle', 'flip l')} onClick={flipL}>
                    Flip Left
                </div>
            </div>
            <div className={cx('button')}>
            </div>
            <div className={cx('button')}>
                <div className = {cx('circle', 'flip r')} onClick={flipR}>
                    Flip right
                </div>
            </div>
        </div>
    );
};

export default ControllSession;


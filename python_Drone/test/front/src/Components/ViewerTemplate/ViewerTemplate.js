import React from 'react';
import styles from './ViewerTemplate.scss';
import classNames from 'classnames/bind';

const cx = classNames.bind(styles);
const ViewerTemplate = ( {controllSession, statusViewer} ) => {
    return(
        <div className = {cx('viewer-template')}>
            <header>
                Tello Controller
            </header>
            <div className={cx('viewer-wrapper')}>
                {controllSession}
                <div className={cx('controll-session-wrapper')}>
                    {statusViewer}
                </div>
            </div>
        </div>
    );
};

export default ViewerTemplate;
import React from 'react'
import { TabLeftHeader } from "../tab-left-header/tab-header.js"
import { TabLeftContent } from '../tab-left-content/index.js'

export const TabLeft = (props) => {
    return (
        <div className='tab-left'>
            <TabLeftHeader />
            <TabLeftContent bold={true} />
            {
                props.data &&
                props.data.map((item, index) => 
                    <TabLeftContent
                        key={index}
                        machine={item.name}
                        productNo={item.id}
                        status={item.status}
                    />
            )
            }
        </div>
    )
} 
import { TabRightContent } from "../tab-right-content"
import { TabRightHeader } from "../tab-right-header"

export const TabRight = ({ header, data }) => {
    return (
        <div className='tab-right'>
            <TabRightHeader header={header} />
            <TabRightContent hours={true} />
            {
                data &&
                data.map((item, index) =>
                    <TabRightContent
                        key={index}
                        partInfo={item.infos}
                        header={header}
                    />
                )
            }
        </div>
    )
}
<template>
    <div class="container">
        <CAccordion>
            <CAccordionItem :item-key="1">
                <CAccordionHeader>
                Ammenities
                </CAccordionHeader>
                <CAccordionBody>
                <strong>This is the first item's accordion body.</strong> It is hidden by default,
                until the collapse plugin adds the appropriate classes that we use to style each
                element. These classes control the overall appearance, as well as the showing and
                hiding via CSS transitions. You can modify any of this with custom CSS or overriding
                our default variables. It's also worth noting that just about any HTML can go within
                the <code>.accordion-body</code>, though the transition does limit overflow.
                </CAccordionBody>
            </CAccordionItem>
            <CAccordionItem :item-key="2">
                <CAccordionHeader>
                Data and Model information
                </CAccordionHeader>
                <CAccordionBody>
                <strong>This is the second item's accordion body.</strong> It is hidden by default,
                until the collapse plugin adds the appropriate classes that we use to style each
                element. These classes control the overall appearance, as well as the showing and
                hiding via CSS transitions. You can modify any of this with custom CSS or overriding
                our default variables. It's also worth noting that just about any HTML can go within
                the <code>.accordion-body</code>, though the transition does limit overflow.
                </CAccordionBody>
            </CAccordionItem>
            <CAccordionItem :item-key="3">
                <CAccordionHeader>
                Accordion Item #3
                </CAccordionHeader>
                <CAccordionBody>
                <strong>This is the third item's accordion body.</strong> It is hidden by default,
                until the collapse plugin adds the appropriate classes that we use to style each
                element. These classes control the overall appearance, as well as the showing and
                hiding via CSS transitions. You can modify any of this with custom CSS or overriding
                our default variables. It's also worth noting that just about any HTML can go within
                the <code>.accordion-body</code>, though the transition does limit overflow.
                </CAccordionBody>
            </CAccordionItem>
        </CAccordion>
    </div>
</template>

<script>
import { CAccordion, CAccordionItem, CAccordionHeader, CAccordionBody } from '@coreui/vue';

export default {
  name: "Accordion",
  props: {
    msg: String
  },
  components:{
    CAccordion,
    CAccordionItem,
    CAccordionHeader,
    CAccordionBody,
  },
}
</script>
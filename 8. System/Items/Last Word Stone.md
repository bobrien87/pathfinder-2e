---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Divine]]"]
price: "{'gp': 8}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventures: Troubles in Grayce"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small, palm-sized smooth crystal has a translucent gray coloration. But with a whisper from the lips of the desperate, a *last word stone* can be filled with a spark of memory, changing its appearance to an opaque, polished stone that is strangely warm to the touch. These divinely infused objects were initially created by Pharasmin priests to preserve a dying person's last moment of life should loved ones be delayed in their arrival at the dying person's side. But with the tragedy of Lastwall, *last word stones* have gained a new, more desperate purpose. Here, along the Gravelands border regions, refugees and adventurers have taken to using *last word stones* to impart important details to recipients outside of endangered places when it seems likely they won't survive to spread the news themselves.

**Activate—Capture Memory** `pf2:3` (concentrate, manipulate, mental)

**Requirements** The *last word stone* doesn't contain a memory

**Effect** You press an empty *last word stone* to an adjacent willing creature's head. The stone fills with an important memory from the creature's mind, then becomes opaque in appearance. The memory is duplicated, and remains in the target creature's thoughts, but no indication of what type of memory is held within the stone is discernible to anyone else. Which memory is placed in the *last word stone* is chosen by the creature from whom the memory is copied, and once a memory is stored, the stone can't be used again to Capture Memory. A stored memory can't contain much information beyond a single emotion and a hazy mental picture that, taken together, convey a short message of no more than 10 words—typically enough to impart final words of comfort to a loved one, or to warn one of a specific location that might be trapped, or to impart a bit of news about a noteworthy event. The limit of 10 words represents the hazy and sometimes confusing nature of the mental image.

**Activate—Reveal Memory** `pf2:3` (concentrate, manipulate, mental)

**Requirements** The *last word stone* contains a memory

**Effect** You hold the *last word stone* to your head and concentrate on its contents. A moment later, the stored memory plays out in your mind and the *last word stone* crumbles to dust in your hand.

**Source:** `= this.source` (`= this.source-type`)

---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Light]]", "[[Magical]]"]
price: "{'gp': 35}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #213: Thirst for Blood"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Farlight stones* are common in libraries, monasteries, labs, and other places where simple but silent communication is important. *Farlight stones* always come in linked pairs, and each of the fist-sized stones can be Activated independently.

**Activate—Light** `pf2:1` (manipulate)

**Effect** The stone begins to glow as a torch, shedding bright light in a 20-foot radius (and dim light to the next 20 feet). You can Activate the stone in this way again to end the effect.

**Activate—Color** `pf2:1` (concentrate)

**Requirements** The stone is glowing with light

**Effect** You change the color of the stone's light to any other color, which remains as long as the stone sheds light.

**Activate—Notify** `pf2:1` (concentrate)

**Requirements** The stone is glowing with light

**Effect** The stone's light begins to pulse. You can choose the rate of the pulse between slow, moderate, and fast. If the linked stone is within 15 miles, its center begins to glow in the same color and pulse at the same rate. You can use this activation to end the pulsing caused by a linked stone.

**Source:** `= this.source` (`= this.source-type`)

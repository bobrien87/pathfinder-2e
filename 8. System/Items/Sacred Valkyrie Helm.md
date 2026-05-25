---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Apex]]", "[[Holy]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 40000}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder #206: Bring the House Down"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Lightning crackles from the wings flanking this helm, which is emblazoned with images of valkyries in the service of benevolent deities. You gain a +3 item bonus to Athletics checks and gain electricity resistance 20. When you invest in the helm, you either increase your Strength modifier by 1 or increase it to +4, whichever would give you a higher score. If you are unholy, you become [[Drained]] 2 as long as you wear the helm.

**Activate—Path of the Pegasus** 10 minutes (concentrate)

**Frequency** once per day

**Effect** The *sacred valkyrie helm* casts interplanar teleport to your specifications. When you start this activation, each creature you target with this spell mounts a conjured pegasus who then carries them through reality to arrive at the specified location; each affected creature experiences the 10-minute activation as a kaleidoscopic ride through strange worlds and realities atop a pegasus's back.

**Activate—Storm's Arms** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** The helm casts a 9th-rank weapon storm to your specifications. At your option, all damage caused by this spell is electricity damage—in this option, the duplicated weapons created by the spell appear to be made of lightning.

**Source:** `= this.source` (`= this.source-type`)

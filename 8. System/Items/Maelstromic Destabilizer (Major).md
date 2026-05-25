---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Consumable]]", "[[Gadget]]", "[[Spirit]]"]
price: "{'gp': 2750}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A maelstromic destabilizer is a whirling gyroscope of burnished bronze and glass. It strengthens the bonds that hold a creature to this world by weakening those same bonds to every other nearby creature. When activated, the destabilizer emits a constant pleasant chime as it spins. For the next minute, the creature holding the gadget gains resistance 10 to spirit damage, while all creatures not immune to spirit damage in a @Template[type:emanation|distance:10] gains weakness 10 to spirit damage.

**Source:** `= this.source` (`= this.source-type`)

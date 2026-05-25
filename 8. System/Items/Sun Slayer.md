---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'gp': 1000}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This lesser reinforced wooden shield (Hardness 6, HP 64, BT 32) is painted with intricate, pale-blue knots. The wood has been magically enhanced against solar energy and heat. While you have this shield raised, you gain fire resistance 5.

**Activate—Sunset** `pf2:1` (darkness, manipulate)

**Frequency** once per day

**Requirements** You are in sunlight

**Effect** You raise your shield in the air toward the sunlight, eclipsing it. The area in a @Template[type:emanation|distance:60] becomes dim light for 1 minute.

**Source:** `= this.source` (`= this.source-type`)

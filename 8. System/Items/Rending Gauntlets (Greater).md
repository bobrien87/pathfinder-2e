---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 32000}"
usage: "wornbracers"
bulk: "L"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These heavy gloves are reinforced with thick animal hide and sharpened bone.

**Activate—Shredding Finisher** `pf2:1` (manipulate)

**Frequency** once per hour

**Requirements** You hit the same creature with two unarmed Strikes in the same round

**Effect** The gauntlets' spikes dig into the creature just before you tear them free, dealing 6d6 piercing damage.

**Source:** `= this.source` (`= this.source-type`)

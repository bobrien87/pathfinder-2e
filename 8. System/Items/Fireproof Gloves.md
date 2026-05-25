---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 650}"
usage: "worngloves"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

First developed by blacksmiths to move burning hot workpieces around, fireproof gloves then became popular with soldiers responsible for disabling bombs and magical traps. The thick tan gloves come up over the arm. When wearing these gloves, you gain fire resistance 5.

**Activate—Release Heat** `pf2:1` (concentrate, fire)

**Frequency** once per day

**Requirements** You have a free hand

**Effect** You take the heat that's built up in your gloves and discharge it onto an enemy. You deal 6d8 fire damage to one creature within reach (DC 26 [[Reflex]] save).

**Source:** `= this.source` (`= this.source-type`)

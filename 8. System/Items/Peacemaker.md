---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 35}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to a weapon

**Activate** a (concentrate, manipulate)

**Requirements** Your last action was an Interact action to stow the affixed firearm or crossbow.

This ragged piece of white cloth is wrapped around the grip, stock, or haft of the affixed weapon. When you activate the talisman, you gain the effects of a [[Sanctuary]] spell (DC 20) lasting for 1 minute. If you draw the affixed firearm, the effect ends immediately and the talisman crumbles.

**Source:** `= this.source` (`= this.source-type`)

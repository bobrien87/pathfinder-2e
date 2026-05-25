---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 400}"
usage: "affixed-to-melee-weapon"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to a weapon

**Activate** A (manipulate)

This small iron band has a shifting weight that helps equalize the affixed weapon's balance. When you activate it, you use [[Certain Strike]], as the fighter feat. You must meet the normal requirements, including those of the press trait.

If you have the Certain Strike feat, the failure effect increases to deal the weapon's normal damage.

**Source:** `= this.source` (`= this.source-type`)

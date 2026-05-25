---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 240}"
usage: "wornbelt"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You wear a brightly colored sash around your waist as a symbol of your new position. You're bound to make mistakes in this role, but if you can learn from them, perhaps you'll live long enough to become an officer. If you trigger a reaction from an enemy or a hazard, you gain a +1 circumstance bonus to saving throws you attempt as a result of that reaction and a +1 circumstance bonus to your AC against attacks made during that reaction.

**Activate—Heads Up!** `pf2:r` (concentrate)

**Frequency** once per hour

**Trigger** One of your allies triggers a reaction from an enemy or a hazard

**Effect** You share your hard-earned experience with your ally, giving them a +1 circumstance bonus to saving throws they attempt as a result of that reaction and a +1 circumstance bonus to their AC against attacks made during that reaction.

> [!danger] Effect: Heads Up!

**Source:** `= this.source` (`= this.source-type`)

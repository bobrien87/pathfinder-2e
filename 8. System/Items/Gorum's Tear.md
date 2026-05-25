---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 80}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder #209: Destroyer's Doom"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate, fortune)

**Trigger** You make an attack with the affixed weapon.

This teardrop-shaped piece of iron is a naturally occurring mineral, said to be a solidified tear of bellicose joy shed by Gorum during his battles. When you activate the Gorum's tear, you roll your next attack roll twice and take the better result, ignoring any circumstance penalties. You then become [[Off Guard]] to the creature you targeted until the beginning of your next turn.

**Source:** `= this.source` (`= this.source-type`)

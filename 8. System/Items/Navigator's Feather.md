---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 6}"
usage: "affixed-to-headgear"
bulk: "L"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate, fortune)

**Trigger** You would roll a Survival check to [[Sense Direction]] or [[Track]] but haven't rolled yet

**Requirements** You're trained in Survival.

This jaunty feather is affixed to headgear and can guide you in times of trouble, twisting to point in different directions. When you activate the talisman, you roll the triggering Survival check to Sense Direction or Track twice, and use the higher result.

For 24 hours, you gain a +1 circumstance bonus to Survival checks to Sense Direction, so long as you're navigating toward the same destination as when you activated the talisman, and a +1 circumstance bonus to Survival checks to Track, so long as you continue to Track the same creature as when you activated the talisman. After 24 hours, the feather disintegrates, becoming mundane dust that blows away on the breeze.

**Source:** `= this.source` (`= this.source-type`)

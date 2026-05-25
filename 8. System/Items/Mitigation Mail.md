---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Flexible]]", "[[Invested]]", "[[Magical]]", "[[Noisy]]"]
price: "{'gp': 700}"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 resilient chain mail* helps bind up your wounds when you're injured in battle, enabling you to continue fighting.

**Activate—Salve** `pf2:2` (concentrate, healing, manipulate, vitality)

**Frequency** once per day

**Effect** You restore @Damage[(5d10+10)[healing,vitality]|shortLabel|traits:concentrate,healing,manipulate,vitality] Hit Points.

**Source:** `= this.source` (`= this.source-type`)

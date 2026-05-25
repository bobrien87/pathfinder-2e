---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]"]
price: "{'gp': 1400}"
usage: "etched-onto-weapon-wo-holy-rune"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A holy weapon commands powerful celestial energy. Strikes made with it gain the holy trait and deal an extra 1d4 spirit damage, or an extra 2d4 against an unholy target. If you are unholy, you are [[Enfeebled]] 2 while carrying or wielding this weapon.

**Activate—Holy Healing** R (concentrate, healing, vitality)

**Frequency** once per day

**Trigger** You critically succeed at a Strike against an unholy creature with the weapon

**Effect** You regain HP equal to double the unholy creature's level.

**Craft Requirements** You are holy.

**Source:** `= this.source` (`= this.source-type`)

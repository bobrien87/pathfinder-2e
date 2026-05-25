---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]", "[[Unholy]]"]
price: "{'gp': 1400}"
usage: "etched-onto-weapon-wo-unholy-rune"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An *unholy* rune instills fiendish power into the etched weapon. Strikes made with it gain the unholy trait and deal an extra 1d4 spirit damage, or an extra 2d4 against a holy target. If you are holy, you are [[Enfeebled]] 2 while carrying or wielding this weapon.

**Activate—Unholy Bloodshed** R (concentrate)

**Frequency** once per day

**Trigger** You critically succeed at an attack roll against a holy creature with the weapon

**Effect** The target takes [[Persistent Bleed Damage]] equal to 1d8 per weapon damage die of the etched weapon.

**Craft Requirements** You are unholy.

**Source:** `= this.source` (`= this.source-type`)

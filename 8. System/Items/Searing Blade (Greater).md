---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Fire]]", "[[Magical]]", "[[Versatile p]]"]
price: "{'gp': 13800}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+3 greater striking Greater Flaming longsword* has an ornate brass hilt and a blade shaped like stylized flames. When wielded, the blade projects illumination resembling shimmering firelight, emitting dim light in a 10-foot radius.

**Activate—Shoot Fire** `pf2:2` (concentrate, manipulate)

**Effect** You cast the [[Ignition]] cantrip from the sword as a 9th-rank arcane spell, using your melee attack modifier with *searing blade* as your spell attack modifier.

**Activate—Radiate Flames** A (aura, concentrate, fire)

**Frequency** once per day

**Effect** A @Template[emanation|distance:10] of flame radiates from the *greater searing blade* for 1 minute. All weapon and unarmed attacks by you and your allies within the area gain the effect of the *flaming* property rune.

> [!danger] Effect: Aura: Searing Blade (Greater)

**Source:** `= this.source` (`= this.source-type`)

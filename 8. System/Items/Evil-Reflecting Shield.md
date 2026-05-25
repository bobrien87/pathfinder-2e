---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]"]
price: "{'gp': 1250}"
bulk: "1"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A bright, octagonal frame surrounds this circular dawnsilver shield, which itself is polished to a mirrorlike sheen that reflects clear and true. While you have this standard-grade dawnsilver shield (Hardness 5, HP 20 [BT 10]) raised, you gain its circumstance bonus to saving throws against spells with the unholy or void trait.

**Activate—Reflect Evil** `pf2:r` (concentrate, fortune)

**Frequency** once per day

**Trigger** You attempt a saving throw against an effect with the unholy or void traits

**Effect** Your saving throw result is considered one degree better than the actual result. If this effect turns a success into a critical success, you can reflect some of the effect's power as a wave of magical backlash back to the source of the triggering effect, as long as the source is within 30 feet. When you do so, the target must succeed at a DC 28 [[Fortitude]] save or become [[Stunned]] 1.

**Source:** `= this.source` (`= this.source-type`)

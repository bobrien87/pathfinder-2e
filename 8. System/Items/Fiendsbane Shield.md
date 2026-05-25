---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Holy]]", "[[Magical]]"]
price: "{'gp': 70}"
bulk: "1"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This low-grade silver shield is equipped with a *+1 shield boss* emblazoned with the image of a beheaded fiend. Any creature with the unholy trait that wields the shield becomes [[Enfeebled]] 2 and can't recover from this condition while wielding the shield.

**Activate—Silvery Backlash** `pf2:f` (concentrate, holy)

**Frequency** once per day

**Trigger** You Shield Block an attack from a creature with the unholy trait

**Effect** The fiendsbane shield's Hardness increases to 10, and the symbol of the beheaded demon lashes out in silvery ribbons, dealing 3d6 slashing damage (DC 19 [[Reflex]] save) to the creature whose attack you blocked. This damage is treated as silver for the purposes of weaknesses, resistances, and the like.

HardnessHPBT3126

**Source:** `= this.source` (`= this.source-type`)

---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Agile]]", "[[Finesse]]", "[[Holy]]", "[[Magical]]", "[[Versatile s]]", "[[Vitality]]"]
price: "{'gp': 15000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

From blade to pommel, this sword is carved from a branch of the now-extinct celestial peach tree. The blade of this *+3 greater striking holy vitalizing peachwood shortsword* has ancient runes that can permanently destroy the most powerful undead—if you are willing to pay the price.

An undead creature of 12th level or lower that takes damage from a Strike with the sword takes 10d6 vitality damage with a DC 35 [[Fortitude]] save. This damage is separate from the Strike itself and isn't included in any effect based on the Strike's damage.

**Activate—Violent Exorcism** `pf2:r` (concentrate)

**Frequency** once per day

**Trigger** You critically hit an undead creature with the sword

**Effect** The creature must succeed at a DC 35 [[Fortitude]] save or be destroyed. If the undead fails its saving throw and is destroyed, you suffer a backlash, taking 1d6 void damage per level of the destroyed undead.

**Source:** `= this.source` (`= this.source-type`)

---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]"]
price: "{'gp': 145}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This minor reinforcing wooden shield (Hardness 6, HP 56, BT 28) is made with a sturdy but flexible wood found in Tian Xia. It's painted with bold, bright colors in the style of a fiendish tiger head. In combat, the eyes of the tiger seem to follow the opponent.

**Activate—Tiger's Eyes** `pf2:1` (manipulate)

**Frequency** once per day

**Requirements** Your shield is raised

**Effect** The tiger's eyes glow and animate. The shield casts [[Ill Omen]] (DC 20) on a target within your melee range.

**Craft Requirements** Supply one casting of ill omen.

**Source:** `= this.source` (`= this.source-type`)

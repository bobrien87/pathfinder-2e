---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 55}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Each dose of weapon-weird oil is keyed to a particular melee weapon group, selected from among axe, brawling, club, flail, hammer, knife, pick, polearm, shield, spear, and sword. The oil creates a synergy between skill and weapon, enabling you to wield the weapon in unexpected ways. You must have proficiency with the original weapon to benefit from the oil; however, you use your proficiency rank with the oil's keyed group instead of the weapon's original group. Also, you apply the critical specialization effect from the oil's keyed group instead of the weapon's normal critical specialization effect. While the oil remains effective, the [[Grievous]] rune and similar magic react as if the weapon belongs to the oil's group. A weapon can be coated in only one type of weapon-weird oil at a time. Any new application of this oil supersedes any previous one. These effects last for 1 hour.

**Source:** `= this.source` (`= this.source-type`)

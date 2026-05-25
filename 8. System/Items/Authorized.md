---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]"]
price: "{'gp': 50}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Sharp needles impale anyone who attempts to wield this weapon other than its rightful owner. Each authorized rune is etched with the blood of a specific creature. If any other creature wields the weapon, needles immediately erupt from the weapon's hilt or shaft, dealing 1d8 piercing damage plus 1d4 persistent bleed damage to the wielder. If the weapon has a striking rune, this damage increases to 1d8 piercing damage per damage die and 1d4 persistent damage per damage die; this counts only the weapon's base die and dice from the striking rune. The persistent bleed damage can't end while the creature still holds the weapon. The spikes retract once the creature lets go.

When the rune is crafted, the crafter can choose to broaden the criteria for who can safely wield the item, expanding the users to creatures with a particular alignment, bloodline, or patron deity, as the crafter chooses. This criterion must be shared by the creature who contributed the blood for the rune.

**Source:** `= this.source` (`= this.source-type`)

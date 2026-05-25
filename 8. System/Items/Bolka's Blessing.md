---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Divine]]", "[[Magical]]"]
price: "{'gp': 160}"
usage: "etched-onto-clan-dagger"
bulk: "L"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This filigree grants you a +1 item bonus to Diplomacy checks and to Perception checks to [[Sense Motive]]. Additionally, once per day, the filigree symbol can be activated for a healing effect.

**Activate—Gift of Life** `pf2:1` (concentrate, healing, vitality)

**Frequency** once per day

**Effect** You regain @Damage[3d10[healing,vitality]|shortLabel] Hit Points.

**Source:** `= this.source` (`= this.source-type`)

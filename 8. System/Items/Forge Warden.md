---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'gp': 975}"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The religious symbol of Torag, the forge god-an ornate hammer of dwarven construction-adorns the face of this *lesser reinforcing steel shield* (Hardness 8, HP 72, BT 36). The shield is a religious symbol of Torag.

You and any adjacent allies have fire resistance 5 while you have the shield raised. When used for a Shield Block, the *forge warden* rings out like the hammer strike of a blacksmith, and the symbol glows as if lit by the fires of a furnace.

**Activate—Forge Fires** `pf2:f` (concentrate, fire)

**Trigger** You use the *forge warden* to Shield Block an adjacent creature's attack and the shield takes damage

**Effect** The attacking creature takes 2d6 fire damage.

**Source:** `= this.source` (`= this.source-type`)

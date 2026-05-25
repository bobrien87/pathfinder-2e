---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 60}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` (concentrate)

Made from a shaft of silver with a gleaming copper tip, the lightning rod shot crackles with electricity as it flies through the air. When a lightning rod shot strikes a target, it remains intact. It moves with a creature it struck, unless the GM determines otherwise, until that creature regains any Hit Points. If it doesn't stick to the target, it falls to the ground and becomes inactive. If the target of this shot is within 10 feet of any creature or target that takes electricity damage, the target of this shot takes 1 electricity for each die of damage taken by the nearby creature or target. If the target of this shot takes electricity damage from a spell or attack, it also takes 1 additional electricity damage for each die of damage dealt. If the spell or attack allows a saving throw to reduce the damage, the target of this shot takes a –1 circumstance penalty to the save. This shot remains active for 1 minute, after which it falls to the ground and crumbles to dust.

**Source:** `= this.source` (`= this.source-type`)

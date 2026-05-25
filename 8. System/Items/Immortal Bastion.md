---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Bulwark]]", "[[Entrench melee]]", "[[Hindering]]"]
price: "{'gp': 70000}"
bulk: "5"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This impressive *+3 greater resilient greater fortification bastion plate* is built like an impregnable castle, with multiple layers of defense and no weak points. When you activate the armor's deflect melee trait, you gain a +2 circumstance bonus to AC against melee attacks instead of +1, and you gain 10 temporary Hit Points that last until the start of your next turn.

> [!danger] Effect: Immortal Bastion

**Activate** `pf2:r` (concentrate)

**Frequency** once per day

**Trigger** You are reduced to 0 Hit Points or would die from a death effect

**Effect** You drop to 1 Hit Point instead of being reduced to 0 HP or dying, and you gain 100 temporary Hit Points that last until the start of your next turn.

**Activate** `pf2:r` (concentrate)

**Frequency** once per day

**Trigger** You would gain or increase the [[Doomed]] or [[Wounded]] condition

**Effect** You avoid gaining or increasing the condition. If the triggering effect imposes both doomed and wounded, choose only one to prevent. This doesn't remove either of the conditions if you already have them, nor does it prevent the same triggering effect from giving or increasing the prevented condition later.

**Source:** `= this.source` (`= this.source-type`)

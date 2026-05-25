---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 25}"
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

This ammunition bears a rune with three lines radiating out, each ending in a circle. When an activated bola shot hits a target, it deals nonlethal bludgeoning damage. Compare the attack roll to the target's Reflex DC to determine the shot's other effects.
- **Critical Success** The target falls [[Prone]] and is [[Stunned]] 1.
- **Success** The target falls prone.
- **Failure** No additional effect.

**Source:** `= this.source` (`= this.source-type`)
